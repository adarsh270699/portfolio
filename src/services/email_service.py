import os
import resend
from typing import Dict, Optional
from flask import current_app
from src.utils.helpers import validate_email, sanitize_input, get_environment_config

class EmailService:
    """Service class for handling email operations"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.env_config = get_environment_config()
        self.api_key = self._get_api_key()
        if self.api_key:
            resend.api_key = self.api_key
    
    def _get_api_key(self) -> str:
        """Get API key from config or environment"""
        if self.config and 'RESEND_API_KEY' in self.config:
            return self.config['RESEND_API_KEY']
        return self.env_config.get('resend_api_key') or os.getenv("RESEND_API_KEY")
    
    def _get_from_email(self) -> str:
        """Get from email from config"""
        if self.config and 'EMAIL_FROM' in self.config:
            return self.config['EMAIL_FROM']
        return self.env_config.get('email_from') or os.getenv('EMAIL_FROM', '')
    
    def _get_required_fields(self) -> list:
        """Get required fields from config"""
        if self.config and 'CONTACT_FORM_FIELDS' in self.config:
            return self.config['CONTACT_FORM_FIELDS']
        return ['name', 'email', 'subject', 'message']
    
    def _get_max_message_length(self) -> int:
        """Get maximum message length from config"""
        if self.config and 'MAX_MESSAGE_LENGTH' in self.config:
            return self.config['MAX_MESSAGE_LENGTH']
        return 1000
    
    def _get_contact_recipient_email(self) -> str:
        """Get the email address where contact form submissions should be sent"""
        if self.config and 'CONTACT_RECIPIENT_EMAIL' in self.config:
            return self.config['CONTACT_RECIPIENT_EMAIL']
        return os.getenv('CONTACT_RECIPIENT_EMAIL', '')
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML characters to prevent XSS"""
        if not text:
            return ""
        
        html_escape_table = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#x27;",
        }
        return "".join(html_escape_table.get(c, c) for c in str(text))
    

    def send_email(self, to: str, subject: str, html: str) -> Dict:
        """
        Send an email using Resend API
        
        Args:
            to (str): Recipient email address
            subject (str): Email subject
            html (str): Email HTML content
            
        Returns:
            Dict: Response from Resend API
        """
        if not self.api_key:
            return {"success": False, "error": "Invalid Configuration"}
        
        # Validate email address
        if not validate_email(to):
            return {"success": False, "error": "Invalid Configuration"}
        
        try:
            response = resend.Emails.send({
                "from": self._get_from_email(),
                "to": to,
                "subject": sanitize_input(subject),
                "html": html
            })
            return {"success": True, "data": response}
        except Exception as e:
             return {"success": False, "error": "Email Service Error"}
    
    def send_contact_form_email(self, form_data: Dict) -> Dict:
        """
        Send email from contact form
        
        Args:
            form_data (Dict): Contact form data containing name, email, subject, message
            
        Returns:
            Dict: Response indicating success or failure
        """
        try:
            # Get required fields from config
            required_fields = self._get_required_fields()
            
            # Validate required fields
            for field in required_fields:
                if not form_data.get(field):
                    return {"success": False, "error": f"Missing required field: {field}"}
            
            name = sanitize_input(form_data.get('name'))
            email = form_data.get('email')
            subject = sanitize_input(form_data.get('subject'))
            message = sanitize_input(form_data.get('message'))
            
            # Validate email
            if not validate_email(email):
                return {"success": False, "error": "Invalid Email Address"}
            
            # Validate message length
            max_length = self._get_max_message_length()
            if len(message) > max_length:
                return {"success": False, "error": f"Message too long. Maximum {max_length} characters allowed."}
            
            # Create HTML email content with proper escaping
            subject_prefix = self.env_config.get('email_subject_prefix', 'Portfolio Contact: ')
            html_content = f"""
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {self._escape_html(name)}</p>
            <p><strong>Email:</strong> {self._escape_html(email)}</p>
            <p><strong>Subject:</strong> {self._escape_html(subject)}</p>
            <p><strong>Message:</strong></p>
            <p>{self._escape_html(message).replace(chr(10), '<br>')}</p>
            """
            
            # Send email to the correct recipient (should be site owner, not form submitter)
            to_email = self._get_contact_recipient_email()
            result = self.send_email(to_email, f"{subject_prefix}{subject}", html_content)
            return result
            
        except Exception as e:
            return {"success": False, "error": "Internal Server Error"}
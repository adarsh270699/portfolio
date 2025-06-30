import os
from typing import Dict, Any
import re

def validate_email(email: str) -> bool:
    """
    Basic email validation
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    # Use regex for more robust email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def sanitize_input(text: str) -> str:
    """
    Basic input sanitization
    
    Args:
        text (str): Text to sanitize
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    if not isinstance(text, str):
        text = str(text)
    
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '"', "'", '&']
    for char in dangerous_chars:
        text = text.replace(char, '')
    
    return text.strip()

def get_environment_config() -> Dict[str, Any]:
    """
    Get environment-specific configuration
    
    Returns:
        Dict: Environment configuration
    """
    return {
        'debug': os.environ.get('DEBUG', 'False').lower() == 'true',
        'environment': os.environ.get('FLASK_ENV', 'development'),
        'resend_api_key': os.environ.get('RESEND_API_KEY'),
        'secret_key': os.environ.get('SECRET_KEY'),
        'email_from': os.environ.get('EMAIL_FROM', 'onboarding@resend.dev'),
        'email_subject_prefix': os.environ.get('EMAIL_SUBJECT_PREFIX', 'Portfolio Contact: ')
    }

def get_app_info() -> Dict[str, Any]:
    """
    Get application information from config
    
    Returns:
        Dict: Application information
    """
    try:
        from flask import current_app
        return {
            'name': current_app.config.get('APP_NAME', 'Portfolio'),
            'version': current_app.config.get('APP_VERSION', '1.0.0'),
            'debug': current_app.config.get('DEBUG', False)
        }
    except (RuntimeError, ImportError):
        # Outside of application context or Flask not available
        return {
            'name': 'Portfolio',
            'version': '1.0.0',
            'debug': False
        }
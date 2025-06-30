from flask import render_template, request, jsonify
from src.services.data_service import DataService
from src.services.email_service import EmailService
from typing import Dict, Any

class MainController:
    """Main controller for handling portfolio routes and operations"""
    
    def __init__(self, config=None):
        self.config = config
        self.data_service = DataService(config=config)
        self.email_service = EmailService(config=config)
    
    def index(self) -> str:
        """
        Handle the main page route
        
        Returns:
            str: Rendered HTML template
        """
        try:
            data = self.data_service.get_all_data()
        
            return render_template('index.html', 
                                 contact_info=data.get('contact_info', {}),
                                 content=data.get('content', {}))
        except Exception as e:
            # Fallback to empty data if there's an error
            return render_template('index.html', 
                                 contact_info={},
                                 content={})
    
    def send_email(self) -> tuple:
        """
        Handle email sending from contact form
        
        Returns:
            tuple: JSON response and status code
        """
        # Check if request method is POST
        if request.method != 'POST':
            return jsonify({
                'success': False,
                'message': 'Method not allowed',
                'error': 'Only POST requests are allowed'
            }), 405
        
        # Check content type for form data
        if not request.form and not request.is_json:
            return jsonify({
                'success': False,
                'message': 'Invalid request',
                'error': 'No form data or JSON data provided'
            }), 400

        try:
            # Get form data based on content type
            if request.is_json:
                form_data = request.get_json() or {}
            else:
                form_data = request.form.to_dict()
            
            # Send email using service (validation is handled in service)
            result = self.email_service.send_contact_form_email(form_data)
            if result['success']:
                return jsonify({
                    'success': True, 
                    'message': 'Email sent successfully'
                }), 200
            else:
                return jsonify({
                    'success': False, 
                    'message': 'Failed to send email', 
                    'error': result.get('error', 'Internal Server Error')
                }), 400
                
        except Exception as e:
            return jsonify({
                'success': False, 
                'message': 'Failed to send email', 
                'error': "Internal Server Error"
            }), 500
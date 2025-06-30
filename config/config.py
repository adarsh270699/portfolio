import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # File paths
    DATA_FOLDER = 'src/data'
    STATIC_FOLDER = 'src/static'
    TEMPLATE_FOLDER = 'src/templates'
    
    # Email configuration
    EMAIL_FROM = os.environ.get('EMAIL_FROM', '')
    CONTACT_RECIPIENT_EMAIL = os.environ.get('CONTACT_RECIPIENT_EMAIL', '')
    EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', 'Portfolio Contact: ')

    # Application settings
    APP_NAME = 'Portfolio'
    APP_VERSION = '1.0.0'
    
    # Contact form settings
    CONTACT_FORM_FIELDS = ['name', 'email', 'subject', 'message']
    MAX_MESSAGE_LENGTH = 1000
    
    # Data file names
    CONTACT_INFO_FILE = 'contact-info.json'
    CONTENT_FILE = 'content.json'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 
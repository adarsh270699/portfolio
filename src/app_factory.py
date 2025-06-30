from flask import Flask
from src.routes import main_bp
from config.config import config
import os

def create_app(config_name=None):
    """
    Application factory pattern for creating Flask app
    
    Args:
        config_name (str): Configuration name (development, production, testing)
        
    Returns:
        Flask: Configured Flask application
    """
    # Determine configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    # Create Flask app
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/static')
    
    # Load configuration - add error handling for invalid config names
    try:
        config_class = config[config_name]
        app.config.from_object(config_class)
        
        # Add config object to app for easy access
        app.config_object = config_class()
    except KeyError:
        raise ValueError(f"Unknown configuration name: {config_name}. Available configurations: {list(config.keys())}")
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    return app
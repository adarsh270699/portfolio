from flask import Blueprint, send_from_directory, current_app, abort
from src.controllers.main_controller import MainController
import os

# Create blueprint for main routes
main_bp = Blueprint('main', __name__)

def get_main_controller():
    """Get main controller with current app config"""
    return MainController(config=current_app.config)

@main_bp.route('/')
def index():
    """Main page route"""
    controller = get_main_controller()
    return controller.index()

@main_bp.route('/email/send', methods=['POST'])
def send_email():
    """Email sending route"""
    controller = get_main_controller()
    return controller.send_email()

@main_bp.route('/<path:path>')
def serve_static_files(path):
    """Serve static files"""
    # Security check: prevent directory traversal attacks
    if '..' in path or path.startswith('/'):
        abort(404)
    
    # Ensure the static directory exists and file is within it
    static_dir = os.path.join(current_app.root_path, 'static')
    requested_file = os.path.join(static_dir, path)
    
    # Normalize paths and check if requested file is within static directory
    static_dir = os.path.abspath(static_dir)
    requested_file = os.path.abspath(requested_file)
    
    if not requested_file.startswith(static_dir):
        abort(404)
    
    return send_from_directory(static_dir, path)
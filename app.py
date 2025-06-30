from src.app_factory import create_app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
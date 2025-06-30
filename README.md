# Portfolio Website

A modern, responsive portfolio website built with Flask using professional MVC architecture, comprehensive security features, and modern development practices.

## Features

### Core Features

-   **Responsive Design**: Works perfectly on all devices and screen sizes
-   **Modern UI**: Clean, professional design with CSS animations
-   **Contact Form**: Functional contact form with email integration and validation
-   **Fast Loading**: Optimized for performance and user experience
-   **SEO Friendly**: Proper meta tags, semantic HTML structure

### Technical Features

-   **MVC Architecture**: Well-organized, maintainable codebase following best practices
-   **Comprehensive Testing**: Unit and integration tests with security validation
-   **Security Features**: Input validation, XSS prevention, directory traversal protection
-   **Error Handling**: Proper HTTP status codes and graceful error handling
-   **Configuration Management**: Environment-based configuration with validation
-   **Type Safety**: Full type hints and documentation throughout

## Technologies Used

### Backend

-   **Framework**: Flask (Python) with MVC architecture
-   **Email Service**: Resend API for reliable email delivery
-   **Configuration**: Environment-based configuration system
-   **Testing**: Python unittest framework with comprehensive coverage

### Frontend

-   **Technologies**: HTML5, CSS3, Modern JavaScript
-   **Styling**: Custom CSS with modern design principles and responsive layout
-   **Assets**: Optimized SVG illustrations and documents

### Security & DevOps

-   **Security**: Input validation, XSS prevention, secure file serving
-   **Deployment**: Vercel with optimized build configuration
-   **Documentation**: Comprehensive technical documentation

## Project Structure

```
portfolio/
├── src/                    # Source code directory
│   ├── controllers/        # HTTP request handlers with validation
│   │   └── main_controller.py
│   ├── services/           # Business logic and external integrations
│   │   ├── email_service.py    # Email processing with security
│   │   └── data_service.py     # Data management with error handling
│   ├── utils/              # Utility functions and helpers
│   │   └── helpers.py          # Input validation and sanitization
│   ├── static/             # Static assets
│   │   ├── css/           # Stylesheets with responsive design
│   │   ├── js/            # JavaScript functionality
│   │   ├── images/        # SVG illustrations and icons
│   │   └── documents/     # PDFs and other documents
│   ├── templates/          # HTML templates
│   ├── data/               # JSON configuration files
│   ├── routes.py           # URL routing with security
│   └── app_factory.py      # Application factory pattern
├── config/                 # Configuration files
│   └── config.py          # Environment-specific settings
├── docs/                   # Comprehensive documentation
│   ├── ARCHITECTURE.md    # Architecture overview
│   ├── CONFIGURATION.md   # Configuration guide
│   ├── SECURITY.md        # Security documentation
│   └── README.md          # Project structure guide
├── tests/                  # Test files with security tests
├── deployment/             # Deployment configuration
├── app.py                  # Main application entry point
└── requirements.txt        # Python dependencies
```

## Architecture

The application follows a professional **Model-View-Controller (MVC)** pattern with enhanced security:

### Controllers

-   Handle HTTP requests with comprehensive validation
-   Coordinate between services and views
-   Implement proper error handling and status codes

### Services

-   Contain all business logic and external integrations
-   Implement security features and input validation
-   Handle email processing with XSS prevention

### Utils

-   Provide common utility functions and helpers
-   Implement input validation and sanitization
-   Handle environment configuration

### Security Features

-   **Input Validation**: Robust email and form validation
-   **XSS Prevention**: HTML escaping and content sanitization
-   **Path Security**: Directory traversal protection
-   **Error Handling**: Secure error responses without information leakage

## Quick Start

### Prerequisites

-   Python 3.8 or higher
-   pip package manager
-   Git

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/adarsh270699/portfolio.git
    cd portfolio
    ```

2. **Create and activate virtual environment:**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    ```bash
    # Required
    export RESEND_API_KEY="your_resend_api_key_here"

    # Optional (with sensible defaults)
    export FLASK_ENV="development"
    export DEBUG="true"
    export EMAIL_FROM="portfolio@yourdomain.com"
    export CONTACT_RECIPIENT_EMAIL="your_email@domain.com"
    export SECRET_KEY="your_secret_key_for_production"
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    Open your browser and navigate to `http://127.0.0.1:5000/`

## Configuration

### Environment Variables

| Variable                  | Required | Default                 | Description               |
| ------------------------- | -------- | ----------------------- | ------------------------- |
| `RESEND_API_KEY`          | Yes      | -                       | API key for email service |
| `FLASK_ENV`               | No       | `development`           | Application environment   |
| `DEBUG`                   | No       | `False`                 | Enable debug mode         |
| `EMAIL_FROM`              | No       | `portfolio@example.com` | Sender email address      |
| `CONTACT_RECIPIENT_EMAIL` | No       | `recipient@example.com` | Contact form recipient    |
| `SECRET_KEY`              | No       | Auto-generated          | Flask secret key          |

### Configuration Files

-   **`config/config.py`**: Main configuration with environment-specific settings
-   **`src/data/`**: JSON files for portfolio content and contact information
-   **`deployment/vercel.json`**: Deployment configuration for Vercel

## Security

### Security Features

-   **Input Validation**: Email regex validation and form field validation
-   **XSS Prevention**: HTML escaping and content sanitization
-   **Path Security**: Directory traversal protection for static files
-   **CSRF Protection**: Request validation and proper HTTP methods
-   **Error Handling**: Secure error responses without sensitive information

### Security Testing

-   Input validation tests
-   XSS prevention verification
-   Path traversal protection tests
-   HTTP method validation
-   Error handling security

## Deployment

### Vercel Deployment (Recommended)

1. **Connect Repository**: Link your GitHub repository to Vercel
2. **Set Environment Variables**: Configure required environment variables
3. **Deploy**: Automatic deployment on push to main branch

### Manual Deployment

1. **Prepare Environment**: Set production environment variables
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run Application**: `python app.py` (consider using WSGI server for production)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

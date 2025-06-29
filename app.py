from flask import Flask, send_from_directory
import json
from flask import render_template, request, jsonify

app = Flask(__name__)

# Load contact info from JSON file
with open('data/contact-info.json', 'r') as file:
    contact_info = json.load(file)

# Load content from JSON file
with open('data/content.json', 'r') as file:
    content = json.load(file)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', contact_info=contact_info, content=content)

# Route to serve all other static files
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('./static', path)

@app.route('/email/send', methods=['POST'])
def send_email():
    try:
        data = request.form
        print(data)
        return jsonify({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Failed to send email'})


if __name__ == '__main__':
    app.run(debug=True) 
"""
Grissom Corporate Services - Flask Application
A modern corporate services website built with Flask
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')

# Configuration
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

# Home route
@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    """Render the contact page"""
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    """Render the privacy page"""
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    """Render the terms of use page"""
    return render_template('terms.html')

# Contact form endpoint (example)
@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Validate input
        if not all([name, email, message]):
            return jsonify({
                'status': 'error',
                'message': 'All fields are required'
            }), 400
        
        # Here you would typically save to database or send email
        # For now, just log the submission
        print(f"Contact form submission: {name} ({email})")
        print(f"Message: {message}")
        
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your inquiry. We will get back to you soon.'
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }), 500

# Health check endpoint
@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

# Context processor for template variables
@app.context_processor
def inject_now():
    """Inject current year for footer"""
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    # Create static directories if they don't exist
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static', 'images'), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static', 'logos'), exist_ok=True)
    
    # Run the Flask development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

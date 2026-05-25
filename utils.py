"""
Utility functions and helpers for Grissom Flask Application
"""

from functools import wraps
from flask import jsonify
import json


def api_response(data=None, message=None, status='success', status_code=200):
    """
    Create a standardized API response
    
    Args:
        data: Response data (optional)
        message: Response message (optional)
        status: Response status ('success', 'error', 'warning')
        status_code: HTTP status code
    
    Returns:
        Tuple of (response dict, status_code)
    """
    response = {
        'status': status,
    }
    
    if message:
        response['message'] = message
    if data is not None:
        response['data'] = data
    
    return jsonify(response), status_code


def validate_email(email):
    """
    Basic email validation
    
    Args:
        email: Email address to validate
    
    Returns:
        Boolean indicating if email is valid
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def truncate_text(text, length=100, suffix='...'):
    """
    Truncate text to specified length
    
    Args:
        text: Text to truncate
        length: Maximum length
        suffix: Suffix to add if truncated
    
    Returns:
        Truncated text
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def format_date(date_obj, format_str='%B %d, %Y'):
    """
    Format date object to string
    
    Args:
        date_obj: Date object to format
        format_str: Format string
    
    Returns:
        Formatted date string
    """
    if date_obj is None:
        return None
    return date_obj.strftime(format_str)


def log_request_info(func):
    """
    Decorator to log request information
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        from flask import request
        from datetime import datetime
        
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] {request.method} {request.path}")
        
        return func(*args, **kwargs)
    
    return decorated_function


def require_json(f):
    """
    Decorator to require JSON content type
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from flask import request
        
        if not request.is_json:
            return api_response(
                message='Content-Type must be application/json',
                status='error',
                status_code=400
            )
        
        return f(*args, **kwargs)
    
    return decorated_function


def handle_errors(f):
    """
    Decorator to handle common errors
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            return api_response(
                message=f'Invalid value: {str(e)}',
                status='error',
                status_code=400
            )
        except KeyError as e:
            return api_response(
                message=f'Missing required field: {str(e)}',
                status='error',
                status_code=400
            )
        except Exception as e:
            return api_response(
                message=f'An error occurred: {str(e)}',
                status='error',
                status_code=500
            )
    
    return decorated_function

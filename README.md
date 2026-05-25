# Grissom Corporate Services - Flask Application

A modern, responsive Flask web application for Grissom Corporate Services with beautiful animations and smooth scroll effects.

## Project Structure

```
flask-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Main HTML template (Jinja2)
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    ├── js/
    │   └── main.js       # JavaScript animations and interactivity
    ├── images/           # Background and section images
    │   ├── hero-left.jpg
    │   ├── what-we-do.jpg
    │   └── approach.jpg
    └── logos/            # Company logos
        └── grissom-logo.svg
```

## Features

- **Responsive Design**: Mobile-first approach with breakpoints for tablets and desktops
- **Smooth Animations**: CSS transitions and JavaScript intersection observer animations
- **Modern UI**: Minimalist design with serif and sans-serif typography
- **Progress Bar**: Scroll progress indicator at the top of the page
- **Contact Form API**: REST endpoint for contact form submissions
- **Dynamic Navigation**: Fixed navigation bar with scroll effects
- **Accessibility**: Reduced motion media query support for users with motion sensitivity

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the flask-app directory**
   ```bash
   cd flask-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add images to the static folder**
   - Place your images in `static/images/`:
     - `hero-left.jpg` (Hero section background)
     - `what-we-do.jpg` (What We Do section image)
     - `approach.jpg` (Approach section background)
   
   - Place your logos in `static/logos/`:
     - `grissom-logo.svg` (or any logo format)

## Running the Application

### Development Mode
```bash
python app.py
```

The application will start at `http://localhost:5000`

### Production Mode
For production deployment, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### GET /
Home page - renders the main landing page

### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00"
}
```

### POST /api/contact
Submit a contact form inquiry

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Your message here"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Thank you for your inquiry. We will get back to you soon."
}
```

## Customization

### Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
  --navy: #0a1456;
  --navy-deep: #0e1a34;
  --white: #ffffff;
  --off-white: #f8f7f4;
  --light-grey: #e8e6e0;
  --mid-grey: #b0aaa0;
  --text-muted: #6b6560;
}
```

### Fonts
Fonts are imported from Google Fonts in the HTML template:
- **Serif**: Cormorant Garamond (titles and headers)
- **Sans-serif**: DM Sans (body text)

You can change these in `templates/index.html`

### Content
Edit the HTML content in `templates/index.html` to update text, headings, and sections.

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 14+, Chrome Mobile)

## Performance Optimization

The application includes:
- CSS minification-ready structure
- Lazy loading for background images
- Optimized animations using CSS transforms
- Intersection Observer for scroll-triggered animations

## Troubleshooting

### Port 5000 is already in use
```bash
# Change the port in app.py or run on a different port
python app.py --port 8000
```

### Images not loading
- Ensure images are placed in `static/images/` directory
- Check the image file names match the HTML references
- Use absolute paths with `url_for()` in templates

### Animations not working
- Check browser console for JavaScript errors
- Ensure `static/js/main.js` is loaded correctly
- Verify CSS transitions are not disabled in browser settings

## Deployment

### Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Environment Variables
Create a `.env` file for configuration:
```
FLASK_ENV=production
FLASK_DEBUG=False
```

## License

© 2024 Grissom Corporate Services. All rights reserved.

## Support

For issues or questions, contact: info@grissomsa.com

# Grissom Flask App - Quick Start Guide

## 🚀 Installation (5 minutes)

### Step 1: Navigate to the Flask app directory
```bash
cd flask-app
```

### Step 2: Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add placeholder images
Create or place these images in `static/images/`:
- `hero-left.jpg` - Hero section background
- `what-we-do.jpg` - Service section image  
- `approach.jpg` - Approach section background

You can use placeholder images from:
- [Unsplash](https://unsplash.com/)
- [Pexels](https://www.pexels.com/)
- [Pixabay](https://pixabay.com/)

### Step 5: Run the application
```bash
python app.py
```

Open your browser and navigate to: **http://localhost:5000**

---

## 📁 Project Structure Overview

```
flask-app/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── utils.py                        # Utility functions
├── requirements.txt                # Python dependencies
├── requirements-dev.txt            # Development dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── README.md                       # Full documentation
├── QUICKSTART.md                   # This file
│
├── templates/
│   └── index.html                  # Main HTML template (Jinja2)
│
└── static/
    ├── css/
    │   └── style.css               # Main stylesheet (extracted CSS)
    ├── js/
    │   └── main.js                 # JavaScript animations
    ├── images/
    │   ├── README.md               # Image guidelines
    │   ├── hero-left.jpg           # (Add your image)
    │   ├── what-we-do.jpg          # (Add your image)
    │   └── approach.jpg            # (Add your image)
    └── logos/
        └── README.md               # Logo guidelines
```

---

## 🛠️ Common Tasks

### Add Your Company Logo
1. Save your SVG logo as `static/logos/grissom-logo.svg`
2. Create a white version as `static/logos/grissom-logo-white.svg`
3. The navigation bar will automatically use it

### Update Contact Email
1. Open `templates/index.html`
2. Find `info@grissomsa.com` (appears 3 times)
3. Replace with your email address

### Change Brand Colors
1. Open `static/css/style.css`
2. Edit the CSS variables at the top:
```css
:root {
  --navy: #0a1456;              /* Main brand color */
  --navy-deep: #0e1a34;         /* Dark variant */
  --off-white: #f8f7f4;         /* Background */
  /* ... more colors ... */
}
```

### Add New Section
1. Add HTML in `templates/index.html`
2. Add CSS styles in `static/css/style.css`
3. Add JavaScript animations in `static/js/main.js` if needed

---

## 🌐 Deployment Options

### Heroku (Free tier available)
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
```

### PythonAnywhere
1. Sign up at https://www.pythonanywhere.com
2. Upload your files
3. Configure web app to use Flask

### AWS/Google Cloud
Use Docker for easy deployment:
```bash
docker build -t grissom-flask .
docker run -p 5000:5000 grissom-flask
```

---

## 📝 Customization Checklist

- [ ] Add company logo to `static/logos/`
- [ ] Add images to `static/images/`
- [ ] Update email address in HTML
- [ ] Customize brand colors in CSS
- [ ] Update company name and content in HTML
- [ ] Test all links and navigation
- [ ] Test on mobile devices
- [ ] Configure analytics (Google Analytics optional)

---

## 🐛 Troubleshooting

### Port 5000 already in use
```bash
# Use a different port
python app.py --port 8000
```

### Images not loading
1. Check if images are in `static/images/` folder
2. Verify filenames match HTML references
3. Check browser console for 404 errors

### CSS/JS not updating
```bash
# Clear browser cache
# Or use Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
```

### Module not found error
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [CSS Tricks](https://css-tricks.com/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## 💡 Tips & Best Practices

1. **Always use virtual environment** to avoid dependency conflicts
2. **Keep images optimized** - use PNG or WebP format
3. **Test on mobile** - use browser DevTools responsive mode
4. **Use HTTPS in production** - get free SSL from Let's Encrypt
5. **Monitor performance** - use Google PageSpeed Insights
6. **Keep dependencies updated** - run `pip install --upgrade -r requirements.txt`

---

## 📞 Support

For issues:
1. Check the README.md file
2. Review the main Flask documentation
3. Check browser console for errors (F12)
4. Search Stack Overflow for common issues

---

**Happy coding! 🎉**

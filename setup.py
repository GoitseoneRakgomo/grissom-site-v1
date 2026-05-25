#!/usr/bin/env python3
"""
Grissom Flask App - Setup Script
Helps with initial setup and configuration
"""

import os
import subprocess
import sys
import platform
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def print_section(text):
    """Print a section header"""
    print(f"\n➜ {text}\n")


def check_python_version():
    """Check if Python version is 3.8+"""
    print_section("Checking Python version")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python 3.8+ required (you have {version.major}.{version.minor})")
        return False


def check_pip():
    """Check if pip is installed"""
    print_section("Checking pip")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()}")
            return True
    except Exception as e:
        print(f"❌ pip not found: {e}")
        return False


def create_virtual_env():
    """Create virtual environment"""
    print_section("Creating virtual environment")
    venv_path = "venv"
    
    if os.path.exists(venv_path):
        print(f"ℹ️  Virtual environment already exists at '{venv_path}'")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        print(f"✅ Virtual environment created at '{venv_path}'")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False


def activate_virtual_env():
    """Get activation command for virtual environment"""
    if platform.system() == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"


def install_dependencies():
    """Install Python dependencies"""
    print_section("Installing dependencies")
    
    pip_executable = "venv\\Scripts\\pip" if platform.system() == "Windows" else "venv/bin/pip"
    
    try:
        # Check if pip executable exists
        if not os.path.exists(pip_executable):
            print("⚠️  Virtual environment not yet activated")
            print("Please run the activation command first:")
            print(f"    {activate_virtual_env()}")
            return False
        
        print("Installing packages from requirements.txt...")
        subprocess.run([pip_executable, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def check_directories():
    """Check if required directories exist"""
    print_section("Checking project structure")
    
    required_dirs = [
        "static",
        "static/css",
        "static/js",
        "static/images",
        "static/logos",
        "templates"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ {dir_path}")
        else:
            print(f"❌ {dir_path} (missing)")
            all_exist = False
    
    return all_exist


def check_files():
    """Check if required files exist"""
    print_section("Checking required files")
    
    required_files = [
        "app.py",
        "config.py",
        "utils.py",
        "static/css/style.css",
        "static/js/main.js",
        "templates/index.html",
        "requirements.txt"
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (missing)")
            all_exist = False
    
    return all_exist


def check_images():
    """Check if required images exist"""
    print_section("Checking image files")
    
    required_images = [
        "static/images/hero-left.jpg",
        "static/images/what-we-do.jpg",
        "static/images/approach.jpg"
    ]
    
    for img_path in required_images:
        if os.path.exists(img_path):
            size = os.path.getsize(img_path) / 1024  # Size in KB
            print(f"✅ {img_path} ({size:.1f} KB)")
        else:
            print(f"⚠️  {img_path} (not found - please add)")


def show_next_steps():
    """Show next steps"""
    print_header("SETUP COMPLETE!")
    
    print("📋 Next Steps:\n")
    
    print("1. Activate virtual environment:")
    print(f"   {activate_virtual_env()}\n")
    
    print("2. Add your images to static/images/:")
    print("   - hero-left.jpg")
    print("   - what-we-do.jpg")
    print("   - approach.jpg\n")
    
    print("3. Update your company information:")
    print("   - Edit templates/index.html for content")
    print("   - Edit static/css/style.css for colors\n")
    
    print("4. Run the application:")
    print("   python app.py\n")
    
    print("5. Open your browser:")
    print("   http://localhost:5000\n")


def main():
    """Run setup"""
    print_header("GRISSOM FLASK APP - SETUP WIZARD")
    
    # Check Python
    if not check_python_version():
        print("❌ Setup aborted: Python 3.8+ required")
        sys.exit(1)
    
    # Check pip
    if not check_pip():
        print("⚠️  pip check passed with warnings")
    
    # Create venv
    if not create_virtual_env():
        print("⚠️  Virtual environment creation may have issues")
    
    # Check structure
    check_directories()
    check_files()
    check_images()
    
    print_section("Installation Instructions")
    print("To complete the setup, please run:\n")
    
    activation_cmd = activate_virtual_env()
    pip_install = "pip install -r requirements.txt"
    
    if platform.system() == "Windows":
        print(f"  {activation_cmd}")
        print(f"  {pip_install}")
        print(f"  python app.py\n")
    else:
        print(f"  {activation_cmd}")
        print(f"  {pip_install}")
        print(f"  python app.py\n")
    
    show_next_steps()
    
    print_header("Documentation")
    print("""
📖 Read these files for more information:
   - QUICKSTART.md     - 5-minute quick start guide
   - README.md         - Complete documentation
   - PROJECT_SUMMARY.md - Project overview
""")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

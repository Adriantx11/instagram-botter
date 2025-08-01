#!/usr/bin/env python3
"""
Installation script for Instagram Botter
This script will install the required packages for the Instagram Botter.
"""

import subprocess
import sys
import os

def install_packages():
    """Install required packages"""
    print("Installing packages for Instagram Botter...")
    
    # Set console title if on Windows
    if os.name == 'nt':
        os.system("title Installing packages for Instagram Botter...")
        os.system("color a")  # Set console color to green
    
    try:
        # Install packages from requirements file
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "reqs.txt"])
        print("✅ All packages installed successfully!")
        print("You can now run the main.py file to start the botter.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        print("Please make sure you have pip installed and try again.")
    except FileNotFoundError:
        print("❌ reqs.txt file not found!")
        print("Installing packages manually...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "requests"])
            print("✅ Packages installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing packages: {e}")

if __name__ == "__main__":
    install_packages()
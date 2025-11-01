#!/bin/bash
# Quick setup script for YouTube Playlist Scraper

echo "======================================"
echo "YouTube Playlist Scraper - Setup"
echo "======================================"
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "======================================"
echo "✅ Setup complete!"
echo "======================================"
echo ""
echo "Usage:"
echo "  python3 youtube_scraper.py"
echo ""
echo "Or with URL:"
echo "  python3 youtube_scraper.py 'YOUTUBE_URL'"
echo ""

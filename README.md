# YouTube Playlist Scraper

A robust Python tool to extract video information, transcripts, titles, and descriptions from YouTube videos and playlists.

## Features

- ✅ **Extract from playlists or single videos**
- ✅ **Get video metadata** (title, description, channel, views, duration)
- ✅ **Extract transcripts** (when available)
- ✅ **Export to JSON and Markdown** formats
- ✅ **Actively maintained libraries** (yt-dlp + youtube-transcript-api)
- ✅ **Proper error handling** for missing transcripts
- ✅ **Progress indicators** for playlist processing

## Why This Tool?

This scraper uses **yt-dlp** (actively maintained, 2025-ready) instead of the outdated `pytube` library. Based on research:

- ✅ `yt-dlp` is the gold standard for YouTube extraction
- ✅ Regular updates keep pace with YouTube changes
- ✅ Faster downloads and improved format selection
- ✅ Active community and quick bug fixes

## Installation

### Requirements

- Python 3.10 or higher (Python 3.9 may work but is deprecated)
- pip (Python package manager)

### Setup

1. **Clone or download this repository**

```bash
cd ~/Developer/rona354/youtube-playlist-scraper
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install yt-dlp youtube-transcript-api
```

## Usage

### Basic Usage

Run the scraper interactively:

```bash
python3 youtube_scraper.py
```

Then enter a YouTube URL when prompted.

### Command Line Usage

Pass the URL as an argument:

```bash
python3 youtube_scraper.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or for a playlist:

```bash
python3 youtube_scraper.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

### Output

The script creates an `output/` directory with two files:

1. **`youtube_data.json`** - Complete raw data in JSON format
   - Video IDs, URLs, metadata
   - Full transcripts with timestamps
   - Channel information

2. **`youtube_data.md`** - Human-readable summary in Markdown
   - Formatted video information
   - Transcripts in readable format
   - Easy to share or import into other tools

## Example

```bash
$ python3 youtube_scraper.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

============================================================
YouTube Playlist Scraper
Using yt-dlp + youtube-transcript-api
============================================================

============================================================
Fetching information from: https://www.youtube.com/watch?v=dQw4w9WgXcQ
============================================================

Detected single video

Processing: Rick Astley - Never Gonna Give You Up (Official Video)
   ⚠ Transcript not available for video dQw4w9WgXcQ

✓ JSON saved to: output/youtube_data.json
✓ Markdown saved to: output/youtube_data.md

============================================================
✅ Successfully processed 1 video(s)
============================================================
```

## Troubleshooting

### Transcript Not Available

Some videos don't have transcripts (auto-generated or manual). The scraper will:
- Extract all other metadata successfully
- Mark transcript as unavailable
- Continue processing other videos in the playlist

### Python Version Warning

If you see "Deprecated Feature: Support for Python version 3.9", consider upgrading:

```bash
# Check your Python version
python3 --version

# Install Python 3.10+ from python.org or use pyenv
```

### SSL/OpenSSL Warning

If you see urllib3 warnings about OpenSSL, this doesn't affect functionality. To fix:

```bash
pip install --upgrade urllib3
```

## API Details

### Libraries Used

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Video metadata extraction
  - Active maintenance, YouTube-change resilient
  - No API key required
  - Fast and reliable

- **[youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)** - Transcript extraction
  - Works with auto-generated subtitles
  - No API key required
  - Supports multiple languages

### No API Keys Required

Both libraries work without YouTube API keys, making this tool easy to use without quota limits.

## Project Structure

```
youtube-playlist-scraper/
├── youtube_scraper.py    # Main scraper script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
└── output/              # Generated output files (created automatically)
    ├── youtube_data.json
    └── youtube_data.md
```

## Contributing

Feel free to open issues or submit pull requests for improvements!

## License

MIT License - Feel free to use and modify as needed.

## Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Transcripts via [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- Research confirmed these are the most reliable tools for 2025

---

**Note:** This tool is for personal and educational use. Respect YouTube's Terms of Service and copyright laws.

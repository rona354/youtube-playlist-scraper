# Example Output

This file shows what the scraper outputs look like.

## Command

```bash
python3 youtube_scraper.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Console Output

```
============================================================
YouTube Playlist Scraper
Using yt-dlp + youtube-transcript-api
============================================================

============================================================
Fetching information from: https://www.youtube.com/watch?v=dQw4w9WgXcQ
============================================================

Detected single video

Processing: Rick Astley - Never Gonna Give You Up (Official Video)

✓ JSON saved to: output/youtube_data.json
✓ Markdown saved to: output/youtube_data.md

============================================================
✅ Successfully processed 1 video(s)
============================================================
```

## JSON Output Structure

```json
[
  {
    "id": "dQw4w9WgXcQ",
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Video)",
    "description": "The official video for \"Never Gonna Give You Up\"...",
    "channel": "Rick Astley",
    "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "duration": 213,
    "view_count": 1708495999,
    "upload_date": "20091025",
    "transcript": [
      {
        "text": "[Music]",
        "start": 0.0,
        "duration": 2.5
      },
      {
        "text": "We're no strangers to love",
        "start": 2.5,
        "duration": 3.0
      }
    ],
    "transcript_available": true
  }
]
```

## Markdown Output Preview

```markdown
# YouTube Videos Summary

Total videos: 1

---

## 1. Rick Astley - Never Gonna Give You Up (Official Video)

**Channel:** Rick Astley

**URL:** https://www.youtube.com/watch?v=dQw4w9WgXcQ

**Duration:** 213 seconds

**Views:** 1,708,495,999

**Description:**

The official video for "Never Gonna Give You Up" by Rick Astley...

**Transcript:** (61 segments)

\`\`\`
[Music]
We're no strangers to love
You know the rules and so do I
...
\`\`\`

---
```

## Playlist Example

For a playlist URL, you'll see progress for each video:

```
Detected playlist: My Favorite Videos
Total videos: 10

[1/10] Processing: Video Title 1
[2/10] Processing: Video Title 2
...
```

Each video will be processed and included in the output files.

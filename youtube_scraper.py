#!/usr/bin/env python3
"""
YouTube Playlist Scraper
Extract titles, descriptions, and transcripts from YouTube videos and playlists
Using yt-dlp (actively maintained) and youtube-transcript-api
"""

import json
import sys
from typing import List, Dict, Optional
from pathlib import Path

try:
    import yt_dlp
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError as e:
    print(f"Error: Required libraries not installed.")
    print(f"Please run: pip install -r requirements.txt")
    sys.exit(1)


class YouTubeScraper:
    """Scraper for YouTube videos and playlists"""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.transcript_api = YouTubeTranscriptApi()

    def get_video_info(self, url: str) -> Dict:
        """
        Extract metadata from a single video or playlist

        Args:
            url: YouTube video or playlist URL

        Returns:
            Dictionary containing video metadata
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': 'in_playlist',  # Extract playlist info without downloading
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"Error extracting video info: {e}")
            return {}

    def get_transcript(self, video_id: str, languages: List[str] = None) -> Optional[List[Dict]]:
        """
        Get transcript for a video

        Args:
            video_id: YouTube video ID
            languages: List of language codes to try (default: ['en'])

        Returns:
            List of transcript segments or None if unavailable
        """
        if languages is None:
            languages = ['en']

        try:
            transcript = self.transcript_api.fetch(video_id, languages)
            # Convert FetchedTranscriptSnippet objects to dictionaries
            return [
                {
                    'text': segment.text,
                    'start': segment.start,
                    'duration': segment.duration
                }
                for segment in transcript
            ]
        except Exception as e:
            print(f"   ⚠ Transcript not available for video {video_id}: {str(e)[:50]}...")
            return None

    def process_video(self, video_info: Dict) -> Dict:
        """
        Process a single video and extract all relevant information

        Args:
            video_info: Video information from yt-dlp

        Returns:
            Dictionary containing processed video data
        """
        video_id = video_info.get('id', '')
        title = video_info.get('title', 'Unknown')

        print(f"Processing: {title}")

        # Get transcript
        transcript = self.get_transcript(video_id)

        # Build result
        result = {
            'id': video_id,
            'url': f"https://www.youtube.com/watch?v={video_id}",
            'title': title,
            'description': video_info.get('description', ''),
            'channel': video_info.get('uploader', ''),
            'channel_id': video_info.get('channel_id', ''),
            'duration': video_info.get('duration', 0),
            'view_count': video_info.get('view_count', 0),
            'upload_date': video_info.get('upload_date', ''),
            'transcript': transcript,
            'transcript_available': transcript is not None,
        }

        return result

    def scrape(self, url: str) -> List[Dict]:
        """
        Scrape YouTube video or playlist

        Args:
            url: YouTube video or playlist URL

        Returns:
            List of processed video data
        """
        print(f"\n{'='*60}")
        print(f"Fetching information from: {url}")
        print(f"{'='*60}\n")

        info = self.get_video_info(url)
        if not info:
            print("Failed to extract video information")
            return []

        results = []

        # Check if it's a playlist
        if 'entries' in info:
            print(f"Detected playlist: {info.get('title', 'Unknown')}")
            print(f"Total videos: {len(info['entries'])}\n")

            for idx, entry in enumerate(info['entries'], 1):
                if not entry:
                    continue

                print(f"[{idx}/{len(info['entries'])}] ", end='')

                # For flat extraction, we need to get full info
                video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                video_info = self.get_video_info(video_url)

                if video_info:
                    result = self.process_video(video_info)
                    results.append(result)

                print()  # New line after each video

        else:
            # Single video
            print("Detected single video\n")
            result = self.process_video(info)
            results.append(result)

        return results

    def save_results(self, results: List[Dict], prefix: str = "youtube_data"):
        """
        Save results to JSON and Markdown files

        Args:
            results: List of video data
            prefix: Filename prefix
        """
        if not results:
            print("No results to save")
            return

        # Save as JSON
        json_file = self.output_dir / f"{prefix}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n✓ JSON saved to: {json_file}")

        # Save as Markdown
        md_file = self.output_dir / f"{prefix}.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write("# YouTube Videos Summary\n\n")
            f.write(f"Total videos: {len(results)}\n\n")
            f.write("---\n\n")

            for idx, video in enumerate(results, 1):
                f.write(f"## {idx}. {video['title']}\n\n")
                f.write(f"**Channel:** {video['channel']}\n\n")
                f.write(f"**URL:** {video['url']}\n\n")
                f.write(f"**Duration:** {video['duration']} seconds\n\n")
                f.write(f"**Views:** {video['view_count']:,}\n\n")

                if video['description']:
                    f.write(f"**Description:**\n\n{video['description']}\n\n")

                if video['transcript']:
                    f.write(f"**Transcript:** ({len(video['transcript'])} segments)\n\n")
                    f.write("```\n")
                    for segment in video['transcript']:
                        f.write(f"{segment['text']}\n")
                    f.write("```\n\n")
                else:
                    f.write("**Transcript:** Not available\n\n")

                f.write("---\n\n")

        print(f"✓ Markdown saved to: {md_file}")


def main():
    """Main entry point"""
    print("="*60)
    print("YouTube Playlist Scraper")
    print("Using yt-dlp + youtube-transcript-api")
    print("="*60)

    # Get URL from user
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print("\nEnter YouTube URL (video or playlist):")
        url = input("> ").strip()

    if not url:
        print("Error: No URL provided")
        sys.exit(1)

    # Create scraper and process
    scraper = YouTubeScraper()
    results = scraper.scrape(url)

    if results:
        scraper.save_results(results)
        print(f"\n{'='*60}")
        print(f"✅ Successfully processed {len(results)} video(s)")
        print(f"{'='*60}")
    else:
        print("\n❌ No videos were processed")
        sys.exit(1)


if __name__ == "__main__":
    main()

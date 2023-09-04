import os
from pytube import Playlist
from tqdm import tqdm
import argparse

# Function to download a YouTube playlist
def download_playlist(playlist_url, output_directory, quality):
    try:
        playlist = Playlist(playlist_url)
        downloaded_videos = 0  # Initialize a counter for downloaded videos

        for video in tqdm(playlist.videos, desc="Downloading", unit="video"):
            stream = video.streams.filter(res=quality).first()  # Filter by the specified quality
            if stream:
                stream.download(output_path=output_directory)
                downloaded_videos += 1  # Increment the counter

        if downloaded_videos > 0:
            print(f"\n{downloaded_videos} video(s) from the playlist downloaded successfully to {output_directory}")
        else:
            print("\nNo videos matching the specified quality were found in the playlist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Download all videos from a YouTube playlist and save them to a directory.")


    parser.add_argument("playlist_url", help="YouTube playlist URL")

    parser.add_argument("output_directory", help="Output directory to save the videos")

    # Add an argument for the desired video quality
    parser.add_argument("--quality", default="720p", choices=["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"],
                        help="Desired video quality (default: 720p)")

    # Parse the command-line arguments
    args = parser.parse_args()

    download_playlist(args.playlist_url, args.output_directory, args.quality)

    # Notify the user after all videos are downloaded
    print("Download process complete.")

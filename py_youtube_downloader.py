import os
from pytube import YouTube

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def download_video(url, output_path=None):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video = yt.streams.get_highest_resolution()

        # Set the output path
        if output_path is None:
            output_path = get_desktop_path()

        # Download the video
        print(f"Downloading: {yt.title}")
        video.download(output_path)
        print(f"Download complete! Saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("YouTube Video Downloader")
    print("========================")
    print(f"Default save location: {get_desktop_path()}")

    while True:
        url = input("Enter the YouTube video URL (or 'q' to quit): ")
        
        if url.lower() == 'q':
            break

        output_path = input("Enter the output path (press Enter for desktop): ")
        if not output_path:
            output_path = None

        download_video(url, output_path)
        print()

if __name__ == "__main__":
    main()
# Importing necessary libraries
import os
import argparse
from pytube import YouTube, Playlist


# Function to download a video from a given link
def download_video(link, output_path="."):
    yt = YouTube(link)  # Create a YouTube object using the video link
    title = yt.title  # Get the title of the video
    stream = yt.streams.filter(file_extension="mp4", progressive=True).first()  # Filter and get the first mp4 stream
    download_path = os.path.join(output_path, title + ".mp4")  # Create the download path for the video
    stream.download(download_path)  # Download the video to the specified path
    return download_path  # Return the path where the video is downloaded

# Function to download audio from a given link
def download_audio(link, output_path="."):
    yt = YouTube(link)  # Create a YouTube object using the video link
    title = yt.title  # Get the title of the video
    stream = yt.streams.filter(only_audio=True).first()  # Filter and get the first audio stream
    download_path = os.path.join(output_path, title + ".mp3")  # Create the download path for the audio
    stream.download(output_path)  # Download the audio to the specified path
    return download_path  # Return the path where the audio is downloaded

# Function to get top 10 videos from a channel
def get_videos_in_channel(channel_name):
    playlist = Playlist(f"https://www.youtube.com/@{channel_name}/videos")  # Create a Playlist object using the channel name
    return playlist.video_urls[:10]  # Return the URLs of the top 10 videos in the channel

# Function to search and list videos based on a query
def search_and_list_videos(query):
    search_results = YouTube(f"https://www.youtube.com/results?search_query={query}")  # Search for videos based on the query
    videos = search_results.video_urls[:15]  # Get the URLs of the top 15 search results
    return videos  # Return the list of video URLs

# Function to display video information
def display_video_info(video_url):
    yt = YouTube(video_url)  # Create a YouTube object using the video URL
    return f"{yt.title} - {yt.author} - {yt.length} seconds"  # Return the title, author, and length of the video

# Main function to execute the downloader
def main(args):
    if args.action == "download":
        link = args.link
        output_path = args.output
        if args.type == "video":
            result = download_video(link, output_path)
        elif args.type == "audio":
            result = download_audio(link, output_path)
        else:
            result = "Invalid download type. Please choose 'video' or 'audio'."
    elif args.action == "channel":
        channel_name = args.channel
        videos = get_videos_in_channel(channel_name)
        print("Top 10 videos in the channel:")
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {display_video_info(video)}")
    elif args.action == "search":
        search_query = args.query
        videos = search_and_list_videos(search_query)
        print("Top 15 search results:")
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {display_video_info(video)}")
    else:
        result = "Invalid action. Please choose 'download', 'channel', or 'search'."
    print(f"Operation completed. Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    download_parser = subparsers.add_parser("download", help="Download a video or audio")
    download_parser.add_argument("link", help="YouTube video link")
    download_parser.add_argument("type", choices=["video", "audio"], help="Type of download (video/audio)")
    download_parser.add_argument("-o", "--output", default=".", help="Output path (default: current directory)")

    channel_parser = subparsers.add_parser("channel", help="Get top videos from a channel")
    channel_parser.add_argument("channel", help="YouTube channel name")

    search_parser = subparsers.add_parser("search", help="Search videos on YouTube")
    search_parser.add_argument("query", help="Search query")

    args = parser.parse_args()
    main(args)

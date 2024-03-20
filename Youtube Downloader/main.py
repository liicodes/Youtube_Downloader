"""
Author: liicodex
Date: 17.jan.24
"""

# Importing necessary libraries
import os
from pytube import YouTube, Playlist, Channel


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

# Function to get top 10 videos from a channel (incomplete)
"""
def get_videos_in_channel(channel_name):
    playlist = Playlist(f"https://www.youtube.com/@{channel_name}/videos")  # Create a Playlist object using the channel name
    return playlist.video_urls[:10]  # Return the URLs of the top 10 videos in the channel
"""
# Function to search and list videos based on a query
"""
def search_and_list_videos(query):
    search_results = YouTube(f"https://www.youtube.com/results?search_query={query}")  # Search for videos based on the query
    videos = search_results.video_urls[:15]  # Get the URLs of the top 15 search results
    return videos  # Return the list of video URLs
"""
# Function to display video information
"""
def display_video_info(video_url):
    yt = YouTube(video_url)  # Create a YouTube object using the video URL
    return f"{yt.title} - {yt.author} - {yt.length} seconds"  # Return the title, author, and length of the video
"""

# Main function to execute the downloader
def main():
  print("Welcome to my YouTube downloader, call it whatever you want.")
  choice = int(input("Enter \n1. Download by link \n2. Download from channel(incomplete) \n3. Search on YouTube \n>>  "))

  # Downloading by link
  if choice == 1:
      link = input("Enter YouTube video link: ")  # Prompt user to enter a YouTube video link
      download_type = input("Enter 'video' or 'audio': ")  # Prompt user to choose download type
      if download_type.lower() == "video":  # If user chose to download video
          result = download_video(link)  # Call download_video function with the provided link
      elif download_type.lower() == "audio":  # If user chose to download audio
          result = download_audio(link)  # Call download_audio function with the provided link
      else:
        result = "Invalid download type. Please choose 'video' or 'audio'."  # Error message for invalid download type
    
  # Check if the length of choice is greater than 1
  elif len(str(choice)) > 1:
    print("Invalid input. Please enter a valid choice.")
  
  # Downloading from a channel
  elif choice == 2:
    channel_name = input("Enter YouTube channel name, without spaces: ")  # Prompt user to enter a YouTube channel name
    videos = get_videos_in_channel(channel_name)  # Get top 10 videos from the specified channel
    print("Top 10 videos in the channel:")
    
    for i, video in enumerate(videos, start=1):  # Iterate through the top 10 videos
      print(f"{i}. {display_video_info(video)}")  # Display video information for each video
      
    video_choice = int(input("Enter the number of the video you want to download: "))  # Prompt user to choose a video to download
    link = videos[video_choice - 1]  # Get the URL of the selected video
    download_type = input("Enter 'video' or 'audio': ")  # Prompt user to choose download type
    if download_type.lower() == "video":  # If user chose to download video
      result = download_video(link)  # Call download_video function with the selected video link
    elif download_type.lower() == "audio":  # If user chose to download audio
      result = download_audio(link)  # Call download_audio function with the selected video link
    else:
      result = "Invalid download type. Please choose 'video' or 'audio'."  # Error message for invalid download type

  # Searching on YouTube
  elif choice == 3:
    search_query = input("Enter text to search on YouTube: ")  # Prompt user to enter a search query
    videos = search_and_list_videos(search_query)  # Search and list top 15 videos based on the query
    print("Top 15 search results:") # To return top 15 results
    for i, video in enumerate(videos, start=1):  # Iterate through the top 15 search results
      print(f"{i}. {display_video_info(video)}")  # Display video information for each search result
    video_choice = int(input("Enter the number of the video you want to download: "))  # Prompt user to choose a video to download
    link = videos[video_choice - 1]  # Get the URL of the selected video
    download_type = input("Enter 'video' or 'audio': ")  # Prompt user to choose download type
    if download_type.lower() == "video":  # If user chose to download video
      result = download_video(link)  # Call download_video function with the selected video link
    elif download_type.lower() == "audio":  # If user chose to download audio
      result = download_audio(link)  # Call download_audio function with the selected video link
    else:
      result = "Invalid download type. Please choose 'video' or 'audio'."  # Error message for invalid download type
    
  else:
    result = "Invalid choice. Please enter 1, 2, or 3."  # Error message for invalid choice
  print(f"Downloaded successfully. File saved at: {result}")  # Print the download result
  
if __name__ == "__main__":
  main()  # Call the main function if the script is run as a standalone program

import os
from pytube import YouTube, Playlist, Channel



""" MAKE THE FUNCTIONS"""



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

# 🎥 YouTube Downloader 📥

This Python script allows you to download videos or audio from YouTube, get top videos from a specific channel, or search for videos based on a query.

## Usage

1. **Download a Video/Audio**:
   ```
   python youtube_downloader.py download <video_link> <type> [-o <output_path>]
   ```

   - `<video_link>`: YouTube video link.
   - `<type>`: Type of download, choose either `video` or `audio`.
   - `-o, --output`: (Optional) Output path to save the downloaded file. Default is the current directory.

2. **Get Top Videos from a Channel**:
   ```
   python youtube_downloader.py channel <channel_name>
   ```

   - `<channel_name>`: YouTube channel name.

3. **Search Videos on YouTube**:
   ```
   python youtube_downloader.py search <query>
   ```

   - `<query>`: Search query.

## Requirements

- Python 3.x
- PyTube library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/....
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Example

1. Download a video:
   ```
   python youtube_downloader.py download https://www.youtube.com/watch?v=video_link video -o /path/to/save
   ```

2. Get top videos from a channel:
   ```
   python youtube_downloader.py channel channel_name
   ```

3. Search for videos on YouTube:
   ```
   python youtube_downloader.py search "search_query"
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the README according to your specific project structure and requirements. 🚀

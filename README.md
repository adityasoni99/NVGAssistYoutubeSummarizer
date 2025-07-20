# YouTube Video Summarizer - G-Assist Plugin

<div align="center">

![G-Assist](https://img.shields.io/badge/NVIDIA-G--Assist-76B900?style=for-the-badge&logo=nvidia)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![AI](https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

**🏆 NVIDIA G-Assist Hackathon 2025 Submission**

*Revolutionize your video consumption with AI-powered YouTube summaries directly from G-Assist*

</div>

---

## 🎯 Project Overview

**YouTube Video Summarizer** is an innovative G-Assist plugin that transforms how you consume YouTube content. Instead of watching entire videos, simply ask G-Assist to summarize any YouTube video and get instant, AI-powered insights powered by Google Gemini.

### 🌟 Key Features

- **📝 Smart Summaries**: Generate concise, intelligent summaries of any YouTube video
- **🔍 Key Points Extraction**: Automatically identify and extract main topics with timestamps
- **💡 Actionable Insights**: Get practical takeaways and recommendations from video content
- **⚡ Instant Access**: Works directly from G-Assist overlay - no need to leave your current application
- **🔒 Privacy-First**: Processes video transcripts securely using Google Gemini API
- **🎮 Gaming-Friendly**: Perfect for summarizing tutorials, reviews, and guides while gaming

### 🎪 Demo Functions

1. **`summarize_video`** - Creates comprehensive video summaries
2. **`extract_keypoints`** - Identifies key topics with timestamps
3. **`get_insights`** - Provides actionable recommendations

---

## 🚀 Installation & Setup

### Prerequisites

- **GeForce RTX GPU**: RTX 30, 40, or 50 Series with 12GB+ VRAM
- **Windows**: Windows 10 or 11
- **NVIDIA App**: Latest version with G-Assist enabled
- **Python Dependencies**: See `requirements.txt`

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/adityasoni99/NVGAssistYoutubeSummarizer.git
   cd NVGAssistYoutubeSummarizer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Google Gemini API**
   - Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey)
   - Update `config.json` with your API key:
   ```json
   {
     "gemini_api_key": "YOUR_API_KEY_HERE",
     "gemini_model": "gemini-1.5-flash",
     "output_format": "json"
   }
   ```

4. **Build the Plugin**
   ```bash
   # Run the build script
   build.bat
   ```

5. **Install in G-Assist**
   - Copy the entire plugin folder to your G-Assist plugins directory
   - Restart G-Assist from NVIDIA App

---

## 🎮 Usage Examples

### Voice Commands

- *"Summarize this YouTube video: https://youtube.com/watch?v=xyz"*
- *"Extract key points from this tutorial video"*
- *"What insights can I get from this video?"*

### Text Commands

Simply type the same commands in the G-Assist interface!

### Sample Workflow

1. **Gaming Setup**: You're playing your favorite game
2. **Quick Learning**: Press `Alt+G` to open G-Assist
3. **Smart Summary**: Ask to summarize a YouTube tutorial
4. **Instant Knowledge**: Get key insights without leaving your game

---

## 🔧 Technical Architecture

### Core Components

- **`plugin.py`**: Main plugin logic and G-Assist integration
- **`manifest.json`**: Plugin configuration and function definitions  
- **`config.json`**: API configuration and settings
- **`requirements.txt`**: Python dependencies
- **`build.bat`**: Build automation script
- **`yt.spec`**: PyInstaller specification

### AI Integration

- **YouTube Transcript API**: Extracts video transcripts automatically
- **Google Gemini 1.5 Flash**: Powers intelligent summarization
- **G-Assist Framework**: Seamless integration with NVIDIA's AI assistant

### Data Flow

```
YouTube URL → Transcript Extraction → Gemini Processing → G-Assist Response
```

---

## 🛠️ Development

### Building from Source

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller yt.spec

# Output: dist/youtube_summarizer_plugin.exe
```

### Testing

```bash
# Test the plugin directly
python plugin.py test

# Or use the test script
python test_youtube_plugin.py
```

**Note**: Testing requires Windows environment with G-Assist installed, as the plugin uses Windows-specific APIs for G-Assist communication.

### Plugin Structure

```
youtube-summarizer/
├── plugin.py              # Main plugin logic
├── manifest.json          # G-Assist function definitions
├── config.json           # Configuration file
├── requirements.txt       # Dependencies
├── build.bat             # Build script
├── yt.spec              # PyInstaller config
├── test_youtube_plugin.py # Test script
└── dist/
    └── youtube_summarizer_plugin.exe
```

---

## 🎯 Hackathon Innovation

### 🚀 Innovation & Creativity

- **First-of-its-kind** YouTube integration for G-Assist
- **Multi-modal AI approach** combining transcript analysis with large language models
- **Seamless gaming integration** - learn while you play
- **Voice-first design** for hands-free operation

### 🔧 Technical Excellence

- **Robust error handling** for various YouTube video types
- **Efficient transcript processing** with caching capabilities
- **Modular architecture** for easy extension
- **Production-ready executable** with PyInstaller

### 👥 Community Impact

- **Educational enhancement** - Learn faster from video content
- **Gaming productivity** - Get tutorial insights without interrupting gameplay
- **Content discovery** - Quickly evaluate video quality before watching
- **Accessibility** - Voice commands make content more accessible

---

## 📋 Submission Checklist

### ✅ Required Files

- [x] **Source Code**: `plugin.py`
- [x] **Dependencies**: `requirements.txt` 
- [x] **Configuration**: `manifest.json`
- [x] **Settings**: `config.json`
- [x] **Executable**: `dist/youtube_summarizer_plugin.exe`
- [x] **Documentation**: `README.md`

### 🎥 Video Demo

[![Watch the video](https://img.youtube.com/vi/4_O6T6CUsTs/maxresdefault.jpg)](https://www.youtube.com/watch?v=4_O6T6CUsTs)

- [x] **Demo Video**: 30 seconds - 2 minutes showcasing plugin functionality
- [ ] **Social Media**: Post with #AIonRTXHackathon hashtag

### 🏆 Judging Criteria Alignment

1. **Innovation**: Novel YouTube + G-Assist integration
2. **Technical Execution**: Production-ready plugin with comprehensive error handling
3. **Usability**: Voice-first, gaming-friendly design with immediate practical value

---

## 🔑 API Setup Guide

### Google Gemini API

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to `config.json`

**Note**: Free tier includes generous usage limits perfect for testing and demonstration.

---

## 🚨 Troubleshooting

### Common Issues

**Plugin not loading?**
- Verify G-Assist is updated to latest version
- Check Windows firewall settings
- Ensure all dependencies are installed

**API errors?**
- Verify Gemini API key is valid
- Check internet connection
- Confirm video URL is accessible

**Build failures?**
- Install latest PyInstaller: `pip install --upgrade pyinstaller`
- Check Python version compatibility (3.8+)

---

## 🤝 Contributing

We welcome contributions! Areas for enhancement:

- Additional AI model support (OpenAI, Claude, etc.)
- Playlist summarization
- Multi-language support
- Advanced caching mechanisms

---

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **NVIDIA** - For the incredible G-Assist platform and hackathon opportunity
- **Google** - For the powerful Gemini API
- **YouTube** - For transcript accessibility through their platform
- **Open Source Community** - For the amazing libraries that made this possible

---

<div align="center">

**Built with ❤️ for the NVIDIA G-Assist Hackathon 2025**

*Empowering gamers and creators with AI-powered video intelligence*

</div> 

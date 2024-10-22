# Real-Time Language Translator

A real-time language translation desktop application developed for Smart India Hackathon, powered by IBM Watson Language Translator and Text-to-Speech APIs. Built entirely in Python using CustomTkinter for a modern, customizable GUI.

## 🌟 Features

- Real-time translation between multiple Indian languages and international languages
- Text-to-speech functionality for translated content
- Modern and customizable GUI built with CustomTkinter
- Support for both text and voice input
- Dark/Light mode support
- Cross-platform compatibility (Windows, macOS, Linux)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- IBM Cloud account
- IBM Watson API credentials
- Internet connection for real-time translation

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/real-time-language-translator.git
cd real-time-language-translator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `config.py` file in the root directory and add your IBM Watson credentials:
```python
WATSON_API_KEY = "your_api_key_here"
WATSON_URL = "your_service_url_here"
WATSON_TTS_API_KEY = "your_tts_api_key_here"
WATSON_TTS_URL = "your_tts_service_url_here"
```

5. Run the application:
```bash
python main.py
```

## 📦 Dependencies

- customtkinter
- ibm-watson
- python-dotenv
- requests
- pyaudio
- pygame (for audio playback)
- pillow (for image processing)

## 🔧 Configuration

### Supported Languages
- Hindi
- Bengali
- Tamil
- Telugu
- Marathi
- Gujarati
- English
- And many more...

### API Rate Limits
- Basic tier: 1000 requests/day
- Premium tier: Unlimited requests

## 💡 Usage

1. Launch the application
2. Select source and target languages from the dropdown menus
3. Enter text in the source language text box
4. Click the translate button or use the auto-translate feature
5. Use the speaker icon to listen to the translation
6. Switch between light and dark modes using the theme toggle



## 🎨 GUI Features

- Modern and sleek interface using CustomTkinter
- Responsive design that adapts to window resizing
- Custom-styled buttons and input fields
- Smooth animations and transitions
- System-native look and feel
- Dark/Light mode support

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Smart India Hackathon

This project was developed as part of Smart India Hackathon, addressing the challenge of language barriers in India. Our solution aims to facilitate better communication across different linguistic regions of India.


## 🙏 Acknowledgments

- IBM Watson for providing the translation and text-to-speech APIs
- CustomTkinter developers for the amazing GUI framework
- Smart India Hackathon organizing team
- Our mentors and guides
- [Add other acknowledgments]

## 📞 Contact

For any queries regarding the project, please reach out to:
- Email: vethanathanvk@gmail.com
- LinkedIn: [Vethanathan V K](https://linkedin.com/in/vethanathanvk)

## 🚨 Support

If you encounter any issues or need assistance, please:
1. Check the [Issues](https://github.com/vethanathanvk/real-time-language-translator/issues) page
2. Create a new issue if your problem isn't already listed
3. Reach out to the team via email

---
Made with ❤️ for Smart India Hackathon

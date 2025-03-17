# Gemini Image Editor

A powerful web-based tool that uses Google's Gemini AI to transform your images with various effects, filters, and creative edits - all through a simple user interface.

![Gemini Image Editor](https://i.imgur.com/example.jpg)

## 🌟 Features

- **Web UI Interface**: Easy-to-use interface with image preview
- **Multiple Editing Styles**: Choose from 10+ pre-defined styles
- **Custom Prompts**: Create your own unique image transformations
- **Real-time Feedback**: See Gemini's explanations of your edits
- **Simple Setup**: Works on Windows, Mac, and Linux

## 📋 Requirements

- Python 3.7 or higher
- Google Gemini API key (get one free at [Google AI Studio](https://aistudio.google.com))
- Internet connection

## 🚀 Installation

### Step 1: Get the code

```bash
git clone https://github.com/yourusername/gemini-image-editor.git
cd gemini-image-editor
```

### Step 2: Set up a virtual environment

#### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install required packages

```bash
pip install google-generativeai pillow python-dotenv gradio
```

### Step 4: Create `.env` file with your API key

Create a file named `.env` in the project root directory containing:
```
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key.

## 🖥️ How to Use

### Starting the Web Interface

```bash
# Ensure your virtual environment is activated
python gemini_webui.py
```

This will start a local web server at `http://localhost:7860`. Open this URL in your browser to access the interface.

### Using the Web Interface

1. **Upload an Image**: Click the image area or drag and drop an image
2. **Choose a Style**: Select from the dropdown menu or pick "none" to use only a custom prompt
3. **Enter a Custom Prompt** (optional): For example, "Add a majestic castle in the background"
4. **Click "Edit Image"**: Wait a few seconds for Gemini to process your image
5. **View Results**: See your edited image and read Gemini's explanation of the changes

## 🎨 Available Editing Styles

| Style | Description |
|-------|-------------|
| none | Custom prompt only |
| cartoon | Transform into cartoon style |
| oil | Oil painting effect |
| sketch | Pencil sketch conversion |
| vintage | Nostalgic vintage filter |
| cyberpunk | Futuristic cyberpunk aesthetic |
| watercolor | Soft watercolor painting look |
| neon | Vibrant neon glow effects |
| add_object | Intelligently adds contextual objects |
| background | Changes background scenery |
| enhance | Improves image quality (default) |

## 💡 Example Prompts for Custom Edits

- "Make it look like a scene from a fantasy movie with magical elements"
- "Add a majestic mountain range in the background"
- "Transform into anime style with vibrant colors"
- "Add northern lights to the sky"
- "Convert to black and white with one colored element"
- "Make it look like it was taken on Mars"
- "Add dramatic stormy weather"
- "Transform into pixel art style"

## 🔧 Troubleshooting

### API Key Issues
- Double-check your API key in the `.env` file
- Ensure you have the free Gemini API tier activated

### Installation Problems
- Make sure you're using Python 3.7+
- Verify all packages are installed with `pip list`
- If gradio installation fails, try: `pip install --upgrade pip` then reinstall

### Image Processing Errors
- Ensure images are in common formats (JPG, PNG)
- Try with smaller images if you encounter timeouts
- Check your internet connection

## 📝 Technical Notes

- Uses the `gemini-2.0-flash-exp-image-generation` model
- Generated images will have a small watermark
- Free tier has usage limitations (check Google AI Studio for details)
- Image quality and creative results vary based on your prompt clarity

## 🔒 Privacy

- Images are processed through Google's Gemini API
- Review Google's privacy policy for more information
- No images are permanently stored by this application

## 📄 License

MIT License

---

*Crafted with ❤️ for creative image enthusiasts*

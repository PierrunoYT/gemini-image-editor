# Gemini Image Editing Tools

This collection of Python scripts enables editing images with the Google Gemini API and Imagen 3. With these tools, you can transform images into various styles, add objects, change backgrounds, and much more - all with the power of AI.

![Example Image Editing](https://i.imgur.com/example.jpg)

## Requirements

1. Python 3.7 or higher
2. A Google Gemini API key (available via [Google AI Studio](https://aistudio.google.com))
3. The following Python packages:
   ```bash
   pip install google-generativeai pillow python-dotenv gradio
   ```

## Setup

1. Clone this repository or download the files

2. Create a `.env` file in the project directory with your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. Make sure you have an input image that you want to edit (e.g. `input_image.jpg`)

## Available Scripts

### 1. gemini_webui.py (Recommended)

Web user interface for easy image editing with predefined or custom prompts. Provides the most user-friendly experience.

```bash
python gemini_webui.py
```

This script:
- Launches a web interface at http://localhost:7860
- Allows uploading images via drag & drop
- Offers a selection of predefined styles
- Enables custom prompts for creative edits
- Shows original image, edited image, and Gemini's response side by side

### 2. gemini_image_editor.py

Simple script for editing an image with a predefined prompt. Ideal for getting started with the command line.

```bash
python gemini_image_editor.py
```

This script:
- Loads an image from the specified path (`input_image.jpg`)
- Transforms it into an oil painting style
- Shows both the original and edited image
- Saves the result as `edited_image.jpg`

### 3. gemini_advanced_image_editor.py

Advanced script with multiple editing options and command-line arguments. Provides maximum flexibility for command-line users.

```bash
# Basic usage
python gemini_advanced_image_editor.py path/to/image.jpg

# With specific style
python gemini_advanced_image_editor.py path/to/image.jpg --style cartoon

# With custom prompt
python gemini_advanced_image_editor.py path/to/image.jpg --custom "Add a dinosaur to the image"

# Show images and save to a specific file
python gemini_advanced_image_editor.py path/to/image.jpg --show --output result.jpg
```

#### Available Styles:

| Style | Description |
|------|-------------|
| none | Custom prompt only |
| cartoon | Cartoon style |
| oil | Oil painting style |
| sketch | Pencil sketch |
| vintage | Vintage filter |
| cyberpunk | Cyberpunk style |
| watercolor | Watercolor painting |
| neon | Neon effects |
| add_object | Adds an object |
| background | Changes the background |
| enhance | Improves image quality (Default) |

### 4. imagen_editor.py (Planned)

Uses the Imagen 3 API for advanced image editing.

```bash
python imagen_editor.py
```

## Technical Details

- **API Model**: The scripts use the `gemini-2.0-flash-exp-image-generation` model
- **Image Formats**: Supports common formats like JPG, PNG, etc. (via PIL/Pillow)
- **Error Handling**: Robust error handling for missing files and API issues

## Notes

- The Imagen 3 API is only available in the paid tier
- Gemini 2.0 Flash Experimental supports image editing in the free tier
- All generated images contain a digital watermark
- The quality of results depends heavily on the clarity of the prompt

## Examples of Editing Prompts

- "Transform this image into a cartoon style"
- "Add a rainbow to the sky"
- "Change the season to winter with snow"
- "Add a dog in the foreground"
- "Make the image look like an old photograph"
- "Transform the scene into a night scene"
- "Add a dramatic sunset"
- "Transform the image into a science fiction movie style"

## Troubleshooting

- **API Key Errors**: Ensure your `.env` file is correctly set up
- **Image Issues**: Check if the input image exists and is in a supported format
- **Model Limitations**: Note that the model may have certain limitations on image size

## License

MIT

---

*Created with ❤️ for image editing enthusiasts*

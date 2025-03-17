# Import necessary packages
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
import gradio as gr
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Google Generative AI Client
client = genai.Client(api_key=api_key)

# Function to edit an image with Gemini
def edit_image(image, prompt):
    """Edits an image based on a prompt using Gemini."""
    try:
        # Debug output showing which prompt is being used
        print(f"Using prompt: {prompt}")
        
        # Ensure the prompt is in English (if not explicitly specified otherwise)
        if not prompt.strip().endswith("."):
            prompt = prompt.strip() + "."
        prompt += " Please respond in English."
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=[prompt, image],
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
            )
        )
        
        # Process results
        result_text = "Gemini Response:\n"
        edited_image = None
        
        # Debug output of the response structure
        print(f"Response type: {type(response)}")
        print(f"Candidates: {len(response.candidates)}")
        
        if len(response.candidates) > 0:
            for part in response.candidates[0].content.parts:
                print(f"Part type: {type(part)}")
                
                if hasattr(part, 'text') and part.text is not None:
                    print(f"Text found: {part.text[:50]}...")
                    result_text += part.text + "\n"
                elif hasattr(part, 'inline_data') and part.inline_data is not None:
                    print("Image found")
                    edited_image = Image.open(BytesIO(part.inline_data.data))
        else:
            result_text = "No response received from Gemini."
            
        if not result_text or result_text == "Gemini Response:\n":
            result_text = "Gemini Response: No text response received, but an image was generated."
            
        return edited_image, result_text
        
    except Exception as e:
        print(f"Error during image editing: {str(e)}")
        return None, f"An error occurred: {str(e)}"

# Predefined editing options
EDIT_OPTIONS = {
    "none": "Use custom prompt only.",
    "cartoon": "Edit this image to look like a cartoon.",
    "oil": "Edit this image to look like an oil painting.",
    "sketch": "Convert this image into a pencil sketch.",
    "vintage": "Apply a vintage filter to this image.",
    "cyberpunk": "Transform this image into a cyberpunk style.",
    "watercolor": "Convert this image into a watercolor painting.",
    "neon": "Add neon effects to this image.",
    "add_object": "Add an interesting object to this image that fits the context well.",
    "background": "Change the background of this image to something more interesting.",
    "enhance": "Improve the quality of this image, make it sharper and more vibrant."
}

# Helper function for the Gradio UI
def process_image(image, style, custom_prompt=""):
    if style == "none" and not custom_prompt:
        return None, "Please enter a custom prompt when selecting the 'none' style."
    
    if custom_prompt:
        prompt = custom_prompt
    else:
        prompt = EDIT_OPTIONS[style]
    
    edited_image, result_text = edit_image(image, prompt)
    return edited_image, result_text

# Create Gradio Web UI
def create_ui():
    with gr.Blocks(title="Gemini Image Editor") as demo:
        gr.Markdown("# Gemini Image Editor")
        gr.Markdown("Edit images with Google Gemini AI")
        
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(type="pil", label="Original Image")
                style_dropdown = gr.Dropdown(
                    choices=list(EDIT_OPTIONS.keys()),
                    value="enhance",
                    label="Editing Style"
                )
                
                custom_prompt = gr.Textbox(
                    label="Custom Prompt (optional)",
                    placeholder="Enter a custom prompt or choose a style from the list above"
                )
                
                # Event handler for dropdown to change textfield placeholder
                def update_prompt_placeholder(style):
                    if style == "none":
                        return {"placeholder": "Please enter a custom prompt", "value": ""}
                    else:
                        return {"placeholder": f"Optional: Override the {style} style with your own prompt"}
                
                style_dropdown.change(
                    fn=update_prompt_placeholder,
                    inputs=style_dropdown,
                    outputs=custom_prompt
                )
                submit_btn = gr.Button("Edit Image")
            
            with gr.Column():
                output_image = gr.Image(type="pil", label="Edited Image")
                output_text = gr.Textbox(
                    label="Gemini Response", 
                    lines=8,
                    show_copy_button=True,
                    interactive=False
                )
        
        # Event handler
        submit_btn.click(
            fn=process_image,
            inputs=[input_image, style_dropdown, custom_prompt],
            outputs=[output_image, output_text]
        )
        
        gr.Markdown("### Available Styles")
        for style, prompt in EDIT_OPTIONS.items():
            gr.Markdown(f"- **{style}**: {prompt}")
    
    return demo

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(share=True)
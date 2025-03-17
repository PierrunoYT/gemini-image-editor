# Notwendige Pakete importieren
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
import gradio as gr
from dotenv import load_dotenv

# API-Key aus .env-Datei laden
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Google Generative AI Client initialisieren
client = genai.Client(api_key=api_key)

# Funktion zum Bearbeiten eines Bildes mit Gemini
def edit_image(image, prompt):
    """Bearbeitet ein Bild basierend auf einem Prompt mit Gemini."""
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=[prompt, image],
        config=types.GenerateContentConfig(
            response_modalities=['Text', 'Image']
        )
    )
    
    # Ergebnisse verarbeiten
    result_text = ""
    edited_image = None
    
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            result_text += part.text + "\n"
        elif part.inline_data is not None:
            edited_image = Image.open(BytesIO(part.inline_data.data))
    
    return edited_image, result_text

# Vordefinierte Bearbeitungsoptionen
EDIT_OPTIONS = {
    "none": "Nur benutzerdefinierten Prompt verwenden.",
    "cartoon": "Bearbeite dieses Bild, um es wie einen Cartoon aussehen zu lassen.",
    "oil": "Bearbeite dieses Bild, um es wie ein Ölgemälde aussehen zu lassen.",
    "sketch": "Wandle dieses Bild in eine Bleistiftskizze um.",
    "vintage": "Wende einen Vintage-Filter auf dieses Bild an.",
    "cyberpunk": "Transformiere dieses Bild in einen Cyberpunk-Stil.",
    "watercolor": "Wandle dieses Bild in ein Aquarellgemälde um.",
    "neon": "Füge diesem Bild Neon-Effekte hinzu.",
    "add_object": "Füge diesem Bild ein interessantes Objekt hinzu, das gut zum Kontext passt.",
    "background": "Ändere den Hintergrund dieses Bildes zu etwas Interessanterem.",
    "enhance": "Verbessere die Qualität dieses Bildes, mache es schärfer und lebendiger."
}

# Hilfsfunktion für die Gradio UI
def process_image(image, style, custom_prompt=""):
    if style == "none" and not custom_prompt:
        return None, "Bitte gib einen benutzerdefinierten Prompt ein, wenn du den Stil 'none' auswählst."
    
    if custom_prompt:
        prompt = custom_prompt
    else:
        prompt = EDIT_OPTIONS[style]
    
    edited_image, result_text = edit_image(image, prompt)
    return edited_image, result_text

# Gradio Web UI erstellen
def create_ui():
    with gr.Blocks(title="Gemini Image Editor") as demo:
        gr.Markdown("# Gemini Image Editor")
        gr.Markdown("Bearbeite Bilder mit Google Gemini AI")
        
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(type="pil", label="Originalbild")
                style_dropdown = gr.Dropdown(
                    choices=list(EDIT_OPTIONS.keys()),
                    value="enhance",
                    label="Bearbeitungsstil"
                )
                
                custom_prompt = gr.Textbox(
                    label="Benutzerdefinierter Prompt (optional)",
                    placeholder="Gib einen benutzerdefinierten Prompt ein oder wähle einen Stil aus der Liste oben"
                )
                
                # Event-Handler für Dropdown, um Textfeld-Placeholder zu ändern
                def update_prompt_placeholder(style):
                    if style == "none":
                        return {"placeholder": "Bitte gib einen benutzerdefinierten Prompt ein", "value": ""}
                    else:
                        return {"placeholder": f"Optional: Überschreibe den {style}-Stil mit deinem eigenen Prompt"}
                
                style_dropdown.change(
                    fn=update_prompt_placeholder,
                    inputs=style_dropdown,
                    outputs=custom_prompt
                )
                submit_btn = gr.Button("Bild bearbeiten")
            
            with gr.Column():
                output_image = gr.Image(type="pil", label="Bearbeitetes Bild")
                output_text = gr.Textbox(label="Gemini Antwort", lines=5)
        
        # Event-Handler
        submit_btn.click(
            fn=process_image,
            inputs=[input_image, style_dropdown, custom_prompt],
            outputs=[output_image, output_text]
        )
        
        gr.Markdown("### Bearbeitungsstile")
        for style, prompt in EDIT_OPTIONS.items():
            gr.Markdown(f"- **{style}**: {prompt}")
    
    return demo

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(share=True)
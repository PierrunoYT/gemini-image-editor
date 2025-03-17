# Gemini Image Editing Tools

Diese Sammlung von Python-Skripten ermöglicht die Bearbeitung von Bildern mit der Google Gemini API und Imagen 3. Mit diesen Tools können Sie Bilder in verschiedene Stile umwandeln, Objekte hinzufügen, Hintergründe ändern und vieles mehr - alles mit der Kraft der KI.

![Beispiel Bildbearbeitung](https://i.imgur.com/example.jpg)

## Voraussetzungen

1. Python 3.7 oder höher
2. Ein Google Gemini API-Schlüssel (erhältlich über [Google AI Studio](https://aistudio.google.com))
3. Die folgenden Python-Pakete:
   ```bash
   pip install google-generativeai pillow python-dotenv gradio
   ```

## Einrichtung

1. Klonen Sie dieses Repository oder laden Sie die Dateien herunter

2. Erstellen Sie eine `.env`-Datei im Projektverzeichnis mit Ihrem API-Schlüssel:
   ```
   GEMINI_API_KEY=Ihr_API_Schlüssel_hier
   ```

3. Stellen Sie sicher, dass Sie ein Eingabebild haben, das Sie bearbeiten möchten (z.B. `input_image.jpg`)

## Verfügbare Skripte

### 1. gemini_webui.py (Empfohlen)

Web-Benutzeroberfläche für die einfache Bearbeitung von Bildern mit vordefiniertem oder benutzerdefiniertem Prompt. Bietet die benutzerfreundlichste Erfahrung.

```bash
python gemini_webui.py
```

Dieses Skript:
- Startet eine Web-Benutzeroberfläche auf http://localhost:7860
- Ermöglicht das Hochladen von Bildern per Drag & Drop
- Bietet eine Auswahl vordefinierter Stile
- Ermöglicht benutzerdefinierte Prompts für kreative Bearbeitungen
- Zeigt Original, bearbeitetes Bild und Gemini-Antwort nebeneinander an

### 2. gemini_image_editor.py

Einfaches Skript zum Bearbeiten eines Bildes mit einem vordefinierten Prompt. Ideal für den Einstieg in die Kommandozeile.

```bash
python gemini_image_editor.py
```

Dieses Skript:
- Lädt ein Bild aus dem angegebenen Pfad (`input_image.jpg`)
- Wandelt es in einen Ölgemälde-Stil um
- Zeigt sowohl das Original als auch das bearbeitete Bild an
- Speichert das Ergebnis als `edited_image.jpg`

### 3. gemini_advanced_image_editor.py

Fortgeschrittenes Skript mit mehreren Bearbeitungsoptionen und Kommandozeilenargumenten. Bietet maximale Flexibilität für Kommandozeilennutzer.

```bash
# Grundlegende Verwendung
python gemini_advanced_image_editor.py pfad/zum/bild.jpg

# Mit spezifischem Stil
python gemini_advanced_image_editor.py pfad/zum/bild.jpg --style cartoon

# Mit benutzerdefiniertem Prompt
python gemini_advanced_image_editor.py pfad/zum/bild.jpg --custom "Füge einen Dinosaurier zum Bild hinzu"

# Bilder anzeigen und in eine bestimmte Datei speichern
python gemini_advanced_image_editor.py pfad/zum/bild.jpg --show --output ergebnis.jpg
```

#### Verfügbare Stile:

| Stil | Beschreibung |
|------|-------------|
| none | Nur benutzerdefinierter Prompt |
| cartoon | Cartoon-Stil |
| oil | Ölgemälde-Stil |
| sketch | Bleistiftskizze |
| vintage | Vintage-Filter |
| cyberpunk | Cyberpunk-Stil |
| watercolor | Aquarellgemälde |
| neon | Neon-Effekte |
| add_object | Fügt ein Objekt hinzu |
| background | Ändert den Hintergrund |
| enhance | Verbessert die Bildqualität (Standard) |

### 4. imagen_editor.py (Geplant)

Verwendet die Imagen 3 API für fortgeschrittene Bildbearbeitung.

```bash
python imagen_editor.py
```

## Technische Details

- **API-Modell**: Die Skripte verwenden das `gemini-2.0-flash-exp-image-generation`-Modell
- **Bildformate**: Unterstützt gängige Formate wie JPG, PNG, etc. (via PIL/Pillow)
- **Fehlerbehandlung**: Robuste Fehlerbehandlung für fehlende Dateien und API-Probleme

## Hinweise

- Die Imagen 3 API ist nur im kostenpflichtigen Tarif verfügbar
- Gemini 2.0 Flash Experimental unterstützt die Bildbearbeitung im kostenlosen Tarif
- Alle generierten Bilder enthalten eine digitale Wassermarke
- Die Qualität der Ergebnisse hängt stark von der Klarheit des Prompts ab

## Beispiele für Bearbeitungsprompts

- "Wandle dieses Bild in einen Cartoon-Stil um"
- "Füge einen Regenbogen zum Himmel hinzu"
- "Ändere die Jahreszeit zu Winter mit Schnee"
- "Füge einen Hund im Vordergrund hinzu"
- "Mache das Bild wie eine alte Fotografie aussehen"
- "Verwandle die Szene in eine Nachtszenerie"
- "Füge einen dramatischen Sonnenuntergang hinzu"
- "Verwandle das Bild in einen Science-Fiction-Film-Stil"

## Fehlerbehebung

- **API-Schlüssel-Fehler**: Stellen Sie sicher, dass Ihre `.env`-Datei korrekt eingerichtet ist
- **Bildprobleme**: Überprüfen Sie, ob das Eingabebild existiert und in einem unterstützten Format vorliegt
- **Modellbeschränkungen**: Beachten Sie, dass das Modell bestimmte Einschränkungen bei der Bildgröße haben kann

## Lizenz

MIT

---

*Erstellt mit ❤️ für Bildbearbeitungs-Enthusiasten*

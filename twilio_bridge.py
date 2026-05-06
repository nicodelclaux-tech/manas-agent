
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Directory configuration
BASE_DIR = "/root/manas-agent"
MEDIA_DIR = os.path.join(BASE_DIR, "media")
DOSSIER_DIR = os.path.join(BASE_DIR, "dossiers")

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg_body = request.form.get('Body', '').strip()
    num_media = int(request.form.get('NumMedia', 0))
    sender = request.form.get('From')
    
    response = MessagingResponse()
    
    if num_media > 0:
        media_url = request.form.get('MediaUrl0')
        content_type = request.form.get('MediaContentType0')
        
        # Save Incoming
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"incoming_{timestamp}.jpg"
        save_path = os.path.join(MEDIA_DIR, "incoming", filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        r = requests.get(media_url)
        with open(save_path, 'wb') as f:
            f.write(r.content)
            
        response.message(f"Snapshot received! I'm identifying this horse and filing it in the Manas Archive. (Ref: {timestamp})")
    
    elif msg_body.lower().startswith("who is"):
        horse_query = msg_body.lower().replace("who is", "").strip().replace(" ", "_")
        dossier_path = os.path.join(DOSSIER_DIR, f"{horse_query}.md")
        
        if os.path.exists(dossier_path):
            with open(dossier_path, 'r') as f:
                content = f.read()
            response.message(f"Here is what I have on {horse_query.replace('_', ' ').title()}:\n\n{content[:500]}...")
        else:
            response.message(f"I don't have a dossier for '{horse_query}' yet. Should I create one?")
            
    else:
        # Default AI-like response for chat
        response.message("Hello! I am your Equine Assistant. You can send me horse photos to file them, or ask me 'Who is [Horse Name]' to see their dossier.")
        
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)

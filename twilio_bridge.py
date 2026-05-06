
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Directory configuration (Absolute paths)
BASE_DIR = "/root/manas-agent"
MEDIA_DIR = os.path.join(BASE_DIR, "media")

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg = request.form.get('Body', '').lower()
    num_media = int(request.form.get('NumMedia', 0))
    sender = request.form.get('From')
    
    response = MessagingResponse()
    
    if num_media > 0:
        # Get image URL from Twilio
        media_url = request.form.get('MediaUrl0')
        content_type = request.form.get('MediaContentType0')
        
        # In a real scenario, we'd trigger the vision identification here
        # For now, we save to an 'incoming' folder for the agent to process
        ext = ".jpg" if "image" in content_type else ".bin"
        filename = f"incoming_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
        save_path = os.path.join(MEDIA_DIR, "incoming", filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Download the file
        r = requests.get(media_url)
        with open(save_path, 'wb') as f:
            f.write(r.content)
            
        response.message(f"Thank you! I've received the photo and I am filing it under the correct horse now. (Ref: {filename})")
    else:
        response.message("Hello! If you send me a photo of a horse, I will identify it and update the dossier.")
        
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)

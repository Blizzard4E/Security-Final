from io import BytesIO
import logging 
import os
import uuid
from dotenv import load_dotenv 
import cv2
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS 
import numpy as np 
from cloudinary.uploader import upload

from security_utils import decrypt_text, encrypt_decrypt_audio, encrypt_decrypt_image, encrypt_decrypt_video, encrypt_text
 
# Load environment variables from the .env file
load_dotenv()
app = Flask(__name__)
CORS(app, origins="*")
app.config['encrypted_image_folder'] = "images/encrypted"
app.config['decrypted_image_folder'] = "images/decrypted"
app.config['encrypted_video_folder'] = "videos/encrypted"
app.config['decrypted_video_folder'] = "videos/decrypted"
app.config['encrypted_audio_folder'] = "audios/encrypted"
app.config['decrypted_audio_folder'] = "audios/decrypted"
@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/text', methods=['POST'])
def encrypt_text_route():
    print(request.get_data()) 
    # Check if request has JSON data
    if not request.is_json:
        return jsonify(error='Invalid JSON data'), 400

    # Get the 'original_text' from the request JSON
    data = request.get_json()
    original_text = data.get('original_text')
    key = data.get('key') 

    # Check if 'original_text' is provided
    if not original_text:
        return jsonify(error='Missing original_text'), 400

    # Call the encrypt_text function
    encrypted_text = encrypt_text(key, original_text) 
    decrypted_text = decrypt_text(key, encrypted_text) 
    # Return the encrypted text
    return jsonify(encrypted_text=encrypted_text, decrypted_text=decrypted_text)  

@app.route('/image', methods=['POST'])
def image_func():
    key = request.form.get('key') 
    # Check if the request has a file part
    if 'original_image' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['original_image']

    # Check if the file is not empty
    if file.filename == '':
        return jsonify(error='No selected file'), 400  

    # Save the uploaded image temporarily
    temp_filename = 'temp_original_image.png'
    file.save(temp_filename)

    # Read the image using OpenCV
    original_image = cv2.imread(temp_filename)
    
    encrypted_image, decrypted_image = encrypt_decrypt_image(key, original_image)
    encrypted_image_path = "images/encrypted/image_" + str(uuid.uuid4()) + ".png"
    decrypted_image_path = "images/decrypted/image_" + str(uuid.uuid4()) + ".png"

    cv2.imwrite(encrypted_image_path, encrypted_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite(decrypted_image_path, decrypted_image)
    print("Images saved successfully")
    
    # Clean up temporary files
    os.remove(temp_filename)
    return jsonify(encrypted_image_url=encrypted_image_path, decrypted_image_url=decrypted_image_path), 200

@app.route('/images/encrypted/<filename>')
def encrypted_image_display(filename):
    return send_from_directory(app.config['encrypted_image_folder'], filename)

@app.route('/images/decrypted/<filename>')
def decrypted_image_display(filename):
    return send_from_directory(app.config['decrypted_image_folder'], filename)

@app.route('/video', methods=['POST'])
def video_func():
    key = request.form.get('key') 
    # Check if the request has a file part
    if 'original_video' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['original_video']

    # Check if the file is not empty
    if file.filename == '':
        return jsonify(error='No selected file'), 400  

    # Save the uploaded video temporarily
    temp_filename = 'temp_original_video.mp4'
    file.save(temp_filename)

    encrypted_video_path, decrypted_video_path = encrypt_decrypt_video(key, temp_filename)
    # Clean up temporary files
    os.remove(temp_filename)
    return jsonify(encrypted_video_url=encrypted_video_path, decrypted_video_url=decrypted_video_path), 200

@app.route('/videos/encrypted/<filename>')
def encrypted_video_display(filename):
    return send_from_directory(app.config['encrypted_video_folder'], filename)

@app.route('/videos/decrypted/<filename>')
def decrypted_video_display(filename):
    return send_from_directory(app.config['decrypted_video_folder'], filename)

@app.route('/audio', methods=['POST'])
def audio_func():
    key = request.form.get('key') 
    # Check if the request has a file part
    if 'original_audio' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['original_audio']

    # Check if the file is not empty
    if file.filename == '':
        return jsonify(error='No selected file'), 400  

    # Save the uploaded audio temporarily
    temp_filename = 'temp_original_audio.wav'
    file.save(temp_filename)

    encrypted_audio_path, decrypted_audio_path = encrypt_decrypt_audio(key, temp_filename)
    # Clean up temporary files
    os.remove(temp_filename)
    return jsonify(encrypted_audio_url=encrypted_audio_path, decrypted_audio_url=decrypted_audio_path), 200

@app.route('/audios/encrypted/<filename>')
def encrypted_audio_display(filename):
    return send_from_directory(app.config['encrypted_audio_folder'], filename)

@app.route('/audios/decrypted/<filename>')
def decrypted_audio_display(filename):
    return send_from_directory(app.config['decrypted_audio_folder'], filename)


if __name__ == '__main__':
    app.run(debug=True)

import math 
import uuid 
import cv2 
import soundfile as sf
from numba import jit
from numba import cfunc, float64

c1_value = -0.3
c2_value = 0.3
y1_value = 0.492
y2_value = -0.133
key = "asdbgffdmsestuiu" 
 
def key_func(key):
    y_array = []
    temp = 0
    temp = ord(key[0]) + c1_value * y1_value + c2_value * y2_value 
    y_array.append(f(temp)) 
 
    temp = ord(key[1]) + c1_value * y_array[0] + c2_value * y1_value 
    y_array.append(f(temp)) 
 
    for i in range(2, 16): 
        temp = ord(key[i]) + c1_value * y_array[i - 1] + c2_value * y_array[i - 2] 
        y_array.append(f(temp)) 
 
    for i in range(16): 
        if i == 14: 
            print("c1Prime: " + str(y_array[i])) 
        elif i == 15: 
            print("c2Prime: " + str(y_array[i])) 
        else: 
            print(str(y_array[i])) 
    c1Prime = y_array[14] 
    c2Prime = y_array[15] 
    return c1Prime, c2Prime


def f(x: float) -> float:
    return math.fmod(x+1, 2.0) - 1


def normalized(value): 
    return value / 256.0

def denormalized(value):
    rounded_value = np.round(value * 256.0) 
    return np.uint8(rounded_value)

def encrypt_value(value, y1, y2, c1Prime, c2Prime):
    return f(value + c1Prime * y1 + c2Prime * y2)

def decrypt_value(value, y1, y2, c1Prime, c2Prime):
    return f(value - c1Prime * y1 - c2Prime * y2)
 
def encrypt_func(key, original_values):
    normalized_original_values = []
    encrypted_values = []
    denormalized_encrypted_values = []
    c1Prime, c2Prime = key_func(key)
    #Convert Values [0,255] to Values [-1,1]
    for i in range(len(original_values)): 
        normalized_original_values.append(normalized(original_values[i])) 
    
    for i in range(len(normalized_original_values)):
        if i == 0:
            temp_encrypted_value = encrypt_value(normalized_original_values[0], y1_value, y2_value, c1Prime, c2Prime)
            temp_denormalized_encrypted_value = normalized(denormalized(temp_encrypted_value)) # NORMALIZED_CEPTION

            # print("Encrypted: " + str(temp_denormalized_encrypted_value))
            # print("Original: " + str(normalized_original_values[0])) 

            encrypted_values.append(temp_denormalized_encrypted_value)
        elif i == 1:
            temp_encrypted_value = encrypt_value(normalized_original_values[1], encrypted_values[0], y1_value, c1Prime, c2Prime)
            temp_denormalized_encrypted_value = normalized(denormalized(temp_encrypted_value)) # NORMALIZED_CEPTION

            # print("Encrypted: " + str(temp_denormalized_encrypted_value)) 
            # print("Original: " + str(normalized_original_values[1])) 

            encrypted_values.append(temp_denormalized_encrypted_value) 
        else:
            temp_encrypted_value = encrypt_value(normalized_original_values[i], encrypted_values[i - 1], encrypted_values[i - 2], c1Prime, c2Prime)
            temp_denormalized_encrypted_value = normalized(denormalized(temp_encrypted_value)) # NORMALIZED_CEPTION

            # print("Encrypted: " + str(temp_denormalized_encrypted_value)) 
            # print("Original: " + str(normalized_original_values[i])) 

            encrypted_values.append(temp_denormalized_encrypted_value)  
    
    # Denormalized to [0, 255]
    for i in range(len(encrypted_values)):
        denormalized_encrypted_values.append(denormalized(encrypted_values[i]))

    return denormalized_encrypted_values

def decrypt_func(key, encrypted_values):
    normalized_encrypted_values = []
    decrypted_values = []
    denormalized_decrypted_values = []
    c1Prime, c2Prime = key_func(key)
    #Convert Values [0,255] to Values [-1,1]
    for i in range(len(encrypted_values)): 
        normalized_encrypted_values.append(normalized(encrypted_values[i])) 

    for i in range(len(normalized_encrypted_values)):
        if i == 0:
            decrypted_values.append(decrypt_value(normalized_encrypted_values[0], y1_value, y2_value, c1Prime, c2Prime))
        elif i == 1:
            decrypted_values.append(decrypt_value(normalized_encrypted_values[1], normalized_encrypted_values[0], y1_value, c1Prime, c2Prime))
        else: 
            decrypted_values.append(decrypt_value(normalized_encrypted_values[i], normalized_encrypted_values[i - 1], normalized_encrypted_values[i - 2], c1Prime, c2Prime))

    # Denormalized to [0, 255]
    for i in range(len(decrypted_values)):
        denormalized_decrypted_values.append(denormalized(decrypted_values[i]))
        
    return denormalized_decrypted_values
 

def encrypt_text(key, original_text):
    print("==== Start Text Encryption Process ====")
    print("\nOriginal Text: " + original_text)
    
    original_values = []
    denormalized_encrypted_values = []
    encrypted_text = ""
    
    #Convert ASCII Text to Values [0,255]
    for i in range(len(original_text)): 
        original_values.append(ord(original_text[i]))  

    denormalized_encrypted_values = encrypt_func(key, original_values) 

    for i in range(len(denormalized_encrypted_values)):
        encrypted_text += chr(denormalized_encrypted_values[i])
    print("\nEncrypted Text: " + encrypted_text)
    print("==== End Text Encryption Process ====")
    return encrypted_text

def decrypt_text(key, encrypted_text):
    print("==== Start Text Decryption Process ====")
    print("\nEncrypted Text: " + encrypted_text)

    encrypted_values = []
    denormalized_decrypted_values = []
    decrypted_text = ""
    
    #Convert ASCII Text to Values [0,255]
    for i in range(len(encrypted_text)): 
        encrypted_values.append(ord(encrypted_text[i]))  

    denormalized_decrypted_values = decrypt_func(key, encrypted_values) 

    for i in range(len(denormalized_decrypted_values)):
        decrypted_text += chr(denormalized_decrypted_values[i])

    print("\nDecrypted Text: " + decrypted_text)
    print("==== End Text Decryption Process ====")
    return decrypted_text  

import numpy as np
from PIL import Image

def encrypt_decrypt_image(key, original_image):
    print("==== Start Image Encryption Process ====") 
    # Check if the image is loaded successfully
    if original_image is None:
        print("Error: Unable to load the image.")
        return None
    else:
        # Reshape the image array to a one-dimensional array
        flattened_image = original_image.ravel() # -1 means automatic calculation of the size

        # Print the flattened array of pixel values
        print("Flattened pixel values array:\n", flattened_image) 
        print("Original Length: " + str(len(flattened_image)))

        print("Encrypt: ")
        flattened__encrypted_image = encrypt_func(key, flattened_image)
        encrypted_image = np.reshape(flattened__encrypted_image, original_image.shape)
        # Print the flattened array of pixel values
        print("Encrypted pixel values array:\n", encrypted_image) 
        print("Encrypted Length: " + str(len(encrypted_image))) 

        print("Flattened pixel values array:\n", flattened__encrypted_image) 
        print("Original Length: " + str(len(flattened__encrypted_image)))
        print("Decrypt: ") 
        
        decrypted_image = decrypt_func(key, flattened__encrypted_image)
        decrypted_image = np.reshape(decrypted_image, encrypted_image.shape)
        # Print the flattened array of pixel values
        print("Decrypted pixel values array:\n", decrypted_image) 
        print("Decrypted Length: " + str(len(decrypted_image))) 

        return encrypted_image, decrypted_image 

# Example Usage

original_image_path = "images/original.png"
encrypted_image_path = "images/encrypted/image_24b5bc30-ef4d-4b13-ac66-4357f7767cc2.png"
decrypted_image_path = "decrypted_image.png"

original_video_path = "original_video.png"
encrypted_video_path = "encrypted_video.png"
decrypted_video_path = "decrypted_video.png"  

#encrypt_decrypt_image(key, cv2.imread(original_image_path))

def encrypt_decrypt_video(key, video_path):
    cap = cv2.VideoCapture(video_path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    encrypted_video_path = "videos/encrypted/video_" + str(uuid.uuid4()) + ".mp4"
    outEncrypted = cv2.VideoWriter(encrypted_video_path, fourcc, fps, (width, height))
    decrypted_video_path = "videos/decrypted/video_" + str(uuid.uuid4()) + ".mp4"
    outDecrypted = cv2.VideoWriter(decrypted_video_path, fourcc, fps, (width, height))

    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        # Assuming you have an encrypt_image function
        # Replace "encrypt_image" with your actual encryption function
        encrypted_frame, decrypted_frame = encrypt_decrypt_image(key, frame)

        # You can also modify this part to save the frames in a temporary folder

        outEncrypted.write(encrypted_frame)
        outDecrypted.write(decrypted_frame)

    cap.release()
    outEncrypted.release()
    outDecrypted.release()
    return encrypted_video_path, decrypted_video_path

def encrypt_func_raw(key, normalized_original_values): 
    encrypted_values = [] 
    c1Prime, c2Prime = key_func(key)

    for i in range(len(normalized_original_values)):
        if i == 0:
            temp_encrypted_value = encrypt_value(normalized_original_values[0], y1_value, y2_value, c1Prime, c2Prime) 
            encrypted_values.append(temp_encrypted_value) 
        elif i == 1:
            temp_encrypted_value = encrypt_value(normalized_original_values[1], encrypted_values[0], y1_value, c1Prime, c2Prime) 
            encrypted_values.append(temp_encrypted_value) 
        else:
            temp_encrypted_value = encrypt_value(normalized_original_values[i], encrypted_values[i - 1], encrypted_values[i - 2], c1Prime, c2Prime) 
            encrypted_values.append(temp_encrypted_value)

    return encrypted_values

def decrypt_func_raw(key, normalized_encrypted_values): 
    decrypted_values = []
    c1Prime, c2Prime = key_func(key) 

    for i in range(len(normalized_encrypted_values)):
        if i == 0:
            decrypted_values.append(decrypt_value(normalized_encrypted_values[0], y1_value, y2_value, c1Prime, c2Prime))
        elif i == 1:
            decrypted_values.append(decrypt_value(normalized_encrypted_values[1], normalized_encrypted_values[0], y1_value, c1Prime, c2Prime))
        else:
            decrypted_values.append(decrypt_value(normalized_encrypted_values[i], normalized_encrypted_values[i - 1], normalized_encrypted_values[i - 2], c1Prime, c2Prime))
        
    return decrypted_values
 

def encrypt_decrypt_audio(key, audio_file_path):
    # Read the audio file using soundfile
    audio, samplerate = sf.read(audio_file_path)

    encrypted_audio = encrypt_func_raw(key, audio) 
 
    encrypted_audio_path = "audios/encrypted/audio_" + str(uuid.uuid4()) + ".wav"
    sf.write(encrypted_audio_path, encrypted_audio, samplerate)

    decrypted_audio = decrypt_func_raw(key, encrypted_audio)
 
    decrypted_audio_path = "audios/decrypted/audio_" + str(uuid.uuid4()) + ".wav"
    sf.write(decrypted_audio_path, decrypted_audio, samplerate) 

    # Print the result
    print("Original Length Audio", len(audio))
    print("Encrypted Length Audio", len(encrypted_audio))
    print("Decrypted Length Audio", len(decrypted_audio))
    return encrypted_audio_path, decrypted_audio_path

# Example usage
audio_file_path = "audios/original.wav"
#print(decrypt_text(key, encrypt_text(key, "a")))
#encrypt_decrypt_audio(key, audio_file_path) 
#print(encrypt_func(key, [100, 200, 300]))
import numpy as np
import cv2
import hashlib

def load_private_key(filename="private_key.bin"):
    with open(filename, 'rb') as f:
        return f.read()

def load_signature(filename="signature.bin"):
    with open(filename, 'rb') as f:
        return f.read()

def extract_dotcode_bits_from_image(filename, point_radius=4, spacing=12, margin=10, threshold=128):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    dotcode_matrix = []

    rows = (height - 2 * margin) // (point_radius * 2 + spacing)
    cols = (width - 2 * margin) // (point_radius * 2 + spacing)

    for y in range(rows):
        row_bits = []
        for x in range(cols):
            center_x = margin + x * (point_radius * 2 + spacing) + point_radius
            center_y = margin + y * (point_radius * 2 + spacing) + point_radius
            pixel_intensity = img[center_y, center_x]
            if pixel_intensity < threshold:
                row_bits.append(1)
            else:
                row_bits.append(0)
        dotcode_matrix.extend(row_bits)

    return np.array(dotcode_matrix)

def verify_key(images, user_code, private_key_filename="private_key.bin", signature_filename="signature.bin"):
    private_key = load_private_key(private_key_filename)
    stored_signature = load_signature(signature_filename)
    reconstructed_bits = []

    for image in images:
        face_bits = extract_dotcode_bits_from_image(image)
        reconstructed_bits.extend(face_bits)
    
    reconstructed_key = bytes(reconstructed_bits)
    
    # Generate signature from the reconstructed key and user code
    reconstructed_signature = hashlib.sha256(reconstructed_key + user_code.encode()).digest()

    if reconstructed_key == private_key and reconstructed_signature == stored_signature:
        print("Access granted: Dotcode and user code match the original signature.")
        return True
    else:
        print("Access denied: Dotcode or user code does not match.")
        return False

# Run the script with images and user code
user_code = input("Enter your 10-digit user code: ")
images = ["face_1_dotcode.png", "face_2_dotcode.png", "face_3_dotcode.png"]
verify_key(images, user_code)


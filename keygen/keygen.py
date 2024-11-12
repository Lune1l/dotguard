import secrets
import numpy as np
from PIL import Image, ImageDraw
import hashlib

def generate_aes_key():
    # Generates a 128-bit AES key (16 bytes)
    return secrets.token_bytes(16)

def key_to_dotcode_matrix(key_bytes):
    # Convert the first 120 bits of the key to a 3x40 matrix
    key_bits = ''.join(f"{byte:08b}" for byte in key_bytes[:15])  # Only use the first 120 bits
    dotcode = np.array([int(bit) for bit in key_bits]).reshape(3, 40)
    return dotcode

def save_dotcode_as_image(dotcode_matrix, filename, point_radius=4, spacing=12, margin=10):
    # Creates an image for the dotcode matrix
    width = (dotcode_matrix.shape[1] * (point_radius * 2 + spacing)) + 2 * margin
    height = (dotcode_matrix.shape[0] * (point_radius * 2 + spacing)) + 2 * margin
    img = Image.new("L", (width, height), color=255)  # White background
    draw = ImageDraw.Draw(img)

    for y, row in enumerate(dotcode_matrix):
        for x, bit in enumerate(row):
            if bit == 1:
                center_x = margin + x * (point_radius * 2 + spacing) + point_radius
                center_y = margin + y * (point_radius * 2 + spacing) + point_radius
                draw.ellipse(
                    (center_x - point_radius, center_y - point_radius, center_x + point_radius, center_y + point_radius),
                    fill=0  # Black dot
                )

    img.save(filename)

def generate_cryptographic_signature(key_bytes, user_code):
    # Combine the key and user code, then hash for additional security
    combined = key_bytes + user_code.encode()
    return hashlib.sha256(combined).digest()

# Generate keys, dotcodes, and files for each face
user_code = input("Enter a 10-digit code for the user: ")
private_key_bits = []
for i in range(1, 4):
    key = generate_aes_key()
    dotcode_matrix = key_to_dotcode_matrix(key)
    private_key_bits.extend(dotcode_matrix.flatten().tolist())
    save_dotcode_as_image(dotcode_matrix, f"face_{i}_dotcode.png")

# Save full private key and cryptographic signature
private_key = bytes(private_key_bits)
signature = generate_cryptographic_signature(private_key, user_code)

with open("private_key.bin", 'wb') as f:
    f.write(private_key)

with open("signature.bin", 'wb') as f:
    f.write(signature)

print("Keys and dotcodes generated and saved for each face.")
print("Private key and cryptographic signature saved.")


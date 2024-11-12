# Secure Triangle Key Access System

![Project Logo](/project_ressources/logo_white.png)

This project is a proof of concept for a physical security access system using a triangular key engraved with a unique dot pattern representing an AES encryption key. The key system relies on a laser scanner that reads the dot-encoded keys on each face of the triangle to validate access.

## Project Overview

The **Secure Triangle Key Access System** combines physical and digital security by using a physical triangular key engraved with unique dot patterns to control access. Each face of the key encodes a unique AES-128 encryption key in a dot matrix format, ensuring that only the correct key provides access.

## System Details

1. **Triangular Key Design**: The physical key has three faces, each engraved with a unique dot pattern encoding a 128-bit AES key.
2. **Dot Encoding**: Each face’s dot matrix has 3 rows by 40 bits (120 bits per face), representing a unique encoded AES key.
3. **Laser Reader**: A laser scanner reads the dot pattern on each face, verifying the key's authenticity based on the dotcode.
4. **Two-Factor Security**:
   - **AES Encryption**: Each face encodes a unique 128-bit AES key for secure validation.
   - **User Code**: A 10-digit user code is required along with the physical key to confirm access. This code is cryptographically combined with the dotcode to validate the key.

## Python Key Generation Script

The Python script `keygen.py` generates three AES-128 keys, converts each to a dot matrix, and saves the following files:

- **Dotcode Images**: PNG images with circular dot patterns for each face (`face_1_dotcode.png`, `face_2_dotcode.png`, `face_3_dotcode.png`).
- **Binary Files**: Each face’s AES key stored in binary format (`face_1_key.bin`, `face_2_key.bin`, `face_3_key.bin`).
- **Combined Private Key**: A single file, `private_key.bin`, storing the combined keys of all faces for verification purposes.
- **Cryptographic Signature**: The script generates a SHA-256 hash signature that combines the complete private key with the 10-digit user code. This signature is saved in `signature.bin` for secure validation.

## Verification and Validation Script

The verification script `verify_key.py` reads the dot pattern images from each face, reconstructs the key, and combines it with the 10-digit user code to validate against the stored private key and signature. The script performs the following:

- Uses OpenCV to read dot matrices from the face images.
- Reconstructs the key from the dotcode images.
- Combines the reconstructed key with the user code to generate a new cryptographic signature.
- Compares this new signature with the original signature stored in `signature.bin` to validate the key.

### Generated Files Summary

- **Dotcode Images**: PNG files for each face, showing the dot patterns (`face_1_dotcode.png`, `face_2_dotcode.png`, `face_3_dotcode.png`).
- **Binary AES Key Files**: Each face's AES key stored in binary format (`face_1_key.bin`, `face_2_key.bin`, `face_3_key.bin`).
- **Private Key File**: A single `private_key.bin` file containing all keys for verification.
- **Signature File**: `signature.bin`, containing the cryptographic signature generated with the user code.

## Getting Started

### Prerequisites

Install the required libraries:

```bash
pip install numpy pillow opencv-python
```

### Running the Key Generation Script

Run the following command to generate keys, dotcode images, and the signature:
```bash
python keygen.py
```
### Running the Verification Script

To verify a key against the private key and signature, use:
```bash
python verify_key.py
```
Ensure that face_1_dotcode.png, face_2_dotcode.png, face_3_dotcode.png, private_key.bin, and signature.bin are in the same directory as the script.

##Dependencies

    Python 3.x
    NumPy
    Pillow (PIL)
    OpenCV


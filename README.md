# Secure Triangle Key Access System

![Project Logo](/project_ressources/logo_white.png)

This project is a proof of concept for a physical security access system using a triangular key engraved with a unique dot pattern, which represents an AES encryption key. The key system relies on a laser scanner that reads the dot-encoded keys on each face of the triangle to validate access.

## Project Overview

The **Secure Triangle Key Access System** leverages a physical triangular key with engraved dots on each face to provide a secure access mechanism. Each face of the key represents a unique AES-128 encryption key encoded as a dot pattern, offering a secure and unique method of access control.

## System Details

1. **Triangular Key Design**: The physical key has three faces, each engraved with a unique pattern of dots that encode a 128-bit AES key.
2. **Dot Encoding**: Each face contains a dot matrix of 3 rows x 40 bits (120 bits per face), representing the encoded key.
3. **Laser Reader**: A laser scanner detects the dot pattern on each face, verifying the key's authenticity based on the dotcode pattern.
4. **Security Enhancements**:
   - AES encryption (128-bit) ensures data security.
   - Each face contains a separate AES key.
   - A combined private key is saved for secure access validation.

## Python Key Generation Script

The Python script `keygen.py` generates three AES-128 keys, converts each to a dot matrix, and saves the following:

- **Dotcode Images**: PNG images with circular dot patterns for each face (`face_1_dotcode.png`, `face_2_dotcode.png`, `face_3_dotcode.png`).
- **Binary Files**: Each face's AES key saved in binary (`face_1_key.bin`, `face_2_key.bin`, `face_3_key.bin`).
- **Combined Private Key**: A file `private_key.bin` containing all three keys for validation purposes.

## Verification and Validation Script

The verification script verify_key.py checks the dot patterns on the images of each face against the stored private key. It uses OpenCV to read dot matrices from images, reconstitutes the key from these matrices, and validates it against the stored private key.

Generated Files

    Dotcode Images: PNG files for each face, displaying dot patterns (face_1_dotcode.png, face_2_dotcode.png, face_3_dotcode.png).
    Binary Files: Each face's AES key stored as a binary file (face_1_key.bin, face_2_key.bin, face_3_key.bin).
    Private Key File: private_key.bin containing the complete set of AES keys for verification.

## Getting Started
### Prerequisites

Install required libraries:

```bash
pip install numpy pillow opencv-python
```

### Running the Key Generation Script

Run the following command to generate keys and dotcode images:

```bash
python keygen.py
```
### Running the Verification Script

To verify a key against the private key file, use:
```bash
python verify_key.py
```
Ensure that face_1_dotcode.png, face_2_dotcode.png, face_3_dotcode.png, and private_key.bin are in the same directory.

## Dependencies

    Python 3.x
    NumPy
    Pillow (PIL)
    OpenCV


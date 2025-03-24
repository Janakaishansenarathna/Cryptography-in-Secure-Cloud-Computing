# Cryptography in Secure Cloud Computing

A sample project demonstrating file encryption and decryption for secure cloud computing using Python and Fernet symmetric encryption.

## Repository Contents

- **`encrypt.py`**: Python script for encrypting files.
- **`decrypt.py`**: Python script for decrypting files.
- **`generate_key.py`**: Script to generate a Fernet encryption key.
- **`sample.txt`**: Example text file for encryption/decryption.
- **`requirements.txt`**: List of dependencies to install.
- **Output files**: Encrypted/decrypted results (e.g., `sample_encrypted.txt`, `sample_decrypted.txt`).

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Generate Encryption Key
First, generate a Fernet key to use for encryption/decryption:
```bash
python generate_key.py
```
This creates a `fernet_key.key` file in the project directory.

---

### Step 2: Encrypt a File
To encrypt the provided `sample.txt` file:
```bash
python encrypt.py
```
- **Input**: `sample.txt`  
- **Output**: `sample_encrypted.txt`

---

### Step 3: Decrypt the File
To decrypt the encrypted file:
```bash
python decrypt.py
```
- **Input**: `sample_encrypted.txt`  
- **Output**: `sample_decrypted.txt` (restores the original content).

---

## Support

- **Issues**: Open a ticket on the [GitHub Issues](https://github.com/yourusername/yourproject/issues) page.
- **Contact**: See the repository's "About" section for direct contact details.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

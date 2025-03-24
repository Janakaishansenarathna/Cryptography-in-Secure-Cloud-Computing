from cryptography.fernet import Fernet

def decrypt_file(input_file, key_file, output_file):
    with open(key_file, 'rb') as f:
        key = f.read()
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    plaintext = cipher_suite.decrypt(ciphertext)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    input_filename = "sample.enc"
    key_filename = "secret.key"
    output_filename = "sample.dec"
    decrypt_file(input_filename, key_filename, output_filename)
    print(f"File '{input_filename}' decrypted to '{output_filename}'")
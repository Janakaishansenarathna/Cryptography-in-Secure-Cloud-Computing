from cryptography.fernet import Fernet

def encrypt_file(input_file, key_file, output_file):
    with open(key_file, 'rb') as f:
        key = f.read()
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher_suite.encrypt(plaintext)
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

if __name__ == "__main__":
    input_filename = "sample.txt"
    key_filename = "secret.key"
    output_filename = "sample.enc"
    encrypt_file(input_filename, key_filename, output_filename)
    print(f"File '{input_filename}' encrypted to '{output_filename}'")
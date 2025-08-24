import argparse

def decrypt_ciphertext(ciphertext_hex, d_hex, n_hex):
    # Convert hex values to integers
    ciphertext_int = int(ciphertext_hex, 16)
    d = int(d_hex, 16)
    n = int(n_hex, 16)

    # Decrypt the ciphertext
    plaintext_int = pow(ciphertext_int,d,n)

    # Convert decrypted integer back to hex
    plaintext_hex = hex(plaintext_int)[2:]

    # Convert hex to bytes and decode to ASCII
    plaintext_bytes = bytes.fromhex(plaintext_hex)
    plaintext_ascii = plaintext_bytes.decode('utf-8')

    return plaintext_ascii

def main():
    parser = argparse.ArgumentParser(description='Decrypt RSA ciphertext.')
    parser.add_argument('ciphertext', type=str, help='Ciphertext in hexadecimal')
    parser.add_argument('d', type=str, help='Private key in hexadecimal')
    parser.add_argument('n', type=str, help='Modulus in hexadecimal')

    args = parser.parse_args()

    plaintext = decrypt_ciphertext(args.ciphertext, args.d, args.n)
    
    print(f"Decrypted message: {plaintext}")

if __name__ == "__main__":
    main()

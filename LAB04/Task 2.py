

import argparse

def message_to_hex(message):
    return message.encode("utf-8").hex()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Encrypt a message using RSA.')
    parser.add_argument('n_hex', type=str, help='Hexadecimal value of n')
    parser.add_argument('e_hex', type=str, help='Hexadecimal value of e')
    parser.add_argument('message', type=str, help='Message to encrypt')

    # Parse arguments
    args = parser.parse_args()

    # Convert hex to integers
    n = int(args.n_hex, 16)
    e = int(args.e_hex, 16)

    # Convert message to hex and then to integer
    message_hex = message_to_hex(args.message)
    message_int = int(message_hex, 16)

    # Encrypt the message
    ciphertext_int = pow(message_int, e, n)
    ciphertext_hex = hex(ciphertext_int)[2:].upper()

    print(f"Encrypted message (ciphertext) in hex: {ciphertext_hex}")

if __name__ == "__main__":
    main()

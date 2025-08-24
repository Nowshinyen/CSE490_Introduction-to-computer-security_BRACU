import argparse
from sympy import mod_inverse

def message_to_hex(message):
    return message.encode("utf-8").hex()

def sign_message(message, d, n):
    # Convert message to hex
    message_hex = message_to_hex(message)
    # Convert hex to integer
    message_int = int(message_hex, 16)
    # Sign the message
    signature_int = pow(message_int,d,n)
    # Return signature as hex string
    return hex(signature_int)[2:].upper()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Sign a message using RSA.')
    parser.add_argument('n_hex', type=str, help='Hexadecimal value of n')
    parser.add_argument('d_hex', type=str, help='Hexadecimal value of d')
    parser.add_argument('message', type=str, help='Message to sign')

    # Parse arguments
    args = parser.parse_args()

    # Convert hex to integers
    n = int(args.n_hex, 16)
    d = int(args.d_hex, 16)

    # Sign the message
    signature = sign_message(args.message, d, n)

    print(f"Signature for the message: {signature}")

if __name__ == "__main__":
    main()

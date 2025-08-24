import argparse

def hex_to_int(hex_str):
    return int(hex_str, 16)

def verify_signature(message, signature_hex, e_hex, n_hex):
    # Convert message to hexadecimal
    message_hex = message.encode("utf-8").hex()
    message_int = hex_to_int(message_hex)
    
    # Convert public key components to integers
    e = hex_to_int(e_hex)
    n = hex_to_int(n_hex)
    
    # Convert signature to integer
    signature_int = hex_to_int(signature_hex)
    
    # Verify the signature
    calculated_message_int = pow(signature_int,e,n)
    calculated_message_hex = hex(calculated_message_int)[2:].upper()
    
    return calculated_message_hex == message_hex.upper()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Verify RSA signature.')
    parser.add_argument('message', type=str, help='Message to verify')
    parser.add_argument('signature', type=str, help='Signature in hexadecimal')
    parser.add_argument('e', type=str, help='Public exponent in hexadecimal')
    parser.add_argument('n', type=str, help='Modulus in hexadecimal')

    # Parse arguments
    args = parser.parse_args()

    # Verify the original signature
    is_valid = verify_signature(args.message, args.signature, args.e, args.n)
    print(f"Original signature valid: {is_valid}")


if __name__ == "__main__":
    main()

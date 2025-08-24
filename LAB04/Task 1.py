import argparse
from sympy import mod_inverse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Calculate RSA private key d.')
    parser.add_argument('p_hex', type=str, help='Hexadecimal value of p')
    parser.add_argument('q_hex', type=str, help='Hexadecimal value of q')
    parser.add_argument('e_hex', type=str, help='Hexadecimal value of e')

    # Parse arguments
    args = parser.parse_args()

    # Convert hexadecimal values to decimal
    p = int(args.p_hex, 16)
    q = int(args.q_hex, 16)
    e = int(args.e_hex, 16)

    # Calculate n
    n = p*q

    # Calculate φ(n)
    totient_n = (p-1)*(q-1)

    # Calculate the private key d
    d = mod_inverse(e, totient_n)

    # Print results in hexadecimal format
    n_hex = hex(n).upper()[2:]
    d_hex = hex(d).upper()[2:]

    print(f"Public key (e, n): ({args.e_hex}, {n_hex})")
    print(f"Private key d: {d_hex}")

if __name__ == "__main__":
    main()

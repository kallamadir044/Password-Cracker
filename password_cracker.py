import argparse
from hash_utils import hash_password
from crack_utils import dictionary_attack, brute_force_attack

def main():
    parser = argparse.ArgumentParser(description="Password Cracker")
    parser.add_argument('hash_value', type=str, help="Hash value of the password to crack")
    parser.add_argument('--mode', choices=['dictionary', 'brute-force'], default='dictionary', help="Mode of attack (default: dictionary)")
    parser.add_argument('--dictionary', type=str, help="Path to dictionary file")
    parser.add_argument('--charset', type=str, help="Character set for brute-force attack")
    parser.add_argument('--max-length', type=int, default=8, help="Maximum length for brute-force attack (default: 8)")
    args = parser.parse_args()

    if args.mode == 'dictionary' and args.dictionary:
        with open(args.dictionary, 'r') as f:
            dictionary = [line.strip() for line in f.readlines()]
        password = dictionary_attack(args.hash_value, dictionary)
    elif args.mode == 'brute-force' and args.charset:
        print(f"Attempting brute-force attack with charset: {args.charset}, max length: {args.max_length}")
        password = brute_force_attack(args.hash_value, args.charset, args.max_length)
    else:
        print("Invalid mode or missing required arguments.")
        return

    if password:
        print(f"Password cracked: {password}")
    else:
        print("Failed to crack the password.")

if __name__ == "__main__":
    main()

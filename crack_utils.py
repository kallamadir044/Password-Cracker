import hashlib
import itertools

def dictionary_attack(hash_value, dictionary):
    """ Performs a dictionary attack to crack the hash. """
    for password in dictionary:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if hashed == hash_value:
            return password
    return None

def brute_force_attack(hash_value, charset, max_length):
    """ Performs a brute-force attack to crack the hash. """
    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            password = ''.join(combination)
            hashed = hashlib.sha256(password.encode()).hexdigest()
            if hashed == hash_value:
                return password
    return None

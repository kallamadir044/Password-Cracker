import hashlib

def hash_password(password, algorithm='sha256'):
    """ Hashes a password using a specified algorithm. """
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

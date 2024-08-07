import hashlib


def password_encrypt_sha512(password):
    """
    Hashes a password using SHA-512.

    :param password: Password to hash (string)
    :return: SHA-512 hash of the password (hexadecimal string).
    """
    return hashlib.sha512(password.encode()).hexdigest()

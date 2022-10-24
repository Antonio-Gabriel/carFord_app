import bcrypt


def generate_password(password: str) -> str:
    """generate a hash to password"""
    salt = bcrypt.gensalt()
    return str(bcrypt.hashpw(password.encode('utf-8'), salt))


def check_password(hash_password: bytes, password: bytes) -> bool:
    """compare password"""
    return bcrypt.checkpw(password, hash_password)

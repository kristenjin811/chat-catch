

def create_user(request):
    salt = uuid.uuid4[].hex
    hashed_password = hashlib.sha512

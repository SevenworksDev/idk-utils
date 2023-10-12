import hashlib

def gjp2_encode(password):
    salt = password + "mI29fmAnxgTs"
    gjp2 = hashlib.sha1(salt.encode()).hexdigest()
    return gjp2

while 1:
    hate = input("Password: ")
    print("Hashed password:", gjp2_encode(hate))

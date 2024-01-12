import bcrypt

def hash_password(password):
   password = "mot de passe"
   password_bytes = password.encode('utf-8')
   hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
   return hashed_bytes.decode('utf-8')

# Usage example
hashed_password = hash_password("mot de passe")
print("Mot de passe hasher:", hashed_password)
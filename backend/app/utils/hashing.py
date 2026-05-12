import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import asyncio
from concurrent.futures import ThreadPoolExecutor
import os
import asyncio
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from base64 import b64encode, b64decode

executor = ThreadPoolExecutor()

async def hash_password(password: str) -> str:
    """Hash the password before storing it in the database (asynchronous wrapper)."""
    return await asyncio.to_thread(_hash_password_sync, password)

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify the password by comparing the plain password with the hashed one (asynchronous wrapper)."""
    return await asyncio.to_thread(_verify_password_sync, plain_password, hashed_password)

async def hash_phone(phone: str) -> str:
    """Hash the phone number before storing it in the database (asynchronous wrapper)."""
    return await asyncio.to_thread(_hash_phone_sync, phone)

def _hash_password_sync(password: str) -> str:
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    hashed_password = kdf.derive(password.encode())  # Derive the hashed password
    return b64encode(salt + hashed_password).decode('utf-8')

def _verify_password_sync(plain_password: str, hashed_password: str) -> bool:
    decoded = b64decode(hashed_password.encode('utf-8'))
    salt, stored_hash = decoded[:16], decoded[16:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    try:
        kdf.verify(plain_password.encode(), stored_hash)
        return True
    except Exception:
        return False

def _hash_phone_sync(phone: str) -> str:
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    hashed_phone = kdf.derive(phone.encode())  # Derive the hashed phone number
    return b64encode(salt + hashed_phone).decode('utf-8')

async def verify_phone_async(phone: str, stored_hash: str) -> bool:
    """Asynchronously verifies if a given phone number matches the stored hash."""
    decoded_data = b64decode(stored_hash)  
    salt, stored_hashed_phone = decoded_data[:16], decoded_data[16:]  # Extract salt and hashed value

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    try:
        kdf.verify(phone.encode(), stored_hashed_phone)  # Verify the hash
        return True  # Match found
    except Exception:
        return False
    

load_dotenv()
AES_KEY_HEX = os.getenv("AES_KEY")

if not AES_KEY_HEX:
    raise ValueError("AES_KEY not found in environment variables!")

# Convert from hex to bytes
AES_KEY = bytes.fromhex(AES_KEY_HEX)  

# Validate AES key length
if len(AES_KEY) != 32:
    raise ValueError("Invalid AES_KEY! Must be exactly 32 bytes.")


# 🔹 Async Function to Encrypt Phone Number
async def encrypt_phone(phone: str):
    aesgcm = AESGCM(AES_KEY)  # Create AES cipher
    nonce = os.urandom(12)  # Generate a 12-byte nonce
    encrypted_data = aesgcm.encrypt(nonce, phone.encode(), None)
    return b64encode(nonce + encrypted_data).decode("utf-8")  # Encode to Base64 for storage


# 🔹 Async Function to Decrypt Phone Number
async def decrypt_phone(encrypted_phone: str):
    aesgcm = AESGCM(AES_KEY)  # Create AES cipher
    encrypted_data = b64decode(encrypted_phone)  # Decode Base64
    nonce, ciphertext = encrypted_data[:12], encrypted_data[12:]  # Extract nonce & ciphertext
    decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted_data.decode("utf-8")


# 🔹 Example Usage (Test)
async def main():
    phone_number = "1234567890"
    encrypted = await encrypt_phone(phone_number)
    decrypted = await decrypt_phone(encrypted)

    print(f"Original: {phone_number}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

# import os

# # Generate a 32-byte AES key
# aes_key = os.urandom(32)  # ✅ Correct length in bytes

# # Convert to hex (for storage in .env)
# aes_key_hex = aes_key.hex()  # 64-character hex string

# # Validate Correctness
# if len(aes_key) != 32:  # Check raw bytes, not hex string
#     raise ValueError("Invalid AES_KEY! Must be exactly 32 bytes.")

# print(f"AES_KEY (Hex): {aes_key_hex}")  # Save this in .env

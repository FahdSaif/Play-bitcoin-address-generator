
import os
import hashlib
import ecdsa
import base58

#GENERATE a random 32 bit provate key
private_key = os.urandom(32).hex()
print(f"Private Key: {private_key}")

#derive the public key
sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key),curve=ecdsa.SECP256k1)
vk = sk.verifying_key
public_key = b'\x04' + vk.to_string()  # Append 04 prefix for uncompressed pubkey
print(f"Public Key: {public_key.hex()}")

# 3. Hash the public key (SHA-256 then RIPEMD-160)
sha256_hash = hashlib.sha256(public_key).digest()
ripemd160 = hashlib.new('ripemd160', sha256_hash).digest()

# 4. Add network byte (0x00 for Mainnet)
network_byte = b'\x00' + ripemd160

# 5. Compute the checksum (first 4 bytes of double SHA-256)
checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]

# 6. Generate the final Bitcoin address (Base58Check encoding)
bitcoin_address = base58.b58encode(network_byte + checksum).decode()
print(f"Bitcoin Address: {bitcoin_address}")


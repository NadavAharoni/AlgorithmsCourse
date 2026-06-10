def xor_encrypt(text, key):
    # key is repeated to match message length
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(text)])

xor_decrypt = xor_encrypt   # same operation!

key = b"secret"
plaintext = b"Hello, world!"

ciphertext = xor_encrypt(plaintext, key)
recovered  = xor_decrypt(ciphertext, key)

print(ciphertext)          # garbled bytes
print(recovered)           # b'Hello, world!'


for i, b in enumerate(plaintext):
    print(f"plaintext byte {i}: {b} (char: {chr(b)})")


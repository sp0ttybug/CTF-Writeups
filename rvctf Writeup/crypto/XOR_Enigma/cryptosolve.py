from binascii import unhexlify

# Given hexadecimal strings
X1_hex = "b3c8d73e3a9b23df7cc1253277a4878ef65bcfe9735f29d84424"
X2_X1_hex = "fb3514ac2e94885e9d5ec915821650572d5e0b842e9630f32b1b"
X2_X3_hex = "d2656867798e8584ec34ab2d4562b1a9c82b8fcf1feeeddf70e2"
FLAG_X1_X3_X2_hex = "07c1de3e3867c32fe29cbd6957a2695f0e021f4b58c2b03446bb"

# Convert hex to bytes
X1 = unhexlify(X1_hex)
X2_X1 = unhexlify(X2_X1_hex)
X2_X3 = unhexlify(X2_X3_hex)
FLAG_X1_X3_X2 = unhexlify(FLAG_X1_X3_X2_hex)

# XOR function
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Find X2
X2 = xor_bytes(X2_X1, X1)

# Find X3
X3 = xor_bytes(X2_X3, X2)

# Find FLAG
FLAG = xor_bytes(FLAG_X1_X3_X2, xor_bytes(X1, xor_bytes(X3, X2)))

# Print the FLAG as text
print("FLAG:", FLAG.decode())

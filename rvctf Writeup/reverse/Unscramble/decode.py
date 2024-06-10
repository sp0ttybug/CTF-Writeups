import base64

def xor_with_key(hex_input, key):
    xored = ""
    for i in range(0, len(hex_input), 2):
        hex_char = int(hex_input[i:i+2], 16)
        hex_char ^= key
        xored += chr(hex_char)
    return xored

def hex_to_ascii(hex_input):
    ascii_str = ""
    for i in range(0, len(hex_input), 2):
        ascii_str += chr(int(hex_input[i:i+2], 16))
    return ascii_str

def caesar_shift(input_str, amount):
    shifted = ""
    for c in input_str:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            shifted += chr((ord(c) - ord(base) - amount) % 26 + ord(base))
        else:
            shifted += c
    return shifted

def main():
    encrypted_flag = "465a38585060405f685f4465734d6a636d4f45705f4e67384565403d5d5c6e506d5d3c4d513a513c5862663c58636a736a5c404d504e6639453866676d4f3873"

    # Step 1: XOR with key 9
    step1 = xor_with_key(encrypted_flag, 9)
    print(f"After XOR: {step1}")
    
    # Step 2: Convert from hexadecimal to ASCII
    step2 = hex_to_ascii(step1.encode('utf-8').hex())
    print(f"After hex to ASCII: {step2}")
    
    # Step 3: Reverse the Caesar shift by 25
    step3 = caesar_shift(step2, 25)
    print(f"After Caesar shift: {step3}")
    
    # Step 4: Base64 decode
    step4 = base64.b64decode(step3).decode()
    print(f"After Base64 decode 1: {step4}")
    
    # Step 5: Reverse the string
    step5 = step4[::-1]
    print(f"After reversing: {step5}")
    
    # Step 6: Base64 decode
    flag = base64.b64decode(step5).decode()
    print("The flag is:", flag)

if __name__ == "__main__":
    main()

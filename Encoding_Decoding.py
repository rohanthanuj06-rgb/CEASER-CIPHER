def encode(message, shift):
    encoded_msg = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encoded_char = chr(start + (ord(char) - start + shift) % 26)
            encoded_msg += encoded_char
        else:
            encoded_msg += char 
    return encoded_msg


def decode(encoded_msg, shift):
    decoded_msg = ""
    for char in encoded_msg:
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a')
            decoded_char = chr(start + (ord(char) - start - shift) % 26)
            decoded_msg += decoded_char
        else:
            decoded_msg += char 
    return decoded_msg

message =input("Enter the message to be encoded :")
shift = int(input("enter the number of shift places:"))


encoded = encode(message, shift)
print(f"Encoded Message: {encoded}")
ch=input("Do you wanna view the decoded message  (yes/no):")
if ch=="YES "or "yes":
    decoded = decode(encoded, shift)
print(f"Decoded Message: {decoded}")



print("\n\nTHIS CODING USES A METHOD KNOWN AS  CEASER CIPHER , WHICH MEANS ENCODING MESSAGES BY SWTICHING INDICES OF ALPHABETS..")

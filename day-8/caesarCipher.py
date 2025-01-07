alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt function
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet) #Make shifted_position number always on the range of alphabet length
        cipher_text += alphabet[shifted_position]


    print(f"Here is the encoded result: {cipher_text}")



# Decrypt function
def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

if direction.lower() == "encode":
    encrypt(original_text=text, shift_amount=shift)

elif direction.lower() == "decode":
    decrypt(original_text=text, shift_amount=shift)
else:
    print("You inputed wrong code")       
        
# def caesar(original_text, shift_amount, encode_or_decode):
#    output_text = ""
#    for letter in original_text:

#        if encode_or_decode == "decode":
#            shift_amount *= -1
        
#        shifted_position = alphabet.index(letter) + shift_amount
#        shifted_position %= len(alphabet)
#        output_text += alphabet[shifted_position]
#    print(f"Here is the encoded result: {output_text}")
#
# caesar(text, shift, direction)

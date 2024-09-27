morse_code = {
    'A': '•–', 'B': '–•••', 'C': '–•–•', 'D': '–••', 'E': '•', 'F': '••–•', 'G': '––•', 'H': '••••', 'I': '••',
    'J': '•–––', 'K': '–•–', 'L': '•–••', 'M': '––', 'N': '–•', 'O': '–––', 'P': '•––•', 'Q': '––•–', 'R': '•–•',
    'S': '•••', 'T': '–', 'U': '••–', 'V': '•••–', 'W': '•––', 'X': '–••–', 'Y': '–•––', 'Z': '––••', '0': '–––––',
    '1': '•––––', '2': '••–––', '3': '•••––', '4': '••••–', '5': '•••••', '6': '–••••', '7': '––•••', '8': '–––••',
    '9': '––––•', '.': '•–•–•–', ',': '––••––', '?': '••––••', "'": '•––––•', '/': '–••–•', '()': '–•––•–', '&': '•–•••',
    ':': '–––•••', ';': '–•–•–•', '=': '–•••–', '+': '•–•–•', '-': '–••••–', '"': '•–••–•', ' ': '/'
}

reverse_morse_code = {v: k for k, v in morse_code.items()}


choice = input("Do you want to encode or decode? "
               "Enter e for encode and d for decode: ").lower()

if choice == "e":
    message = str(input("Enter the message to encode: ")).upper()
    encoded_message = []
    for char in message:
        if char not in morse_code.keys():
            print(f"The character '{char}' doesn't exists. Skipping it.")
        else:
            encoded_message.append(morse_code[char])

    encoded_message = " ".join(encoded_message)
    print("The Encoded message.")
    print(encoded_message)

elif choice == "d":
    encrypted_message = str(input("Enter the encrypted message to decode: ")).split()

    decoded_message = []
    for code in encrypted_message:
        if code in reverse_morse_code:
            decoded_message.append(reverse_morse_code[code])
        else:
            print(f"The code '{code}' is invalid. Skipping it.")

    decoded_message = "".join(decoded_message)
    print("The Decoded message.")
    print(decoded_message)
else:
    print("Character not supported. Either enter 'e' or 'd'.")




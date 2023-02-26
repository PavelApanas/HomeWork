def morse_encode(message):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    encoded_message = []
    for char in message.upper():
        if char == ' ':
            encoded_message.append('/')
        elif char in morse_code:
            encoded_message.append(morse_code[char])
        else:
            pass
    return ' '.join(encoded_message)

message = 'Hello'
encoded_message = morse_encode(message)
print(f'Сообщение "{message}" в коде Морзе: {encoded_message}')
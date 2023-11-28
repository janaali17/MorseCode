
print("Welcome to morse code translation application") #this is gonna print a welcome message to the user when he runs the code
while True: #this while loop is used so that the applications keeps running until the user chooses 0 to exit
    options = input("enter 1 to encrypt from english to morse code, 2 to decrypt from morse code to english, and 0 to exit the application: ") #this asks the user to enter an input (Option) to start the process
    if options == "1": #if user enter "1" the commands below runs encryption translation
        english_to_morse_dict = { #this is the morse code, each english letter or number or symbol is represented in a specific dots and dashes in morses 
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/'}
        text = input("enter a text to encrypt: ") #asks user to eneter input
        encrypted_message = " ".join(english_to_morse_dict.get(char, "") for char in text.upper())
        print("your encyrpted text is : " ,encrypted_message) #this prints "your encyrpted text is: " then the encyrpted_message
    elif options == "2": #the below commands run if the user enters "2" decryption translation
        morse_to_english_dict = { 
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
            '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
            '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
            '...-..-': '$', '.--.-.': '@', '/': ' '}
        text = input("enter a text to decrypt: ") #asks the user 
        decrypted_message = "".join(morse_to_english_dict.get(char, "") for char in text.split()) 
        print("your decyrpted text is : " ,decrypted_message)
    elif options == "0":
        break #this is to exit the app
    else:
        print("option does not exist") 
        

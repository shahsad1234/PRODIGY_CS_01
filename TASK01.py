from colorama import Fore, Style, init
init(autoreset=True)

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char 
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def display_welcome_message():
    print(Fore.CYAN + "=" * 45)
    print(Fore.MAGENTA + "✨  Welcome to the Secret Message Encoder! ✨")
    print(Fore.CYAN + "=" * 45)
    print(Fore.YELLOW + "\nUnlock the power of encryption with the Caesar Cipher!")
    print("Protect your messages or reveal hidden secrets!\n" + Style.RESET_ALL)

def main():
    display_welcome_message()
    choice = input(Fore.GREEN + "Would you like to (e)ncrypt a message or (d)ecrypt a message? " + Style.RESET_ALL).lower()
    
    if choice in ['e', 'd']:
        text = input(Fore.YELLOW + "\nPlease enter your message: " + Style.RESET_ALL)
        shift = int(input(Fore.YELLOW + "Enter a shift value (1-25) to set your secret key: " + Style.RESET_ALL))
        
        if choice == 'e':
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(Fore.CYAN + "\n" + "=" * 45)
            print(Fore.GREEN + "🔐 Encrypted Message: " + Fore.WHITE + encrypted_text)
            print(Fore.CYAN + "=" * 45)
        elif choice == 'd':
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(Fore.CYAN + "\n" + "=" * 45)
            print(Fore.GREEN + "🔓 Decrypted Message: " + Fore.WHITE + decrypted_text)
            print(Fore.CYAN + "=" * 45)
    else:
        print(Fore.RED + "\nOops! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()

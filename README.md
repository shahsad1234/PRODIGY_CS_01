# Caesar Cipher Encryption & Decryption

This project is a Python implementation of the Caesar Cipher, a classic encryption technique that allows you to easily encrypt and decrypt messages using a simple shift-based substitution. This project provides an interactive way to explore basic cryptography principles while also offering a hands-on way to see how encryption transforms text.

## About the Caesar Cipher

The **Caesar Cipher** is a substitution cipher named after Julius Caesar, who reportedly used it to send secret messages. In this cipher, each letter in the plaintext (original message) is shifted by a specified number of positions in the alphabet. This shift "encrypts" the message, making it readable only by someone who knows the shift key.

For example, if the shift is 3:
- `A` becomes `D`
- `B` becomes `E`
- `Z` wraps around to `C`

To decrypt, the process is reversed by shifting in the opposite direction.

## How It Works

This Python program allows users to:
- **Encrypt a message**: Each letter in the input message is shifted forward by a user-specified number of positions.
- **Decrypt a message**: An encrypted message can be returned to its original form by shifting each letter back by the same number of positions.

The program supports both uppercase and lowercase letters, leaving special characters (spaces, punctuation, numbers) unchanged.

## Features

- **Encryption and Decryption**: Shift text forward for encryption or backward for decryption based on user input.
- **User-friendly**: Prompts guide users to choose between encrypting and decrypting, making the program suitable for all experience levels.
- **Non-letter Handling**: Punctuation, spaces, and numbers remain unchanged, so you can encrypt full sentences easily.

## Getting Started

### Prerequisites

This project requires **Python 3** to run. Make sure you have Python installed by typing:

```bash
python --version
```

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone git@github.com:Muhammedshahil24/PRODIGY_CS_01.git
    ```

2. Navigate to the project directory:
    ```bash
    cd caesar-cipher
    ```

3. Run the program:
    ```bash
    python task.py
    ```

## Usage

When the program runs, you’ll be prompted to:
1. Choose to encrypt or decrypt a message.
2. Enter the message.
3. Specify a shift value, an integer that determines how many positions each letter will shift.

### Example

**Encrypting a Message**:
- Input:
    ```
    Would you like to encrypt or decrypt? encrypt
    Enter your message: Hello
    Enter shift value: 3
    ```
- Output:
    ```
    Encrypted Message: Khoor
    ```

**Decrypting the Message**:
- Input:
    ```
    Would you like to encrypt or decrypt? decrypt
    Enter your message: Khoor
    Enter shift value: 3
    ```
- Output:
    ```
    Decrypted Message: Hello
    ```

## Code Overview

The project has two main functions:
1. `encrypt`: Shifts each letter forward by the specified shift amount.
2. `decrypt`: Shifts each letter backward by the specified shift amount.

The main driver function handles user input and calls either the `encrypt` or `decrypt` function based on the user’s choice.

## Limitations

- **Caesar Cipher Security**: This cipher is not secure by modern standards. It is mainly for educational purposes and introductory cryptography exploration.
- **Single Alphabet**: This implementation works with the English alphabet. Modifications would be needed for other languages.

## License

This project is open-source and free to use for educational purposes. Contributions and modifications are welcome.

## Acknowledgments

This project is inspired by one of the oldest cryptographic techniques and serves as a fun introduction to encryption and decryption in programming.

---

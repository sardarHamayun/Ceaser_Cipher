# Caesar Cipher GUI

This project is a simple graphical user interface (GUI) implementation of the Caesar Cipher encryption and decryption algorithm. The GUI is built using Python's `tkinter` library, allowing users to easily input text, specify a shift value, and choose between encryption and decryption modes.

## Features

- **Encrypt Text**: Input text and apply the Caesar Cipher to encrypt it using a specified shift value.
- **Decrypt Text**: Input encrypted text and apply the Caesar Cipher to decrypt it using a specified shift value.
- **Simple GUI**: User-friendly interface for easy interaction.

## Requirements

- Python 3.x
- `tkinter` library (comes pre-installed with standard Python distributions)

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/sardarHamayun/Ceaser_Cipher.git
    cd your-repo-name
    ```

2. **Run the Script**:
    ```sh
    python caesar_cipher_gui.py
    ```

## Usage

1. **Enter your text**: Type or paste the text you want to encrypt or decrypt into the text entry box.
2. **Enter shift value**: Input the numerical shift value to be used for the Caesar Cipher.
3. **Select mode**: Choose whether you want to encrypt or decrypt the text by selecting the appropriate radio button.
4. **Perform Cipher**: Click the "Perform Cipher" button to see the result displayed in the result box.

## Example

- **Encrypting**: 
    - Text: `HELLO`
    - Shift: `3`
    - Result: `KHOOR`

- **Decrypting**: 
    - Text: `KHOOR`
    - Shift: `3`
    - Result: `HELLO`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## Acknowledgments

- Inspired by the classic Caesar Cipher algorithm.
- Built with the help of Python's `tkinter` library.

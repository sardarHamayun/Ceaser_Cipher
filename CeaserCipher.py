import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            shift_amount = shift if mode == "Encrypt" else -shift
            if char.isupper():
                result += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            result += char

    return result

def perform_cipher():
    text = text_entry.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    mode = mode_var.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to encrypt or decrypt.")
        return

    if not shift.isdigit():
        messagebox.showwarning("Input Error", "Shift value must be a number.")
        return

    shift = int(shift)

    result = caesar_cipher(text, shift, mode)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, result)

# Set up the main application window
root = tk.Tk()
root.title("Caesar Cipher")

# Text entry for the message
tk.Label(root, text="Enter your text:").grid(row=0, column=0, padx=10, pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=0, column=1, padx=10, pady=5)

# Entry for the shift value
tk.Label(root, text="Enter shift value:").grid(row=1, column=0, padx=10, pady=5)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

# Radio buttons for selecting mode (Encrypt or Decrypt)
mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").grid(row=2, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").grid(row=2, column=1, padx=10, pady=5)

# Button to perform the cipher operation
cipher_button = tk.Button(root, text="Perform Cipher", command=perform_cipher)
cipher_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Text entry for the result
tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=5)
result_entry = tk.Text(root, height=5, width=40)
result_entry.grid(row=4, column=1, padx=10, pady=5)

# Start the main event loop
root.mainloop()

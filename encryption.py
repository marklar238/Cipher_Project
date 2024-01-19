import tkinter as tk
from caeser_cipher import caeser_cipher

def create_window(open_frequency_analysis_window):
    encryption_root = tk.Toplevel()
    encryption_root.title("Encryption")

    label_text = tk.Label(encryption_root, text="Enter Text:")
    label_text.pack()

    entry_text = tk.Entry(encryption_root)
    entry_text.pack()

    label_key = tk.Label(encryption_root, text="Enter Key (Shift):")
    label_key.pack()

    entry_key = tk.Entry(encryption_root)
    entry_key.pack()

    result_label = tk.Label(encryption_root, text="")
    result_label.pack()

    def on_encrypt():
        plaintext = entry_text.get()
        shift = int(entry_key.get())
        encrypted_text = caeser_cipher(plaintext, shift)
        result_label.config(text=f"Encrypted Text: {encrypted_text}")
        open_frequency_analysis_window(encrypted_text)

    encrypt_button = tk.Button(encryption_root, text="Encrypt", command=on_encrypt)
    encrypt_button.pack()


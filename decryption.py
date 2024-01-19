import tkinter as tk
from caeser_decipher import caeser_decipher


def create_window():
    def decrypt():
        ciphertext = entry_ciphertext.get()
        shift = int(entry_shift.get())
        decrypted_text = caeser_decipher(ciphertext, shift)
        label_result.config(text=f"Decrypted Text: {decrypted_text}")

    decryption_window = tk.Toplevel()
    decryption_window.title("Caesar Cipher Decryption")

    label_ciphertext = tk.Label(decryption_window, text="Enter Ciphertext:")
    label_ciphertext.pack()

    entry_ciphertext = tk.Entry(decryption_window)
    entry_ciphertext.pack()

    label_shift = tk.Label(decryption_window, text="Enter Shift Key:")
    label_shift.pack()

    entry_shift = tk.Entry(decryption_window)
    entry_shift.pack()

    button_decrypt = tk.Button(decryption_window, text="Decrypt", command=decrypt)
    button_decrypt.pack()

    label_result = tk.Label(decryption_window, text="")
    label_result.pack()

# This line is for testing purposes only. Remove or comment it out when integrating with the main application.
# create_window()

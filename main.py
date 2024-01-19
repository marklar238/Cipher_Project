import tkinter as tk
import encryption
import decryption
import frequency_analysis

def open_encryption_window():
    # This function will open the encryption window
    encryption.create_window(on_encryption)

def open_decryption_window():
    # This function will open the decryption window
    decryption.create_window()

def on_encryption(encrypted_text):
    # This function is called after encryption is done
    # and will open the frequency analysis window with the encrypted text
    frequency_analysis.create_window(encrypted_text)

root = tk.Tk()
root.title("Caesar Cipher Toolkit")

btn_encrypt = tk.Button(root, text="Open Encryption Window", command=open_encryption_window)
btn_encrypt.pack()

btn_decrypt = tk.Button(root, text="Open Decryption Window", command=open_decryption_window)
btn_decrypt.pack()

root.mainloop()

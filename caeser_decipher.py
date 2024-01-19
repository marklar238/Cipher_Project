def caeser_decipher(ciphertext, shift):
    """
    Decrypts the given text which was encrypted using the Caesar Cipher.

    Parameters:
    ciphertext (str): The text to decrypt.
    shift (int): The number of places the original text was shifted.

    Returns:
    str: The decrypted text.
    """
    decrypted_text = ""

    for char in ciphertext:
        # Check if character is an uppercase letter
        if char.isupper():
            # Reverse the shift and ensure it remains an uppercase letter
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)

        # Check if character is a lowercase letter
        elif char.islower():
            # Reverse the shift and ensure it remains a lowercase letter
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)

        # Non-alphabetical characters remain unchanged
        else:
            decrypted_text += char

    return decrypted_text

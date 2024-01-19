def caeser_cipher(text, shift):
    """
    Encrypts the given text using the Caesar Cipher.

    Parameters:
    text (str): The plaintext to encrypt.
    shift (int): The number of places to shift each letter.

    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift character and ensure it remains an uppercase letter
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)

        # Check if character is a lowercase letter
        elif char.islower():
            # Shift character and ensure it remains a lowercase letter
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)

        # Non-alphabetical characters remain unchanged
        else:
            encrypted_text += char

    return encrypted_text

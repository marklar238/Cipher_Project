import tkinter as tk
from frequency_analysis_functions import calculate_frequency, guess_key

def create_window(ciphertext):
    def analyze_and_guess():
        frequencies = calculate_frequency(ciphertext)
        guessed_shift, probability = guess_key(ciphertext, frequencies)
        label_result.config(text=f"Guessed Shift: {guessed_shift} (Probability: {probability:.2f}%)")
        # Additional code to display frequency analysis results can go here

    analysis_window = tk.Toplevel()
    analysis_window.title("Frequency Analysis and Key Guessing")

    label_ciphertext = tk.Label(analysis_window, text="Ciphertext:")
    label_ciphertext.pack()

    text_ciphertext = tk.Text(analysis_window, height=4, width=50)
    text_ciphertext.pack()
    text_ciphertext.insert(tk.END, ciphertext)
    text_ciphertext.config(state=tk.DISABLED)  # Make the text field read-only

    button_analyze = tk.Button(analysis_window, text="Analyze and Guess Key", command=analyze_and_guess)
    button_analyze.pack()

    label_result = tk.Label(analysis_window, text="")
    label_result.pack()

# This line is for testing purposes only. Remove or comment it out when integrating with the main application.
# create_window("your encrypted text here")

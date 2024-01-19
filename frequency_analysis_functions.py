def calculate_frequency(text):
    frequency = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
            total_letters += 1

    for char in frequency:
        frequency[char] = (frequency[char] / total_letters) * 100

    return frequency


def guess_key(ciphertext, frequencies):
    english_frequencies = {
        'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
        'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
        'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
        'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
        'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
        'z': 0.07
    }

    best_shift = 0
    best_match = 0

    for shift in range(26):
        match_score = 0
        for char, freq in frequencies.items():
            shifted_char = chr((ord(char) - shift - 97) % 26 + 97)
            match_score += abs(english_frequencies.get(shifted_char, 0) - freq)

        if match_score < best_match or shift == 0:
            best_match = match_score
            best_shift = shift

    probability = (1 - best_match / 100) * 100  # Simplified probability estimation
    return best_shift, probability

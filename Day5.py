def calculate_word_frequency(text):
    # Convert the text to lowercase to ensure case-insensitivity
    text = text.lower()
    
    # Replace punctuations with spaces and split text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_frequency = {}
    
    # Count the frequency of each word
    for word in words:
        word = word.strip(",.!?;:\"()[]{}")  # Remove punctuation from each word
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency


# Input text
text = input("Enter the text: ")

# Calculate word frequency
word_counts = calculate_word_frequency(text)

# Print word frequencies
print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

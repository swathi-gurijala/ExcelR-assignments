import re

def clean_text(text):
    # Remove special characters using regex and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return cleaned_text

# Test the function with the given input
test_input = 'Hello, World! Welcome to NLP 101.'
result = clean_text(test_input)
print("Original Text:", test_input)
print("Cleaned Text:", result)

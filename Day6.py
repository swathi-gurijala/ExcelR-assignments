import nltk
from nltk.corpus import stopwords
import spacy

# Download stopwords from NLTK
nltk.download('stopwords')

def process_text(text):
    # Load the English model from spaCy
    nlp = spacy.load("en_core_web_sm")
    
    # Convert text to lowercase using spaCy
    text_lower = " ".join([token.text.lower() for token in nlp(text)])
    
    # Remove stopwords using NLTK
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in text_lower.split() if word not in stop_words]
    
    return " ".join(filtered_words)

# Input text
text = input("Enter the text: ")

# Process text
processed_text = process_text(text)

# Display the result
print("\nProcessed Text:")
print(processed_text)

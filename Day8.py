#Text_Mining_Coding.py

import nltk

# Download necessary NLTK data
nltk.download('punkt')

def tokenize_text(paragraph):
    # Tokenize into sentences
    sentences = nltk.sent_tokenize(paragraph)
    
    # Tokenize into words
    words = nltk.word_tokenize(paragraph)
    
    return sentences, words

# Sample paragraph
paragraph = """Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence. 
It involves teaching machines to understand and generate human language."""

# Tokenize the paragraph
sentences, words = tokenize_text(paragraph)

# Display results
print("Tokenized Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

print("\nTokenized Words:")
print(words)

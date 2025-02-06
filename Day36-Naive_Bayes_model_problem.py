Coding Question on Naive Bayes Models
Write a Python program to perform text classification using a Naïve Bayes classifier (`MultinomialNB`) from `sklearn.naive_bayes`. 
Train the model using sample text data and predict the category of a given new text.
Example input:
    ["I love programming", "Python is great", "Machine learning is amazing"]


CODE:

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample text data and corresponding labels
texts = ["I love programming", "Python is great", "Machine learning is amazing",
         "I enjoy football", "Football is exciting", "I watch football matches"]

labels = ["Technology", "Technology", "Technology", "Sports", "Sports", "Sports"]  # Categories

# Convert text to numerical feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a Multinomial Naïve Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# Predict category for new input
new_text = ["I enjoy coding in Python"]
new_text_vectorized = vectorizer.transform(new_text)
predicted_category = classifier.predict(new_text_vectorized)

# Output the predicted category
print(f"Predicted Category: {predicted_category[0]}")

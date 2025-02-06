#Coding Question on Bag of Words TF-IDF Word Embeddings
#Write a Python program to convert a given text into a Bag of Words (BoW) representation using `CountVectorizer` from `sklearn.feature_extraction.text`. 
#Also, compute the TF-IDF representation using `TfidfVectorizer`.
#Example input:
    #["I love machine learning", "Machine learning is fun", "Deep learning is amazing"]

CODE:

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def bow_tfidf_representation(corpus):
    # Bag of Words (BoW) representation
    count_vectorizer = CountVectorizer()
    bow_matrix = count_vectorizer.fit_transform(corpus)
    
    print("Bag of Words Representation:")
    print(count_vectorizer.get_feature_names_out())
    print(bow_matrix.toarray())
    print("\n")
    
    # TF-IDF representation
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    
    print("TF-IDF Representation:")
    print(tfidf_vectorizer.get_feature_names_out())
    print(tfidf_matrix.toarray())

# Example input corpus
corpus = [
    "I love machine learning",
    "Machine learning is fun",
    "Deep learning is amazing"
]

bow_tfidf_representation(corpus)

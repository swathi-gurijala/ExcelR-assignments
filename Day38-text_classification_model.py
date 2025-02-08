from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
texts = [
    "Spam messages are annoying", 
    "I won a lottery", 
    "This is a normal message", 
    "Congratulations! You have won a prize", 
    "Meeting at 5 PM", 
    "Claim your free gift now",
    "Let's schedule a call for tomorrow"
]

# Corresponding labels (1 = Spam, 0 = Not Spam)
labels = [1, 1, 0, 1, 0, 1, 0]

# Convert text data into numerical format
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Initialize and train the Decision Tree model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Test new input messages
new_messages = ["Win a free vacation", "Team meeting at 3 PM"]
X_new = vectorizer.transform(new_messages)
y_new_pred = clf.predict(X_new)

for msg, pred in zip(new_messages, y_new_pred):
    label = "Spam" if pred == 1 else "Not Spam"
    print(f"'{msg}' -> {label}")

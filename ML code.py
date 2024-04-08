import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset (replace with your dataset)
texts = ["I love this movie", "This movie is great", "I hate this movie", "This movie is terrible"]
tags = ["positive", "positive", "negative", "negative"]

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Convert tags into numerical labels
tag_dict = {"positive": 1, "negative": 0}
y = np.array([tag_dict[tag] for tag in tags])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier (Naive Bayes classifier in this case)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

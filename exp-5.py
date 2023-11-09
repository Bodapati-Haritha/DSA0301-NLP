import nltk
from nltk.stem import PorterStemmer

# Download the NLTK data (if not already downloaded)
nltk.download('punkt')

# Create an instance of the PorterStemmer
porter_stemmer = PorterStemmer()

# Sample list of words
words = ["running", "easily", "jumps", "happily", "cats", "better"]

# Perform stemming on each word
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Print the original and stemmed words
print("Original words:", words)
print("Stemmed words:", stemmed_words)

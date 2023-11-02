import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download the necessary NLTK data if not already downloaded

# Sample text for analysis
text = "The quick brown foxes jumped over the lazy dogs. Jumper's jumping."

# Tokenize the text into words
words = word_tokenize(text)

# Initialize stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()

# Perform stemming using Porter Stemmer
porter_stems = [porter.stem(word) for word in words]

# Perform stemming using Lancaster Stemmer
lancaster_stems = [lancaster.stem(word) for word in words]

# Display the original words, Porter stems, and Lancaster stems
print("Original Words:", words)
print("Porter Stems:", porter_stems)
print("Lancaster Stems:", lancaster_stems)

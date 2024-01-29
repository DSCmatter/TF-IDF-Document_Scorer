import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob as tb

# Download NLTK resources (stopwords and tokenizer)
nltk.download('stopwords')
nltk.download('punkt')

# Function to calculate term frequency (TF) for a word in a document
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

# Function to count the number of documents containing a specific word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

# Function to calculate inverse document frequency (IDF) for a word in a list of documents
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

# Function to calculate TF-IDF score for a word in a document
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

# Function to read text from a file and return as a TextBlob
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return tb(file.read())

# Get the filename from the user
filename = input("Enter the filename: ")

# Read the contents of the file into a TextBlob
document = read_file(filename)

# Filter out stopwords from NLTK's English stopwords list
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in document.words.lower() if word not in stop_words]

# Create a new TextBlob with the filtered words
filtered_document = tb(' '.join(filtered_words))

# Create a list of TextBlob objects containing the filtered document
bloblist = [filtered_document]

# Print the top words in the document along with their TF-IDF scores
print("Top words in the document:")
scores = {word: tfidf(word, filtered_document, bloblist) for word in filtered_document.words}
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:3]:
    print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

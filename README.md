# TF-IDF
 TF-IDF ('Term frequency, Inverse Document Frequency) isa an algorithm or way to score the imporatance of words (or 'terms') based on how frequently they appear

 which means
 -If a word appears frequently in a document, it's important. Give the word a high score.
 -But if a word appears in many documents, it's not a unique identifier. Give the word a low score.

Prerequisites:
- You may need to install packages such as:
- textblob and nltk
- you can do this typing: pip install textblob on cmd
- same goes for nltk: pip install nltk

How does this word? 
- The code is commented for self explanatory purpose 

This is an improved version of usual TF-IDF code where:
- We use NLTK to download stopwords and tokenize the text.
 Stopwords are filtered out from the document before calculating TF-IDF scores.
 We lowercase the words to ensure case insensitivity.
 The TF-IDF scores are calculated based on the filtered document.
 The top words and their TF-IDF scores are printed as before.

You may have to enter the document file location 
- for example: E:\something\something.txt
- Two example text files have been given 

 For further reading 
 visit: https://stevenloria.com/tf-idf/

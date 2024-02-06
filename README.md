# TF-IDF
TF-IDF ('Term frequency, Inverse Document Frequency) is an algorithm or way to score the imporatance of words (or 'terms') based on how frequently they appear

 which means
 - If a word appears frequently in a document, it's important. Give the word a high score.
 - But if a word appears in many documents, it's not a unique identifier. Give the word a low score.

## Prerequisites:
- You may need to install packages such as:
- textblob and nltk
- you can do this typing: pip install textblob on cmd
- same goes for nltk: pip install nltk

## Improved TF-IDF Implementation
This implementation of TF-IDF features improvements such as:

- Utilizing NLTK to download stopwords and tokenize the text.
- Filtering out stopwords from the document before calculating TF-IDF scores.
- Lowercasing the words to ensure case insensitivity.
- Calculating TF-IDF scores based on the filtered document.

## Usage
- Ensure you have Python installed on your system.
- Install the required packages using pip as mentioned in the Prerequisites section.
- Clone or download this repository.
- Navigate to the directory containing the TF-IDF script.
- Run the script and follow the prompts to enter the location of the document file.

-The script will calculate the TF-IDF scores and display the top words along with their scores.

## Examples
Two example text files have been provided in the repository for testing the TF-IDF algorithm.

- text.txt
- text2.txt
## Further Reading
- For more information on TF-IDF and its applications, visit the following link:

- [TF-IDF Explained - Steven Loria](https://stevenloria.com/tf-idf/)

## License
- This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

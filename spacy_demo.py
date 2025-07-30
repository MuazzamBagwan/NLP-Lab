import spacy
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer

nlp = spacy.load('en_core_web_sm')
stemmer = PorterStemmer()

example_string = """
My name is Muazzam Bagwan. I am form Shrirampur. I am pursuing B.Tech in Information Technology at Sanjivani College of Engineering.
"""

doc = nlp(example_string)

sentences = [sent.text for sent in doc.sents]
print(sentences)

words = [token.text for token in doc if not token.is_punct]
print(words)

filtered_words = [token.text for token in doc if not token.is_punct and not token.is_stop]
print(filtered_words)

lemmatized_words = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
print(lemmatized_words)

stemmed_words = [stemmer.stem(token.text) for token in doc if not token.is_punct and not token.is_stop]
print(stemmed_words)
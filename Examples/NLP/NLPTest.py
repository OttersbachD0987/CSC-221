import nltk
import nltk.collections
import nltk.text
import nltk.data
import nltk.grammar
import nltk.util
import nltk.corpus
from nltk import word_tokenize, sent_tokenize
nltk.download('all', halt_on_error=False)

text: str = "I am a duck. Ducks can walk. Some swim, some don't."
words: list[str] = word_tokenize(text)
sentences: list[str] = sent_tokenize(text)

a = [b for c in ["aei", "gae", "bw"] for b in c]
print(a)
print(words)
words[:] = [word for word in words if word.lower() not in nltk.corpus.stopwords.words('english') and word not in nltk.PunktTokenizer.PUNCTUATION]
print(words)
print(sentences)
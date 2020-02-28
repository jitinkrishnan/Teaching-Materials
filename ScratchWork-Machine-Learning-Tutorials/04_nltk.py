############# NLTK AND STUFF ##############

import nltk
#nltk.download()

text = "The cow jumped over the moon 100 times. Some Doves and Pythons ."

# word tokens and frequency
tokens = [t for t in nltk.word_tokenize(text)]
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

# stop words
from nltk.corpus import stopwords
stopwords.words('english')

# sentence tokennse
sentences = nltk.sent_tokenize(text)

# synonyms and antonyms
from nltk.corpus import wordnet
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())

synonyms = []
for syn in wordnet.synsets('pain'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

antonyms = []
 
for syn in wordnet.synsets("small"):
 
    for l in syn.lemmas():
 
        if l.antonyms():
 
            antonyms.append(l.antonyms()[0].name())
 
print(antonyms)

### STEMMING AND LEMMATIZATION ##########

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing', pos="v")) #POS = VERB

##### PARTS OF SPEECH TAGGING ########
text = "the little yellow dog barked at the cat"

from nltk import pos_tag
pos_tag(nltk.word_tokenize(text))

from nltk import ne_chunk
ne_chunk(pos_tag(nltk.word_tokenize(text))).draw()
#print

grammar = r"""VP: {<VB.*>+(<VB.*>|<JJ.*>|<RB.*>)?}"""
chunk_parser = nltk.RegexpParser(grammar)
tagged_sentence = nltk.pos_tag(text.split())
chunk = chunk_parser.parse(tagged_sentence)
for subtree in chunk.subtrees():
	print(subtree)

######## bigrams and trigrams
bigrm = list(nltk.bigrams(text.split()))

######### TWEET TOKENIZER ##########
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
tknzr.tokenize(text)

############ URLS - get raw data##########################
from bs4 import BeautifulSoup
import urllib.request

url = "https://www2.gmu.edu/admissions-aid/visit-mason"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
#### TF IDF EXAMPLE ########

import pandas as pd
from pandas import read_csv
import re
import emoji, itertools

def preprocess(text):
    # URLs
    sentence = re.sub(r'http\S+', ' ', text)
    
    # emoji
    for c in sentence:
        if c in emoji.UNICODE_EMOJI:
            sentence = re.sub(c, emoji.demojize(c), sentence)
    
    sentence = re.sub("([!]){1,}", " ! ", sentence)
    sentence = re.sub("([.]){1,}", " . ", sentence)
    sentence = re.sub("([?]){1,}", " ? ", sentence)
    sentence = re.sub("([;]){1,}", " ; ", sentence)
    sentence = re.sub("([:]){2,}", " : ", sentence)
    
    # numerical values
    #sentence = re.sub("[-+]?[.\d]*[\d]+[:,.\d]*", " <NUMBER> ", sentence)
    
    # convert words such as "goood" to "good"
    sentence = ''.join(''.join(s)[:2] for _, s in itertools.groupby(sentence))
    
    # convert to lower case
    #words = tknzr.tokenize(sentence)
    words = sentence.split()
    
    # remove stop words
    #stop = stopwords.words("english")
    #words = [word for word in words if word not in stop]
    
    # remove words less than or equal to 2 letters and non-aphabetical
    #words = [word for word in words if len(word) > 2 and word.isalpha()]

    words = ["<number>" if word.isdigit() else word for word in words]
    #words = [word for word in words if len(word) > 1]
    words = [word if word[0] != '#' else word[1:] for word in words]
    words = [word for word in words if word.strip() != ""]
    words = [word for word in words if word[0] != '@']
    
    if sentence[:3] == 'RT ':
        words = words[1:]
        words.append("<rt>")
    
    #words = [word for word in words if len(word) > 1]
        
    
    sentence =  " ".join(words)
    
    sentence = re.sub('[^ a-zA-Z0-9.!?:;<>_#@]', ' ', sentence)
    sentence = re.sub('\s+', ' ', sentence)
    
    
    return sentence

df = pd.DataFrame(pd.read_csv("train_emoji.csv", sep = ',', encoding = "ISO-8859-1", index_col=0, names=["tag", "id", "date", "query", "user", "text"])) # use \t in case of TSV
df = pd.DataFrame(pd.read_csv("train_emoji.csv", sep = ',', encoding = "ISO-8859-1"))

df['processed_text'] = ''

for index, row in df.iterrows():
	df.at[index, 'text'] = preprocess(row['text'])

#df['processed_text'] = df.apply(lambda row: preprocess(row['text']),axis=0)

#######################

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

## SPLIT


###### train 
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
#tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
#X_train_tf = tf_transformer.transform(X_train_counts)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X_train_tfidf, Y_train)

### TEST
X_new_counts = count_vect.transform(X_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
y_pred = clf.predict(X_new_tfidf)

X_new_counts = count_vect.transform(list(X_train))
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
y_pred_train = clf.predict(X_new_tfidf)

print("---- TFIDF + Logisitc Regression-")
print('Training accuracy %s' % round(accuracy_score(Y_train, y_pred_train),3))
print('Training F1 score: {}'.format(round(f1_score(Y_train, y_pred_train, average='weighted'),3)))
print('Testing accuracy %s' % round(accuracy_score(Y_test, y_pred),3))
print('Testing F1 score: {}'.format(round(f1_score(Y_test, y_pred, average='weighted'),3)))
print("-----------------------------------")

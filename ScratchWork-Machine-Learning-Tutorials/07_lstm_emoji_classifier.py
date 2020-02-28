import numpy as np
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform
import csv, emoji

def read_csv(filename = None):
    phrase = []
    emoji = []

    with open (filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        for row in csvReader:
            phrase.append(row[0])
            emoji.append(row[1])

    X = np.asarray(phrase)
    Y = np.asarray(emoji, dtype=int)

    return X, Y

emoji_dictionary = {"0": "\u2764\uFE0F",    # :heart: prints a black instead of red heart depending on the font
                    "1": ":baseball:",
                    "2": ":smile:",
                    "3": ":disappointed:",
                    "4": ":fork_and_knife:"}

def label_to_emoji(label):
    """
    Converts a label (int or string) into the corresponding emoji code (string) ready to be printed
    """
    return emoji.emojize(emoji_dictionary[str(label)], use_aliases=True)

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)]
    return Y

def read_glove_vecs(glove_file):
    with open(glove_file, 'r') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
        
        i = 1
        words_to_index = {}
        index_to_words = {}
        for w in sorted(words):
            words_to_index[w] = i
            index_to_words[i] = w
            i = i + 1
    return words_to_index, index_to_words, word_to_vec_map

def sentences_to_indices(X, word_to_index, max_len):
	m = X.shape[0]
	X_indices = np.zeros((m,max_len))
	for i in range(m):
		sentence_words = (X[i].lower()).split()
		j = 0
		for w in sentence_words:
			X_indices[i,j] = word_to_index[w]
			j = j +1
	return X_indices

def pretrained_embedding_layer(word_to_vec_map, word_to_index, emb_dim):
	vocab_len = len(word_to_index) + 1
	emb_matrix = np.zeros((vocab_len,emb_dim))
	for word, index in word_to_index.items():
		emb_matrix[index, :] = word_to_vec_map[word]
	embedding_layer = Embedding(vocab_len, emb_dim, trainable = False)
	embedding_layer.build((None,))
	embedding_layer.set_weights([emb_matrix])
	return embedding_layer

def model(input_shape, word_to_vec_map, word_to_index):
	sentence_indices = Input(shape = input_shape, dtype = 'int32')
	embedding_layer = pretrained_embedding_layer(word_to_vec_map, word_to_index, 50)
	embeddings = embedding_layer(sentence_indices) 
	X = LSTM(128, return_sequences=True)(embeddings)
	X = Dropout(0.5)(X)
	X = LSTM(128, return_sequences=False)(X)
	X = Dropout(0.5)(X)
	X = Dense(5)(X)
	X = Activation('softmax')(X)
	model = Model(inputs=sentence_indices, outputs=X)
	return model

X_train, Y_train = read_csv('data/train_emoji.csv')
X_test, Y_test = read_csv('data/test_emoji.csv')
maxLen = len(max(X_train, key=len).split())
word_to_index, index_to_word, word_to_vec_map = read_glove_vecs('data/glove.6B.50d.txt')

X_train_indices = sentences_to_indices(X_train, word_to_index, maxLen)
Y_oh_train = convert_to_one_hot(Y_train, C = 5)
Y_oh_test = convert_to_one_hot(Y_test, C = 5)

model = model((maxLen,), word_to_vec_map, word_to_index)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train_indices, Y_oh_train, epochs = 50, batch_size = 32, shuffle=True)

X_test_indices = sentences_to_indices(X_test, word_to_index, max_len = maxLen)
loss, acc = model.evaluate(X_test_indices, Y_oh_test)
print("Test accuracy = ", acc)

while True:
	s = str(input('Enter something about love, baseball, how you feel, or food: '))
	x_test = np.array([s])
	X_test_indices = sentences_to_indices(x_test, word_to_index, maxLen)
	print(x_test[0] +' '+  label_to_emoji(np.argmax(model.predict(X_test_indices))))


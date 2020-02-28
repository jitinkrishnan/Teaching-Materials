###### WORD VECTORS #######

def read_glove_vecs(glove_file):
    with open(glove_file, 'r') as f:
        words = set()
        word_to_vec_map = {}
        
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)

words, word_to_vec_map = read_glove_vecs('glove.6B.50d.txt')


######## NUMPY ##########
import numpy as np

dot = np.dot(u,v)
norm_u = np.sqrt(np.sum(u*u))
norm_v = np.sqrt(np.sum(v*v))
cosine_similarity = dot / (norm_u * norm_v)

father = word_to_vec_map["father"]
mother = word_to_vec_map["mother"]
ball = word_to_vec_map["ball"]
crocodile = word_to_vec_map["crocodile"]
france = word_to_vec_map["france"]
italy = word_to_vec_map["italy"]
paris = word_to_vec_map["paris"]
rome = word_to_vec_map["rome"]

print("cosine_similarity(father, mother) = ", cosine_similarity(father, mother))
print("cosine_similarity(ball, crocodile) = ",cosine_similarity(ball, crocodile))
print("cosine_similarity(france - paris, rome - italy) = ",cosine_similarity(france - paris, rome - italy))

############### GENERATING X AND Y ############

def convert_to_one_hot(Y, C):
    Y = np.eye(C)#[Y.reshape(-1)]
    return Y

convert_to_one_hot(np.array(Y_train),5)


def sentence_to_avg(sentence, word_to_vec_map, dim):
    
	words = sentence.split()
    
    # Initialize the average word vector, should have the same shape as your word vectors.
    avg = np.zeros(dim)
    
    # average the word vectors. You can loop over the words in the list "words".
    count = 0
    for w in words:
        try:
            avg += word_to_vec_map[w]
            count += 1
        except:
            continue
    
    if count == 0 :
        return avg
    avg = avg/len(words)
    
    return avg
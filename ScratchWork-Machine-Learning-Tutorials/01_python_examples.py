################ STRINGS IN PYTHON ##################
para = "The cow jumped over the moon 100 times. Some Doves and Pythons ."
# get words
words = para.split()
# get characters
list(words[0])
# get sentences
sentences = para.split(".")
# lowercase
print(words[0].lower())
# uppercase
print(sentence[0].upper())
# check if alpha
print(word[0].isalpha())
#check if digit
print(word[0].isdigit())
# list comprehension
lower_words = [word.lower() for word in words]
alphas = [word if word.alpha() else "<empty>" for word in words]
sentence_matrix = [sent.split() for sent in para.split(".")]
# split list
words = words[1:3]
words[-3:] # last 3
# sort list
sorted(words) # ascii
# reverse list
list(reversed(words))
# join words
sentence = " ".join(words)
# append vs extend
[1,2,3].append([4,5,6])
[1,2,3].extend([4,5,6])
# type checking
type(word) == str

# http://pythontutor.com




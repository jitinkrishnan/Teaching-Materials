############# REGULAR EXPRESSIONS ############
# https://docs.python.org/3/library/re.html


import re
tweet = "Hello there, my goood friend. I wouldn't watch 10 movies a weeek... @user1034_bug #hastag http://www.stuff.com"

############################## FINDALL
# words
re.findall('\w+',tweet)

# numbers
re.findall('\d',tweet)

# find adverbs
text = "He was carefully disguised but captured quickly by police."
re.findall(r"\w+ly", text)

m = re.search(r'jitin', 'ffaffadfjitinfaffa')
m.start
m.end

############################## SPLIT
# split by space
re.split('\s',tweet)

# split by multiple
re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

# split by everything except
re.split('[^ a-zA-Z0-9.!?:;<>_#@]', tweet)

############################## SUB

# cut URL 
tweet = re.sub(r'http\S+', ' <URL> ', tweet)

# leading periods
tweet = re.sub("([.]){1,}", " . ", tweet)

# whatever you need
tweet = re.sub('[^ a-zA-Z0-9.!?:;<>_#@]', ' ', tweet)

# extra spaces
tweet = re.sub('\s+', ' ', tweet)

################ extra 000s
import itertools
tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

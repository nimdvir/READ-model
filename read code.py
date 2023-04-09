import re
import nltk
import syllables
# from nltk.book import *
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
import matplotlib.pyplot as plt
from wordfreq import zipf_frequency
from wordfreq import word_frequency
import csv 
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob, Word
#import syllapy
from nltk.corpus import cmudict
import textstat
from itertools import chain

d = cmudict.dict()    
def syllable_count(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    except KeyError:
        #if word not found in cmudict
        return syllapy.count(word)

def str_ext(user_input):
## Extract only the string characters from the input
## Display the extraction in lowercase  .lower()
## for letter in user_input:
##    need to keep output type str not type list
    user_output = str(re.findall("[a-zA-Z]+", user_input))
## concantenated 3 lines w/ 1
    user_output = user_output.lower().replace(",","").replace("'", "")
    #user_output=user_output.replace(",","").replace("'", "")
    return user_output

def stringext(txtIn):
    txtIn = txtIn.lower() #this takes what is stored in txtIn and makes it all lower case
    txtIn = re.findall('[a-z]+',txtIn) #this looks at what is stored in txtIn and takes out only the lower cased alpha characters and stores them as seperate words.
    txtOut = ' '.join(txtIn) #this takes the seperate words string and joins them with a space in between and stores it as txtOut
    return(txtOut) #this prints out the value of txtOut

def word_count(user_input):
    counts = dict()
    user_input = user_input.lower()
    #wordslist = user_input.split()
    wordslist = re.findall('[a-z]+',user_input)
    for word in wordslist:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sort_counts = sorted(counts.items(), key=lambda x: x[1])
    #sort_counts = dict(sort_counts)
    return sort_counts

def word_counter(user_input,counts):
    user_input = user_input.lower()
    #wordslist = user_input.split()
    wordslist = re.findall('[a-z]+',user_input)
    for word in wordslist:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sort_counts = sorted(counts.items(), key=lambda x: x[1])
    #sort_counts = dict(sort_counts)
    return sort_counts

def syl_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if (word[0] in vowels):
        count += 1
    for index in range(1, len(word)):
        if ((word[index] in vowels) and (word[index - 1] not in vowels)):
            count += 1
            if (word.endswith("e")):
                count -= 1
    if (count == 0):
        count += 1
    return count

def fdist(text):
    fdist1 = FreqDist(text)
    text_set= set(text)
    for x in text_set:
        print (x, ' - ', fdist1[x])
    fdist1.plot(50, cumulative=True)
    return fdist1

def dict_plot(x):
    names = x.keys()
    vals = x.values()
    plt.plot(names, vals)
    plt.show


def syno(w):
    synonyms=[]
    syns = wn.synsets(w)
    for x in syns:
        print('synset : ', x.name() , '\n')
        print('definitipn: ', x.definition(), '\n')
        print('example: ', x.examples(), '\n')
        print('lemmas: ')
        lem = x.lemmas()
        for l in x.lemmas():
             synonyms.append(l.name())
             print(l.name())
    print(set(synonyms),end="\n")
    return (set(synonyms))

def wnwords():
    counts = dict()
    for w in list(wn.words()):
        w.lower()
        #wordslist = user_input.split()
        wordslist = re.findall('[a-z]+',w)
        for word in wordslist:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    f = open("wn-words.txt", "a")
    for x in counts:
        f.write(x)
        f.write(" - ")
        f.write(str(counts[x]))
        f.write("\n")
    f.close()

def read_score(word):
    read = dict()
    read['word'] = str(word)
    syns = wn.synsets(word)
    read['rs'] = len(syns)
    read['e-swn-pos'] = 0
    read['e-swn-neg'] = 0
    if read['rs'] > 0 :
        for s in syns:
            swn_synset = swn.senti_synset(s.name())
            escore = [swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]
            if len(escore) == 3:
                read['e-swn-pos'] += escore[0]
                read['e-swn-neg'] += escore[1]
        read['e-swn-pos'] = read['e-swn-pos'] / read['rs']
        read['e-swn-neg'] = read['e-swn-neg'] / read['rs']
    read['e-swn-emo'] = read['e-swn-pos'] + read['e-swn-neg']
    read['as'] = syl_count(word)
    read['dfr'] = word_frequency(word, 'en')
    read['dzi'] = zipf_frequency(word, 'en')

def get_hyponyms(word):
    hyponyms = []
    syns = wn.synsets(word)
    for synset in syns:
        for hyponym in synset.hyponyms():
            hyponyms.append(hyponym.lemma_names())
            
    return(hyponyms)

def get_hypernyms(word):
    hypernyms = []
    syns = wn.synsets(word)
    for synset in syns:
        for hypernym in synset.hypernyms():
            hypernyms.append(hypernym.lemma_names())
            
    return(hypernyms)       
            
    #for i in read:
    #    print(read[i])
    return read

def createwnlist():
    with open('wnlist.csv', newline='') as csvfile:
        mydict = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            read = read_score(row['word'])
            read['ra'] = row['ra']
            read['al'] = row['al']
            mydict.append(read)
    with open('wnlist4.csv', 'w') as csvfile:
        x=mydict[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=x)
        writer.writeheader()
        writer.writerows(mydict)

def stemlem():
    lemmatizer = WordNetLemmatizer()
    text = '1'
    while text != '0':
        text = str(input('enter words or 0 to break: '))
        words = text.split()
        for word in words:
            print(word, ' - ',lemmatizer.lemmatize(word.lower()))

def lemmatize_with_postag():
    text = '1'
    while text != '0':
        text = str(input('enter words or 0 to break: '))
        sent = TextBlob(text)
        tag_dict = {"J": 'a', 
                    "N": 'n', 
                    "V": 'v', 
                    "R": 'r'}
        words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]    
        lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
        x = " ".join(lemmatized_list)
        print(x)

def allsynonyms(word):
    synonyms = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms
    

def countsyll(word):
    syllables.estimate(word)

def complexity (word):
    compx = dict()
    compx['flesch_reading_ease'] = textstat.flesch_reading_ease(word)
    compx['textstat.reading_time'] = textstat.reading_time(word, ms_per_char=14.69)
    compx['difficult_words']= textstat.difficult_words(word)
    return compx

def synsets(word):
    syns = []
    syns = wn.synsets(word)
    return syns

def hypo (word):
    s = {}
    for i,j in enumerate(wn.synsets(word)):
#print "Meaning",i, "NLTK ID:", j.name()
        s["Hypernyms"] = " ".join(list(chain(*[l.lemma_names() for l in j.hypernyms()])))
        s["Hyponyms"]= " ".join(list(chain(*[l.lemma_names() for l in j.hyponyms()])))
        print ("Hypernyms:", ", ".join(list(chain(*[l.lemma_names() for l in j.hypernyms()]))))
        print ("Hyponyms:", ", ".join(list(chain(*[l.lemma_names() for l in j.hyponyms()]))))
    return s
   
def fillworddict():
    input_string = 1
    wordlist = {}
    while input_string is not 0:
        input_string = input("Enter a list element separated by space:\n")
        listwords = []
        listwords = input_string. splitlines()
        print (listwords)
        for i in listwords:
            wordlist[i] = {}
        x = input("enter 1 to stop or 0 to go more:")
    return wordlist

wordlist = {}
x= []
inputstring = 1
while inputstring is not "0":
    inputstring = input("Enter a list element separated by space:\n")
    if inputstring == "0":
        break
    else: 
        x = inputstring.split()
        
        
       # wordlist[inputstring] = {}
for i in x:
    z = synsets(i)
    wordlist[i].update({"word": i})
    wordlist[i].update({"synsets": len(z)})
    wordlist[i].update(complexity(i))
    
    z = get_hyponyms(i)
    wordlist[i].update({"hyponyms": len(z)})
    z = get_hypernyms(i)
    wordlist[i].update({"hypernyms": len(z)})
    wordlist[i].update({"synonyms": len(allsynonyms(i))})
    #print(i," - ", get_hyponyms(i), len()
for key, value in wordlist.items():
    print (value.keys())
    print (value.values())
    
print(wordlist)
#s = dict(fillworddict())
#print(s)














    

import distance
import time
import sys
import fuzzy

DICTIONARY = "words"
TARGET = sys.argv[1]
MAX_COST = int(sys.argv[2])

# read dictionary file
words = open(DICTIONARY, "rt").read().split('\n')

print(sys.getsizeof(words))

def search(word, max_cost):
    results=[]
    for w in words:
        cost = distance.levenshtein(word, w)
        if cost<= max_cost:
            results.append(w)
    
    return results

start = time.time()

w = fuzzy.DMetaphone()
wa = fuzzy.nysiis('Wade')
v=  fuzzy.nysiis('Wawadi')
print(wa)
print(v)

end = time.time()
print( "Search took %g s" % (end - start))

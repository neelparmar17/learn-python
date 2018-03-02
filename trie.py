#python code for insert and search in trie
import time
import csv

keys = []
with open('convertcsv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ' ', quotechar = '"')
    for row in spamreader:
        word= row[0] + row[1]
        
        keys.append(word.lower())

class TrieNode:
    #trie node class
    def __init__(self):
        self.children = [None]*26

        #isEndOfWord is true if the word is present
        self.isEndOfWord = False

class Trie:
    #Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        #returns new trie node 
        return TrieNode()
    
    def _charToIndex(self, ch):
        #private helper function
        #converts key current character into index
        #use only 'a' to 'z' and only lowercase letters
        return ord(ch)-ord('a')
    
    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
        
    def search(self, key):
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl != None and pCrawl.isEndOfWord
    

def main():
    # Input keys (use only 'a' through 'z' and lower case)
    output = ["Not present in trie",
              "Present in tire"]
    
    #trie object
    t = Trie()
    data = []
    start = time.time()
    for key in keys:
        data.append(key)
    end = time.time()
    print(len(data))
    #construct trie tree
    start = time.time()
    print( "array Insert took %g s" % (end - start))
    for key in keys:
        t.insert(key)
    end = time.time()

    print( "Insert took %g s" % (end - start))

    start = time.time()
    print("{} ---- {}".format("oramalone",output[t.search("oramalone")]))
    end = time.time()
    print( "search took %g s" % (end - start))
    start = time.time()
    print("oramalone" in data)
    end = time.time()
    print( " array search took %g s" % (end - start))
    print("{} ---- {}".format("marily",output[t.search("marily")]))
    print("{} ---- {}".format("darnell",output[t.search("darnell")]))
    print("{} ---- {}".format("zacker",output[t.search("zacker")]))

if __name__ == '__main__':
    main()
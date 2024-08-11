'''
Tries

These are also known as prefix trees.

They are a type of tree / graph that is 
specifically used for finding out if prefixes to words exist.

searching for words is also done but a simple search without
prefix considerations would be quicker with a hashmap
'''

class TrieNode: 

    def __init__(self):
        self.children = {}
        self.end = False


class Trie: 

    def __init__(self): 
        self.root = TrieNode()

    def insert(self, word:str) -> None: 
        cur = self.root

        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode() 
            cur = cur.children[c]
        cur.end = True
    
    def search(self, word:str) -> bool: 
        cur = self.root

        for c in word: 
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        return cur.end
    
    def is_prefix(self,prefix:str) -> bool:
        cur = self.root

        for c in prefix: 
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        return True

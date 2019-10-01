class Trie(object):

    def __init__(self):
        """
        Represents root node.
        """
        self.sons = {}
        self.val = None
        self.mark = False  # means a word ends there

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        for char in word:
            if char not in self.sons:
                self.sons[char] = Trie()
                if self.val:
                    self.sons[char].val = self.val + char
                else:
                    self.sons[char].val = char
            self = self.sons[char]
        self.mark = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        for char in word:
            if char in self.sons:
                self = self.sons[char]
            else:
                return False
        return self.mark

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for char in prefix:
            if char in self.sons:
                self = self.sons[char]
            else:
                return False
        return True

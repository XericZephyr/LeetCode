


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}


class Trie(object):

    STOP_SYMBOL = '#'

    def __init__(self):
        self.root = TrieNode()
        self.root.children[self.STOP_SYMBOL] = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.children[self.STOP_SYMBOL] = TrieNode()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return self.STOP_SYMBOL in node.children

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c, None)
        return True

if __name__ == '__main__':
    trie = Trie()
    print trie.search("")
    trie.insert("something")
    print trie.search("some")
    print trie.search("something")
    print trie.startsWith("some")
    trie.insert("some")
    print trie.search("some")
    trie.insert("key")
    print trie.search("key")
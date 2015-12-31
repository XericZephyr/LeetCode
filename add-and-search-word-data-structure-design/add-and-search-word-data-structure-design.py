
class TrieNode(object):

    def __init__(self):
        self.children = {}


class WordDictionary(object):

    STOP_SYMBOL = '#'

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        self.root.children[self.STOP_SYMBOL] = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(self.root, word)]
        # DFS
        while stack:
            node, word = stack.pop()
            if not word:
                if self.STOP_SYMBOL in node.children:
                    return True
                continue
            if word[0] == '.':
                for c in node.children:
                    if node.children[c] != self.STOP_SYMBOL:
                        stack.append((node.children[c], word[1:]))
            elif word[0] in node.children:
                stack.append((node.children[word[0]], word[1:]))
        return False

if __name__ == '__main__':
    d = WordDictionary()
    d.addWord("abcde")
    print d.search("abcde")
    print d.search("ab.de")
    print d.search(".....")
    print d.search("....")
    print d.search("")


# coding:utf8


class Trie:
    """
        实现一个字典树
        https://leetcode-cn.com/problems/implement-trie-prefix-tree/
    """

    def __init__(self):
        self.root = {}
        self.end_mark = '#'
    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end_mark] = self.end_mark

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_mark in node


    def startWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.search('apple'); 

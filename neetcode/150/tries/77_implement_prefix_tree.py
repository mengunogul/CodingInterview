from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.endOfWord: bool = False


class PrefixTree:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        curr_node.endOfWord = True

    def search(self, word: str) -> bool:
        curr_node: TrieNode = self.root
        for ch in word:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return curr_node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr_node: TrieNode = self.root
        for ch in prefix:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return True

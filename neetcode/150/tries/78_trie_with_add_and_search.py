from collections import deque
from typing import Dict, Deque, Tuple


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.endOfWord: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        cur: TrieNode = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        q: Deque[Tuple[TrieNode, int]] = deque()
        q.append((self.root, 0))
        while q:
            cur, idx = q.popleft()
            if idx == len(word):
                if cur.endOfWord:
                    return True
                continue

            if word[idx] == ".":
                for key in cur.children.keys():
                    q.append((cur.children[key], idx + 1))
            elif word[idx] in cur.children:
                q.append((cur.children[word[idx]], idx + 1))
        return False

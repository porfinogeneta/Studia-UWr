from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word_end = False

    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, tokens: List[str]) -> None:
        current = self.root
        for token in tokens:
            current = current.children[token]
        current.is_word_end = True
    
    def traverse_dfs(self, current: TrieNode, word: str):
        if current.is_word_end:
            print(word)
        for token, children in current.children.items():
            self.traverse_dfs(children, f"{word} {token}")
    
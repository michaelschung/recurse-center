# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = []

    def __repr__(self):
        return self.val

    def add_child(self, val):
        self.children.append(Node(val))

    def has_child(self, val):
        for child in self.children:
            if child.val == val:
                return True
        return False
    
    def get_child(self, val):
        for child in self.children:
            if child.val == val:
                return child
        return None

class WordDictionary:
    def __init__(self):
        self.root = Node('')

    def repr_helper(self, curr):
        if not curr:
            return ''
        text = curr.val + f' {'END' if curr.is_end else ''} '
        for child in curr.children:
            text += self.repr_helper(child)
        return text

    def __repr__(self):
        return self.repr_helper(self.root)

    def addWordHelper(self, curr, word):
        if not word:
            curr.is_end = True
            return
        # print(f'ADDING {word[0]} TO {curr.val}')
        first = word[0]
        if not curr.has_child(first):
            curr.add_child(first)
        self.addWordHelper(curr.get_child(first), word[1:])

    def addWord(self, word: str) -> None:
        # print('ADDING WORD:', word)
        self.addWordHelper(self.root, word)

    def searchHelper(self, curr, word):
        if not word and curr.is_end:
            return True
        if not word:
            return False
        # print('='*20)
        # print('CURRENT LETTER:', curr.val)
        # print('CURRENT CHILDREN:', curr.children)
        # print('CURRENT SEARCH:', word)
        first = word[0]
        if curr.has_child(first):
            return self.searchHelper(curr.get_child(first), word[1:])
        if first == '.':
            for child in curr.children:
                if self.searchHelper(child, word[1:]):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
print(obj.search('a'))
print(obj.search('.at'))
obj.addWord('bat')
print(obj.search('.at'))
print(obj.search('an.'))
print(obj.search('a.d.'))
print(obj.search('b.'))
print(obj.search('a.d'))
print(obj.search('.'))
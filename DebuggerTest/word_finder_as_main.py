class WordFinder:
    def __init__(self, word_list: list[str]):
        self.word_list = word_list

    def find_word(self, target_word: str):
        for i in range(len(self.word_list)):
            word = self.word_list[i]
            if word == target_word:
                return i
            return -1


if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    finder = WordFinder(words)

    assert finder.find_word("cherry") == 2, f'Expected 2, but got {finder.find_word("cherry")}'
    assert finder.find_word("date") == 3, f'Expected 3, but got {finder.find_word("date")}'
    assert finder.find_word("kiwi") == -1, f'Expected -1, but got {finder.find_word("kiwi")}'

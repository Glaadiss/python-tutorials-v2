class WordFinder:
    def __init__(self, word_list: list[str]):
        self.word_list = word_list

    def find_word(self, target_word: str):
        for i in range(len(self.word_list)):
            word = self.word_list[i]
            if word == target_word:
                return i
            return -1

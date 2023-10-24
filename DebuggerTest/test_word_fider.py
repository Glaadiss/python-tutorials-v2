from .word_finder import WordFinder


def test_word_finder():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    finder = WordFinder(words)

    assert finder.find_word("cherry") == 2, f'Expected 2, but got {finder.find_word("cherry")}'
    assert finder.find_word("date") == 3, f'Expected 3, but got {finder.find_word("date")}'
    assert finder.find_word("kiwi") == -1, f'Expected -1, but got {finder.find_word("kiwi")}'

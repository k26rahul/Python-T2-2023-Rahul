class Word:
    count = 0

    def __init__(self, word, pos):
        Word.count += 1
        self.word = word
        self.pos = pos

    def print_info(self):
        print(
            f'The word is "{self.word}" and its part of speech is "{self.pos}".')


word = Word(input(), input())
word.print_info()

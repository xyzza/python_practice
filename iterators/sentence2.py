import re
import reprlib
from test import tests

RE_WORD = re.compile('\w+')

class Sentence:
    # This is Iterable

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    # This is Iterator

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):

        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return word

    def __iter__(self):
        # for issubclass(SentenceIterator, abc.Iterator)
        return self

tests(Sentence)
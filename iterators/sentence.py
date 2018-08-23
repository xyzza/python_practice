import re
import reprlib
from test import tests

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        pass

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


tests(Sentence)
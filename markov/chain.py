import json
import random


class BaseChain(object):

    def grow(self, words):
        """Seeds the Markov chain with a new sentence.

        words: the words in a sentence, a list of strings.
        """
        pass

    def generate(self):
        """Generates a new sentence using the Markov chain. Returns a list of
        strings.
        """
        pass


class Chain(BaseChain):

    def __init__(self):
        self.words = []
        self.associations = {}

    def _add_word(self, word):
        """Returns an index of an existing word or adds a new one and returns
        its new index.

        word: a string.
        """
        try:
            return self.words.index(word)
        except ValueError:
            self.words.append(word)
            return len(self.words) - 1

    def _add_association(self, i, j):
        """Adds an association from the word with an index i to the word with
        an index j. Those parameters can be None to indicate the beginning or
        end of the sentence.
        """
        if not i in self.associations:
            self.associations[i] = []

        found = False
        for entry in self.associations[i]:
            if entry[0] == j:
                entry[1] += 1
                found = True
                break
        if not found:
            self.associations[i].append([j, 1])

    def save(self, path):
        """Saves this chain in a file."""
        data = {
            'words': self.words,
            'associations': self.associations,
        }
        with open(path, 'w') as f:
            json.dump(data, f)

    def grow(self, words):
        """Grows this chain using the provided words. The words should form
        a single complete sentence.

        words: list of strings.
        """
        prev = None
        for word in words:
            i = self._add_word(word)
            self._add_association(prev, i)
            prev = i
        self._add_association(prev, None)

    def generate(self):
        """Generate a sequence of words."""
        sentence = []
        prev = None
        while True:
            total = sum([entry[1] for entry in self.associations[prev]])
            selected = random.randint(0, total)

            i = 0
            for entry in self.associations[prev]:
                i += entry[1]
                if i >= selected:
                    if entry[0] is None:
                        return sentence
                    else:
                        sentence.append(self.words[entry[0]])
                        prev = entry[0]
                    break


def load(path):
    """Loads a chain previously saved with Chain.save."""
    with open(path, 'r') as f:
        data = json.load(f)
    words = data['words']
    associations = {}
    for key, value in data['associations'].items():
        if key == 'null':
            associations[None] = value
        else:
            associations[int(key)] = value

    rv = Chain()
    rv.words = words
    rv.associations = associations
    return rv

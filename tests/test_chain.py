import os
from markov import Chain, load


s1 = ['Ala', 'ma', 'kota']
s2 = ['Jasiek', 'ma', 'pieska']


def test_grow():
    c = Chain()

    c.grow(s1)
    for w in s1:
        assert w in c.words
    assert len(c.words) == 3

    c.grow(s2)
    for w in s2:
        assert w in c.words
    assert len(c.words) == 5


def test_save(tmp_file):
    c = Chain()
    c.grow(s1)
    c.grow(s2)

    c.save(tmp_file)
    c = load(tmp_file)
    
    for i in range(10):
        print('%s.' % ' '.join(c.generate()))


def test_generate():
    c = Chain()
    c.grow(s1)
    c.grow(s2)

    for i in range(10):
        print('%s.' % ' '.join(c.generate()))

def test_generate_rms():
    c = Chain()

    d = os.path.dirname(__file__)
    filename = os.path.join(d, 'files/rms.txt')
    with open(filename, 'r') as f:
        content = f.read()
    for sentence in content.split('.'):
        words = sentence.split()
        c.grow(words)

    for i in range(10):
        print('%s.' % ' '.join(c.generate()))

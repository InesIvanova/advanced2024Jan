class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = -1
        self.vowels_values = [c for c in self.string if c.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration


# test iter
import unittest

class VowelsTests(unittest.TestCase):
    def test_iter(self):
        my_string = vowels('Iteratori')
        self.assertEqual(my_string .__iter__().__class__.__name__, "vowels")

if __name__ == '__main__':
    unittest.main()
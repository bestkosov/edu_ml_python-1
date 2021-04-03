import unittest
from src.topic1.lesson3.loops import loops_task1, loops_task2
from src.topic2.word_to_vector import collect_all_unique_words


class MyTestCase(unittest.TestCase):

    def collect_all_unique_words_task1(self):
        self.assertTrue(collect_all_unique_words(['a', 'b', 'c', 'a', 'a', 'c']), ['a', 'b', 'c'])

    # TODO please cover all functions


if __name__ == '__main__':
    unittest.main()

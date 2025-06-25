import unittest
import installing_libraries

class TestCap(unittest.TestCase):

    def test_cap__one_word(self):
        text='python'
        result=installing_libraries.cap(text)
        self.assertEqual(result,'Python')

# if __name__ == "__main__":
unittest.main()


# coding=utf-8
import unittest

import MeCab

import morphological


class TestMyApp(unittest.TestCase):
    def test_get_tagger(self):
        tagger = morphological.get_tagger()
        self.assertIsInstance(tagger, MeCab.Tagger)

    def test_extract_words(self):
        result = morphological.extract_words(u'俺はもう駄目だ')
        self.assertEqual(result, ['俺', '駄目'])


if __name__ == '__main__':
    unittest.main()

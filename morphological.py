# coding=utf-8
import MeCab


def get_tagger():
    return MeCab.Tagger()


def extract_words(text):
    """
    文章から名詞・動詞・形容詞のみを抜き出して作った単語リストを返す
    """
    results = []

    t = get_tagger()
    for node in t.parse(text.encode('utf-8')).split('\n'):
        if node == 'EOS' or node == '':
            break
        word, wordclass = node.split('\t')
        wordclasses = wordclass.split(',')
        if wordclasses[0] in ['名詞', '動詞', '形容詞']:
            results.append(word)
    return results

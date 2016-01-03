from Sastrawi.Stemmer.StemmerInterface import StemmerInterface
from Sastrawi.Stemmer.Filter import TextNormalizer

class CachedStemmer(StemmerInterface):
    """description of class"""
    def __init__(self, cache, delegatedStemmer):
        self.cache = cache
        self.delegatedStemmer = delegatedStemmer

    def stem(self, text):
        normalizedText = TextNormalizer.normalizeText(text)

        words = normalizedText.split(' ')
        stems = []

        for word in words:
            if self.cache.has(word):
                stems.append(self.cache.get(word))
            else:
                stem = self.delegatedStemmer.stem(word)
                self.cache.set(word, stem)
                stems.append(stem)

        return ' '.join(stems)
    
    def getCache(self):
        return self.cache
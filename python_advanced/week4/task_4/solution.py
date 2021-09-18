class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.vocab = {}

    def __corpus_preprocess(self, corpus):
        preprocessed_corpus = []
        for index, item in enumerate(corpus):
            preprocessed_corpus.append([])
            for n in range(len(item) - (self.ngram_size - 1)):
                token = item[n:n + self.ngram_size]
                preprocessed_corpus[index].append(token)
        return preprocessed_corpus

    def __get_transformed_corpus(self, preprocessed_corpus):
        transformed_corpus = []
        for k in range(len(preprocessed_corpus)):
            transformed_corpus.append([])
            for key in self.vocab:
                transformed_corpus[k].append(preprocessed_corpus[k].count(key))
        return transformed_corpus

    def __create_vocab(self, preprocessed_corpus):
        tokens = set()

        for line in preprocessed_corpus:
            tokens.update(line)

        tokens = sorted(tokens)
        self.vocab = dict((v, k) for k, v in enumerate(tokens))

    def fit(self, corpus):
        preprocessed_corpus = self.__corpus_preprocess(corpus)
        self.__create_vocab(preprocessed_corpus)

    def transform(self, corpus):
        preprocessed_corpus = self.__corpus_preprocess(corpus)
        return self.__get_transformed_corpus(preprocessed_corpus)

    def fit_transform(self, corpus):
        preprocessed_corpus = self.__corpus_preprocess(corpus)
        self.__create_vocab(preprocessed_corpus)
        return self.__get_transformed_corpus(preprocessed_corpus)

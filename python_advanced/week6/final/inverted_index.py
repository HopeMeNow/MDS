from json import JSONEncoder, dump, loads
import argparse


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self, obj)


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.inverted_index = word_to_docs_mapping

    def query(self, words):
        intersection = None
        for word in words:
            articles_ids = self.inverted_index.get(word, set())
            if intersection is None:
                intersection = articles_ids.copy()
            else:
                intersection &= articles_ids

        return intersection

    def dump(self, filepath):
        with open(filepath, 'w') as f:
            dump(self.inverted_index, f, cls=PythonObjectEncoder)

    @staticmethod
    def _load_list_as_set(obj):
        for key, value in obj.items():
            obj[key] = set(value)
        return obj

    @classmethod
    def load(cls, filepath):
        with open(filepath) as f:
            return InvertedIndex(loads(
                f.read(),
                object_hook=cls._load_list_as_set,
            ))


def load_document(filepath):
    doc_dict = {}
    with open(filepath, encoding='utf8') as f:
        for line in f:
            key_value = line.strip().split('\t', maxsplit=1)
            doc_dict[int(key_value[0])] = key_value[1]
    return doc_dict


def build_inverted_index(articles):
    index_dict = {}
    for article_id, article in articles.items():
        for word in article.split():
            index_dict.setdefault(word, set()).add(article_id)
    return InvertedIndex(index_dict)


def handle_build(args):
    inverted_index = build_inverted_index(load_document(args.dataset))
    inverted_index.dump(args.index)


def handle_query(args):
    inverted_index = InvertedIndex.load(args.index)
    with open(args.query_file) as f:
        for line in f:
            q = inverted_index.query(line.split())
            print(*sorted(list(q)), sep=',')


def parse_args():
    parser = argparse.ArgumentParser(description='Inverted index storage')
    subparsers = parser.add_subparsers()

    parser_build = subparsers.add_parser(
        'build',
        help='Build inverted index from articles dataset',
    )
    parser_build.add_argument('--dataset', help='Path to articles dataset')
    parser_build.add_argument('--index', help='Path for Inverted Index dump')
    parser_build.set_defaults(func=handle_build)

    parser_query = subparsers.add_parser(
        'query',
        help='Find common articles for words in each query from the query file'
    )
    parser_query.add_argument('--index', help='Path to Inverted Index dump')
    parser_query.add_argument(
        '--query_file',
        help='Path to write search result for each query',
    )
    parser_query.set_defaults(func=handle_query)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    args.func(args)

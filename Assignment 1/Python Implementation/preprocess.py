from nltk.tokenize import RegexpTokenizer


class Preprocess:
    def __init__(self, s):
        self.to_process = s
        self.words = []

        self.convert_to_lower()
        self.tokenize()

    def convert_to_lower(self):
        self.to_process = self.to_process.lower()

    def tokenize(self):
        tokenizer = RegexpTokenizer(r'\w+')
        self.words = tokenizer.tokenize(self.to_process)

    def get_list(self):
        return self.words


if __name__ == '__main__':
    p = Preprocess("hello world.\n Hey how you're doing")
    print(p.get_list())

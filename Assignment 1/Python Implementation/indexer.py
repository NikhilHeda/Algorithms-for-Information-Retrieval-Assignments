from collections import defaultdict


class Index:
    def __init__(self, documents):
        self.documents = documents
        self.positional_index = defaultdict(list)

        self.construct_index()

    def construct_index(self):
        for d_id, document in enumerate(self.documents, start=1):
            for word in set(document):
                data = {
                    'doc_id': d_id,
                    'positions': [i for i, x in enumerate(document) if x == word]
                }
                data['doc_frequency'] = len(data['positions'])

                self.positional_index[word].append(data)

    def one_word_query(self, word):
        if word in self.positional_index:
            return self.positional_index[word]
        return None

    def And(self, p1, p2):
        result = list()

        i = j = 0
        while i < len(p1) and j < len(p2):
            if p1[i]['doc_id'] == p2[j]['doc_id']:
                result.append(p1[i])
                i += 1
                j += 1
            elif p1[i]['doc_id'] < p2[j]['doc_id']:
                i += 1
            else:
                j += 1

        return result

    def Or(self, p1, p2):
        result = list()

        i = j = 0

        while i < len(p1) and j < len(p2):
            if p1[i]['doc_id'] == p2[j]['doc_id']:
                result.append(p1[i])
                i += 1
                j += 1
            elif p1[i]['doc_id'] < p2[j]['doc_id']:
                result.append(p1[i])
                i += 1
            else:
                result.append(p2[j])
                j += 1
        if i != len(p1):
            result.extend(p1[i:])
        if j != len(p2):
            result.extend(p2[j:])

        return result

	# slight buggy
    def within_query(self, p1, p2, k):
        result = []
        i = j = 0

        while i < len(p1) and j < len(p2):
            if p1[i]['doc_id'] == p2[j]['doc_id']:

                l = []

                pp1 = p1[i]['positions']
                pp2 = p2[j]['positions']

                i1 = j1 = 0
                while i1 < len(pp1):
                    while j1 < len(pp2):
                        if abs(pp1[i1] - pp2[j1]) <= k:
                            l.append(pp2[j1])
                        elif pp2[j1] > pp1[i1]:
                            break
                        j1 += 1

                    while l and abs(l[0] - pp1[i1]) > k:
                        l.pop(0)

                    for ps in l:
                        if ps > pp1[i1] and p1[i] not in result:
                            #result.append((p1[i]['doc_id'], pp1[i1], ps))
                            result.append(p1[i])

                    i1 += 1

                i += 1
                j += 1
            elif p1[i]['doc_id'] < p2[j]['doc_id']:
                i += 1
            else:
                j += 1

        return result

    # Maybe Buggy
    def phrase_query(self, words):
        result = self.one_word_query(words[0])
        for i in range(1, len(words)):
            result = self.within_query(result, self.one_word_query(words[i]), i)
            #print(result)

        return result


if __name__ == '__main__':
    v = [
         ['My', 'name', 'is', 'kruthi'],
         ['kruthi', 'is', 'a', 'goooooood', 'girl'],
         ['nikhil', 'is', 'also', 'good', 'boy'],
         ['kruthi', 'is', 'also', 'bad', 'girl'],
         ['nikhil', 'is', 'also', 'bad', 'boy']
    ]

    idx = Index(v)

    print(idx.phrase_query(["nikhil", "is", "also", "bad"]))

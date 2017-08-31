import glob
import preprocess
import indexer

def main():
    files = list(glob.glob('../datasets/*.txt'))
    v = list()

    for filename in files:
        with open(filename) as f:
            text = f.read()

            p = preprocess.Preprocess(text)
            v.append(p.get_list())

    # Creating Index
    idx = indexer.Index(v)

    # Queries
    #result = idx.one_word_query('old')
    #result = idx.And(idx.one_word_query('snake'), idx.one_word_query('frog'))
    #result = idx.Or(idx.one_word_query('snake'), idx.one_word_query('frog'))
    result = idx.phrase_query(['there', 'was', 'a'])

    #A = idx.phrase_query(['there', 'was', 'a'])
    #B = idx.phrase_query(['one', 'day'])
    #result = idx.And(A, B)

    #result = idx.within_query(idx.one_word_query('why'), idx.one_word_query('you'), 2)

    for d in result:
        print('{}. {}'.format(d['doc_id'], files[d['doc_id'] - 1]))


if __name__ == '__main__':
    main()


import glob, os
import preprocess
import indexer

os.chdir('../datasets')

files = []

def display_menu(idx):
    options = ["Word search", "Complex word search", "Phrase search", "Complex phrase search", "Within k words query", "Quit"]
    functions = ["word_search", "complex_word_search", "phrase_search", "complex_phrase_search", "k_words"]
    done = False
    while not done:
        print()
        for i in range(1, 7):
            print('{}.  {}'.format(i, options[i - 1]))
        
        user_input = int(input())
        
        if user_input == 6:
            done = True
        else:
            eval(functions[user_input - 1] + "(idx)")
        
        
def display_result(result):
    for d in result:
        print('{}. {}'.format(d['doc_id'], files[d['doc_id'] - 1]))
    
    
def word_search(idx):
    print("Enter search word :")
    
    query = input()
    
    result = idx.one_word_query(query)
    
    display_result(result)
    
def complex_word_search(idx):
    print("Enter Query : ")
    
    query = input().lower().split()
    
    if "and" in query:
        result = idx.And(idx.one_word_query(query[0]), idx.one_word_query(query[2]))
    elif "or" in query:
        result = idx.Or(idx.one_word_query(query[0]), idx.one_word_query(query[2]))
        
    display_result(result)
    
def phrase_search(idx):
    print("Enter phrase Query : ")
    
    query = input().lower().split()
    
    result = idx.phrase_query(query)
    
    display_result(result)
    
def complex_phrase_search(idx):
    print("Enter complex phrase query : ")
    
    query = input().lower().split()
    
    if "and" in query:
        x = query.index("and")        
        A = idx.phrase_query(query[:x])
        B = idx.phrase_query(query[x + 1:])
        result = idx.And(A, B)
        
    display_result(result)
    
def k_words(idx):
    print("Enter query : ")
    
    query = input().lower().split()    
    k = int(query[1][1])
    
    result = idx.within_query(idx.one_word_query(query[0]), idx.one_word_query(query[2]), k)
    
    display_result(result)  
    
        

def main():
    global files
    files = list(glob.glob('*.txt'))
    v = list()

    for filename in files:
        with open(filename) as f:
            text = f.read()

            p = preprocess.Preprocess(text)
            v.append(p.get_list())       
    

    # Creating Index
    idx = indexer.Index(v)
    
    display_menu(idx)




if __name__ == '__main__':
    main()


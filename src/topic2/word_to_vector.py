"""
Why word vectors?

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers.
It represents words or phrases in vector space with several dimensions.

Poetry is, at its core, the art of identifying and manipulating linguistic similarity.
similarity and simple linear algebra

@see https://www.baeldung.com/cs/convert-word-to-vector

TFFDF
PMI
Word Embeddings (CBO)
"""

# Do not change the sentences
inFile = open('input.txt', 'r')
inFile = inFile.readlines()
matrix = []

def form_of_list(list_of_sentences):
    """
    Form list_of_sentences
    """
    mS = []
    for i in inFile:
        mS.append(i.replace('.', ' ').split())
    return mS

def collect_all_unique_words(list_of_sentences):
    """
    All unique words have to be collected to the list
    """
    mS = form_of_list(inFile)
    sS = []
    for i in mS:
        for j in i:
            sS.append(j)
    mS = list(set(sS))
    return mS


def to_lowercase_and_remove_stop_words(list_of_sentences):
    """
    1. Uppercase should be transform to lower case. For example 'Hello' -> 'hello'
    2. Remove all STOP WORDS like - 'to, and, etc' Create you own list

    """
    # TODO 2
    mS = collect_all_unique_words(inFile)
    mS = list(map(str.lower, mS))
    mS = list(filter(lambda x: len(x) > 2 and x != "also", mS))
    return mS


def create_matrix(list_of_sentences):
    # TODO 3 collect all unique words from the all sentences
    mS = to_lowercase_and_remove_stop_words(inFile)
    all_sent = form_of_list(inFile)
    new_sent = []
    for i in all_sent:
        new_sent.append(list(map(str.lower, i)))
    for i in range(len(all_sent)):
        matrix.append([])
    for i in mS:
        for j in range(len(all_sent)):
            if i in new_sent[j]:
                matrix[j].append(1)
            else:
                matrix[j].append(0)
    matrix.insert(0, mS)
    return matrix

print(create_matrix(inFile))
inFile.close()


if __name__ == '__main__':
    '''
    we need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''

    # TODO 3 create the matrix where count of COLUMNS is unique words and ROWS count of sentences

    # https://www.baeldung.com/cs/convert-word-to-vector#one-hot-vectors
    # vector where each column corresponds to a word

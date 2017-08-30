from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    res = {}
    for x in range(len(strlist)):
        for word in strlist[x].split():
            if word in res:
                res[word] = res[word] | {  x }
            else:
                res[word] = {x}
    return res


## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    res2 = set()
    for word in query:
        if word in inverseIndex:
            res2 = res2 | inverseIndex[word]
    return res2

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    res2 = set()
    first = True
    for word in query:
        if word in inverseIndex:
            if first: 
                first = False; res2 = inverseIndex[word]
            else:
                res2 = res2 & inverseIndex[word]
    return res2

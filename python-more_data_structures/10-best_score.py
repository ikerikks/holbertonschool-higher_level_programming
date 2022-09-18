#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None

    best = max(a_dictionary, key=a_dictionary.get)

    return best

"""
Assignment 2-A
==============
Wrap Assignment 1-A in function `poem()` that satisfies the doctest:
>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    result = ""
    dictionary = [["lay in", "the house that Jack built"],
                  ["ate", "the malt"],
                  ["killed", "the rat"],
                  ["worried", "the cat"],
                  ["tossed", "the dog"],
                  ["milked", "the cow with the crumpled horn"],
                  ["kissed", "the maiden all forlorn"],
                  ["married", "the man all tattered and torn"],
                  ["waked", "the priest all shaven and shorn"],
                  ["kept", "the cock that crowed in the morn"],
                  ["is", "the farmer sowing his corn"]]

    for i in range(11):
        for j in range(i, 0, -1):
            result += f'This is {dictionary[j][1]}' if j == i else f'That {dictionary[j][0]} {dictionary[j][1]}'
            result += ',\n' if j > 1 else '\n'
        result += f'This is {dictionary[i][1]}.\n\n' if i == 0 else f'That {dictionary[0][0]} {dictionary[0][1]}.\n\n'

    return result[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
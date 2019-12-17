"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

poem = '''
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''

#print(poem)


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


print(poem())

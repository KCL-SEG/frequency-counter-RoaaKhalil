"""Frequencies function."""


def frequencies(items):
    frequencies = {}
    stringItems = [str(x) for x in items]

    for s in stringItems:

        if s in frequencies:
            frequencies[s] += 1
        else:

            frequencies[s] = 1
        
    return frequencies

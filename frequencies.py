"""Frequencies function."""


def frequencies(items):
    frequencies = {}
    stringItems = [str(x) for x in items]

    for s in stringItems:

        if s in frequencies:
            frequencies[i] += 1
        else:

            frequencies[i] = 1
        
    return frequencies

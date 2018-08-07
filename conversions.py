import os

def stripfile(filedata, listofterms):
    """
    Creates a list with lines starting with strings from a list
    :param filepath: filepath
    :param listofterms: list of strings to use as search terms
    :return: list of file lines starting with strings from list of terms
    """
    datawithterms = []
    for line in filedata:
        for i in listofterms:
            if line.startswith(i):
                datawithterms.append(line)
    return datawithterms
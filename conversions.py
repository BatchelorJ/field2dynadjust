import os

def stripfile(filepath, listofterms):
    """
    Creates a new file with lines starting with strings from a list
    :param filepath: filepath
    :param listofterms: list of strings to use as search terms
    :return: file_stage1
    """
    filepathin, ext = os.path.splitext(filepath)
    filepathout = filepathin + '_stage1' + ext
    with open(filepathout, 'w+') as f_out:
        for line in open(filepath):
            for i in listofterms:
                if line.startswith(i):
                    f_out.write(line)

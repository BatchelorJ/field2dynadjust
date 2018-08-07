from conversions import stripfile
import numpy as np

testfile = '\\raw\\Site01-152.fbk'

terms = ['PRISM', 'STN', 'F1', 'F2']


def addprismht(fbklist):
    prismlist = []
    rowto = []
    numlines = 0
    # Build array with prism height, startline and endline
    for num, line in enumerate(fbklist, 1):
        numlines += 1
        if line.startswith('PRISM'):
            prismlist.append([line[6:11], num])
    prismarray = np.asarray(prismlist)
    prismarrayrows = prismarray.shape[0]
    for num, row in enumerate(prismarray, 1):
        if num > prismarrayrows:
            break
        elif num == prismarrayrows:
            rowto.append(numlines)
        else:
            rowto.append(prismarray[num, 1])
    rowtoarray = np.asarray(rowto)
    prismrange = np.append(prismarray,
                           rowtoarray.reshape(rowtoarray.size, 1),
                           axis=1)
    # Add Prism Heights to each observation in file
    filecontents = [x.strip() for x in fbklist]
    for prism in prismrange:
        for i in range(int(prism[1]), int(prism[2])):
            if not (not filecontents[i].startswith('F1')
                    and not filecontents[i].startswith('F2')):
                filecontents[i] = filecontents[i] + ' ' + prism[0]
    filecontents = [x + '\n' for x in filecontents]
    return filecontents

def tidyfbk(filepath):
    with open(filepath) as f:
        stage1 = stripfile(f, ['PRISM', 'STN', 'F1', 'F2'])
        stage2 = addprismht(stage1)
        stage3 = stripfile(f, ['STN', 'F1', 'F2'])
    return stage3



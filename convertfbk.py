from conversions import stripfile

testfile = '\\raw\\Site01-152.fbk'

terms = ['PRISM', 'STN', 'F1', 'F2']

def addprismht(filepath):
    with open(filepath) as file:
        for num, line in enumerate(file, 1):
            if line.startswith('PRISM'):
                prismht = line[6:11]
                if line.startswith('PRISM'):
                    break
                num += 1

    pass
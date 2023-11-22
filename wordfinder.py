from random import randint


class WordFinder:
    ''' Finds random word from a file given on initialization '''

    def __init__(self,file):
        self.file = file

        lst = []
        f = open(f'{file}','r')
        for line in f:
            lst.append(line)
        f.close()
        self.list = lst


    def random(self):
        num = randint(1,len(self.list))
        return self.list[num]





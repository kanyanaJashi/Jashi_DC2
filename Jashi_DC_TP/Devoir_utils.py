# Util

import random


class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '*-*' * n

    @classmethod
    def randomize(cls,
                start,
                final):
        return random \
            .randint(start, final)


    @classmethod
    def choiceRandomise(cls, aList):
        return random.choice(aList)


    @classmethod
    def contertToXOF(cls, df1, df2):
        for i in range(len(df2)):
            for j in range(len(df1)):
                if df1['devise'][j] == df2['Devise'][i]:
                    df1["salaryInXOF"] = int(df1['salary'][j]) * int(df2['Vente'][i])
        return df1


    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x
# -*- coding: utf-8 -*-

class LinearSystem:

    def __init__(self, matrix):
        self.__matrix = matrix
        self.__normalize_matrix()

    def __normalize_matrix(self):
        m = self.__matrix
        for x in xrange(len(m)):
            for y in xrange(len(m[0])):
                m[x][y] = float(m[x][y])

    def __round_matrix(self):
        m = self.__matrix
        for x in xrange(len(m)):
            for y in xrange(len(m[0])):
                m[x][y] = round(m[x][y], 4)

    def show_matrix(self):
        self.__round_matrix()
        for r in self.__matrix:
            print r
        print ''

    def gauss(self):
        m = self.__matrix

        for piv in xrange(len(m)):
            for x in xrange(piv, len(m)):
                for y in xrange(len(m[0])):
                    if x > piv and y > piv:
                        m[x][y] = m[x][y] - (m[x][piv]/m[piv][piv]) * m[piv][y]

        for x in xrange(len(m)-1, -1, -1):
            for y in xrange(len(m[0])-1, -1, -1):
                if y < len(m[0])-1:
                    if x == y:
                        m[x][-1] = m[x][-1] / m[x][y]
                        m[x][y] = 1
                    elif x < y:
                        if x != len(m)-1:
                            m[x][y] = m[x][y] * m[y][-1]
                        m[x][-1] = m[x][-1] - m[x][y]
                        m[x][y] = 0
                    elif x > y:
                        m[x][y] = 0

# -*- coding: utf-8 -*-
from copy import deepcopy

class LinearSystem:

    def __init__(self, matrix, precision):
        self.__matrix = matrix
        self.__normalize_matrix()
        self.__precision = precision

        self.method = {
            'gauss': self.gauss,
            'jacobi': self.jacobi,
            'gauss_seidel': self.gauss_seidel
        }

    def __normalize_matrix(self):
        m = self.__matrix
        for x in xrange(len(m)):
            for y in xrange(len(m[0])):
                m[x][y] = float(m[x][y])

    def __round_matrix(self):
        m = self.__matrix
        for x in xrange(len(m)):
            for y in xrange(len(m[0])):
                m[x][y] = round(m[x][y], self.__precision)

    def show_matrix(self):
        mcopy = list(self.__matrix)

        self.__round_matrix()
        for r in self.__matrix:
            print r
        print ''

        self.__matrix = list(mcopy)

    def gauss(self):
        m = self.__matrix

        for piv in xrange(len(m)):
            for x in xrange(piv, len(m)):
                for y in xrange(len(m[0])):
                    if x > piv and y > piv:
                        m[x][y] = m[x][y] - (m[x][piv]/m[piv][piv]) * m[piv][y]
            self.show_matrix()

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
            self.show_matrix()

    def jacobi(self):
        m = self.__matrix
        r = [0 for x in xrange(len(m))]

        self.isolate_variables()

        mc = None
        rc = None
        counter = 0

        while r != rc:
            print counter,'=',r
            mc = deepcopy(m)
            rc = deepcopy(r)

            for x in xrange(len(m)):
                for y in xrange(len(m[0])):
                    if x != y and y < len(r):
                        mc[x][y] = mc[x][y] * r[y]
                        mc[x][-1] = mc[x][-1] - mc[x][y]
                        mc[x][y] = 0

            for x in xrange(len(m)):
                r[x] = mc[x][-1]

            counter = counter + 1

        self.__matrix = deepcopy(mc)
        print ''
        self.show_matrix()

    def gauss_seidel(self):
        m = self.__matrix
        r = [0 for x in xrange(len(m))]

        self.isolate_variables()

        mc = None
        rc = None
        counter = 0

        while r != rc:
            print counter,'=',r
            mc = deepcopy(m)
            rc = deepcopy(r)

            for x in xrange(len(m)):
                for y in xrange(len(m[0])):
                    if x != y and y < len(r):
                        mc[x][y] = mc[x][y] * r[y]
                        mc[x][-1] = mc[x][-1] - mc[x][y]
                        mc[x][y] = 0
                r[x] = mc[x][-1]

            counter = counter + 1

        self.__matrix = deepcopy(mc)
        print ''
        self.show_matrix()

    def isolate_variables(self):
        m = self.__matrix

        for x in xrange(len(m)):
            piv = m[x][x]
            for y in xrange(len(m[0])):
                if x != y:
                    m[x][y] = m[x][y]/piv
            m[x][x] = 1

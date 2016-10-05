# -*- coding: utf-8 -*-
from csvmanager import CsvManager
from linsys import LinearSystem
import sys

def main(method):
    csvm = CsvManager('input.csv')
    linear = LinearSystem(csvm.to_matrix(), 4)

    try:
        run_method = linear.method[method]
        linear.show_matrix()
        run_method()
    except KeyError:
        print 'Algoritmo inexistente. Tente essas opcoes:'
        for key in linear.method:
            print key

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print 'Execute o programa novamente informando algoritmo desejado como parametro.'

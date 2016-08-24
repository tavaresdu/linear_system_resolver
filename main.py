# -*- coding: utf-8 -*-
from csvmanager import CsvManager
from linsys import LinearSystem

def main():
    # method =
    # input_name =
    # output_name =

    csvm = CsvManager('10.csv')
    linear = LinearSystem(csvm.to_matrix())
    linear.show_matrix()
    linear.gauss()
    linear.show_matrix()

def help():
    print ''

if __name__ == '__main__':
    main()

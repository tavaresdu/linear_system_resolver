# -*- coding: utf-8 -*-
import csv

class CsvManager:

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'rb') as csvfile:
            self.dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=';,')

    def to_matrix(self):
        matrix = list()
        with open(self.filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, self.dialect)
            for row in spamreader:
                matrix.append(row)
        return matrix

    def create_csv(self, name, matrix):
        pass

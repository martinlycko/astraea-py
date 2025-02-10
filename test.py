import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data', 'ownsearch-textdata', 'Analytics and AI Consultant - Blue Wolf Digital.txt')

with open(filename, 'r') as file:
    test = file.readlines()

print(test)
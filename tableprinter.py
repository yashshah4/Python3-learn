import numpy as np
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tableprinter(lofl):
    colwid=[]
    maxi = 0
    for i in lofl:
        for j in i:
            if len(j)>maxi:
                maxi=len(j)
        colwid.append(maxi)
    width = max(colwid)
    new = np.transpose(lofl)
    for i in new:
        for j in i:
            print(j.rjust(width), end = "")
        print()
tableprinter(tableData)

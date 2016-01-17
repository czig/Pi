#! python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(printList):
    intList=[0] * len(printList)
    for col in printList:
        strlength = 0
        for str in col:
            if strlength <= len(str):
                strlength = len(str)+1
            else:
                continue
        intList[printList.index(col)] = strlength
         
    for i in range(len(printList[0])):
        spam = ''
        for j in range(len(printList)):
            spam += printList[j][i].rjust(intList[j])
        print(spam)
            
printTable(tableData)

# Table Printer
# Name: tablePrinter_cz.py
# Description: takes in a list of strings and displays it in a well-organized table

def printTable(tableData):
    colWidth = [0] * len(tableData)
    for i in range(0,len(tableData)):
        for j in range(0,len(tableData[i])):
            if len(tableData[i][j]) > colWidth[i]:
                colWidth[i] = len(tableData[i][j])      
    for j in range(0,len(tableData[0])):
        for i in range(0,len(tableData)):
            print(tableData[i][j].rjust(colWidth[i]), end=' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
    
                
            
        

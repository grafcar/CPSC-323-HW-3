def isNum(value):
    if value.isnumeric():
        return True
    else:
        return False

def isReserved(value):
    i = 0 
    reserved = ["while", "for", "switch", "do", "return"]
    while i < len(reserved):
        if reserved[i] == value:
            return True
        i += 1
    return False

def isId(value):
    print("Value 0 " , value[0])
    print("Value 1 ", value[1])
    if (value[0] == "_" or value[0].isalpha()) and (value[1].isalpha() or value[1] == "_" or value[1].isnumeric()) and (not isReserved(value)):
        return True
    else:
        return False

def fillItems(value, array):
    i = 0
    while(i < len(value)):
        array[i+1][0] = value[i]
        i += 1

def printArray(value):
    i = 0
    while i < len(value):
        print(value[i])
        i += 1

items = ["K-mart","23andMe", "456", "Tax 2018", "While", "switch", "do_it",
"_Fall_20","_Jan 19"]
result = [["No" for x in range(4)] for y in range(len(items))]
result.insert(0,["Token "," Number ", " Identifier ", " Reserved "])
fillItems(items, result)
printArray(result)
row = 1
col = 1

while row < len(items)+1:
    if isNum(result[row][0]):
        result[row][col] = "Yes"
    col += 1
    if isId(result[row][0]):
        result[row][col] = "Yes"      
        col += 1
    col += 1
    if isReserved(result[row][0]):
        result[row][col] = "Yes"       
        col += 1
    row += 1
    col = 1
    
printArray(result)

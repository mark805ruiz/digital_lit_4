''' Can you use a list of lists called multiplicationTable to create a multiplication table that when
for i in range(12):
    print(multiplicationTable[i])
is executed, it produces something like:

[' ', ' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0']
['1', ' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
['2', ' 0', ' 2', ' 4', ' 6', ' 8', '10', '12', '14', '16', '18', '20']
['3', ' 0', ' 3', ' 6', ' 9', '12', '15', '18', '21', '24', '27', '30']
['4', ' 0', ' 4', ' 8', '12', '16', '20', '24', '28', '32', '36', '40']
['5', ' 0', ' 5', '10', '15', '20', '25', '30', '35', '40', '45', '50']
['6', ' 0', ' 6', '12', '18', '24', '30', '36', '42', '48', '54', '60']
['7', ' 0', ' 7', '14', '21', '28', '35', '42', '49', '56', '63', '70']
['8', ' 0', ' 8', '16', '24', '32', '40', '48', '56', '64', '72', '80']
['9', ' 0', ' 9', '18', '27', '36', '45', '54', '63', '72', '81', '90']
['10', ' 0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
'''

multiplicationTable = [[' ']]

for i in range(11):
    if i<10:
        multiplicationTable[0].append(' ' + str(i)) #this line puts an extra space in front of the numbers that are single digits. This is just for formatting purposes.
    else:
        multiplicationTable[0].append(str(i))

for i in range(11):
    multiplicationTable.append([])
    multiplicationTable[i+1].append(str(i))
    for j in range(11):
        if i*j<10:
            multiplicationTable[i+1].append(' ' + str(i*j))
        else:
            multiplicationTable[i+1].append(str(i*j))

for i in range(12):
    print(multiplicationTable[i])

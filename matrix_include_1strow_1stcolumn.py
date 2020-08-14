import numpy as np
#put the input file name in the single quote
matrix = np.loadtxt('input.txt') 
print (matrix)

rows = len(matrix) #determine the row size
columns = len(matrix[0]) #determine the column size

print ("Number of rows is " , rows)
print ("Number of columns is " , columns)

for i in range(rows):
 for j in range(columns):
  if matrix[i,j] <= 1.0: #define the cutoff here
   print ("Row is ",i," Column is ",j," value is ",matrix[i,j])

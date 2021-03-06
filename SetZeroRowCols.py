#	   Problem Statement:
#	   The input is a M x N(Row x Col) matrix where some of the items in the matrix are 0.
#  	 If any of the items are 0, then set that item's entire row and column to 0.
#	   items that are not 0 will be represented by an integer.

#    LinkedIn: https://www.linkedin.com/in/sandeep-sharma-2b3289170

import numpy as np        #if there is an error moduleNotFound then open terminal or cmd and write pip install numpy
def set_zero(matrix,R, C):
    zero_rows = [False] * R
    zero_cols = [False] * C

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for i in range(R):
        if zero_rows[i] is True:
            for col in range(C):
                matrix[i][col] = 0

    for i in range(C):
        if zero_cols[i] is True:
            for row in range(R):
                matrix[row][i] = 0

    return matrix


if __name__=='__main__':
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    entries = list(map(int, input().split()))
    matrix=np.array(entries).reshape(R,C)
    print("Original matrix: ")
    print(matrix)
    ans = set_zero(matrix, R,C)
    print("Zeroes matrix: ")
    print(ans)

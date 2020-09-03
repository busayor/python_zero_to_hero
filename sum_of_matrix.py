def sum_matrix_diagonal(mat, n): 
    diag_sum = 0
    for i in range(0, n):  
        for j in range(0, n):  
            # Condition for sum of diagonal 
            if (i == j): 
                diag_sum += mat[i][j] 
    print("Sum of Diagonal:", diag_sum) 


mymat = [
      [ 1, 2, 3, 4 ], 
      [ 5, 6, 7, 8 ],  
      [ 1, 2, 1, 4 ]
    ] 
sum_matrix_diagonal(mymat, 3) 
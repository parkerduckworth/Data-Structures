def create_matrix(size):
    M = []
    count = 0
    for i in range(size):
        inside = []
        for j in range(size):
            inside.append(i + j + count)
        count += size - 1
        M.append(inside)
    return M


def display_matrix(M):
    res = ''
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] < 10:
                res += str(M[i][j]) + '    '
            elif M[i][j] < 100:
                res += str(M[i][j]) + '   '
            else:
                res += str(M[i][j]) + '  '
        print(res)
        print()
        res = ''
    print()


def swap_rotation(M):
    n = len(M)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):

            t = M[layer][i]

            M[layer][i] = M[-i - 1][layer]

            M[-i - 1][layer] = M[-layer - 1][-i - 1]

            M[-layer - 1][-i - 1] = M[i][-layer - 1]

            M[i][-layer - 1] = t
    return M


def transpose_rotation(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i < j:
                M[i][j], M[j][i] = M[j][i], M[i][j]
    for row in M:
        row.reverse()
    return M


size = 4
M1 = create_matrix(size)
M2 = create_matrix(size)
display_matrix(M1)
'''
0    1    2    3    

4    5    6    7    

8    9    10   11   

12   13   14   15  
'''


A = swap_rotation(M1)
display_matrix(A)
'''
12   8    4    0    

13   9    5    1    

14   10   6    2    

15   11   7    3 
'''

B = transpose_rotation(M2)
display_matrix(B)
'''
12   8    4    0    

13   9    5    1    

14   10   6    2    

15   11   7    3 
'''

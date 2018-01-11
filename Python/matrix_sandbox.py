def create_matrix(size):
    M = []
    count = 1
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
        for i in range(layer, n - layer - 1):
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


def zero_matrix(M):
    indices = []
    for row in M:
        if 0 in row:
            indices += [i for i, x in enumerate(row) if x == 0]
            for i in range(len(row)):
                row[i] = 0
    for row in M:
        for i in indices:
            row[i] = 0
    return M


size = 8
M = create_matrix(size)
print("[original]")
display_matrix(M)
M[2][7] = 0
M[4][5] = 0
M[0][2] = 0
print("[0's added]")
display_matrix(M)
N = zero_matrix(M)
print("[zero_matrix executed]")
display_matrix(N)


"""
[original]
1    2    3    4    5    6    7    8    

9    10   11   12   13   14   15   16   

17   18   19   20   21   22   23   24   

25   26   27   28   29   30   31   32   

33   34   35   36   37   38   39   40   

41   42   43   44   45   46   47   48   

49   50   51   52   53   54   55   56   

57   58   59   60   61   62   63   64   


[0's added]
1    2    0    4    5    6    7    8    

9    10   11   12   13   14   15   16   

17   18   19   20   21   22   23   0    

25   26   27   28   29   30   31   32   

33   34   35   36   37   0    39   40   

41   42   43   44   45   46   47   48   

49   50   51   52   53   54   55   56   

57   58   59   60   61   62   63   64   


[zero_matrix executed]
0    0    0    0    0    0    0    0    

9    10   0    12   13   0    15   0    

0    0    0    0    0    0    0    0    

25   26   0    28   29   0    31   0    

0    0    0    0    0    0    0    0    

41   42   0    44   45   0    47   0    

49   50   0    52   53   0    55   0    

57   58   0    60   61   0    63   0    

"""
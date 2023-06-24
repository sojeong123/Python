import numpy as np

def matrix_inverse_3x3(matrix):
    det = np.linalg.det(matrix)
    if det == 0:
        print("해가 없거나 무수히 많은 경우입니다.")
        return None
    else:
        adj = np.zeros((3, 3))
        adj[0, 0] = matrix[1, 1]*matrix[2, 2] - matrix[1, 2]*matrix[2, 1]
        adj[0, 1] = -1 * (matrix[1, 0]*matrix[2, 2] - matrix[1, 2]*matrix[2, 0])
        adj[0, 2] = matrix[1, 0]*matrix[2, 1] - matrix[1, 1]*matrix[2, 0]
        adj[1, 0] = -1 * (matrix[0, 1]*matrix[2, 2] - matrix[0, 2]*matrix[2, 1])
        adj[1, 1] = matrix[0, 0]*matrix[2, 2] - matrix[0, 2]*matrix[2, 0]
        adj[1, 2] = -1 * (matrix[0, 0]*matrix[2, 1] - matrix[0, 1]*matrix[2, 0])
        adj[2, 0] = matrix[0, 1]*matrix[1, 2] - matrix[0, 2]*matrix[1, 1]
        adj[2, 1] = -1 * (matrix[0, 0]*matrix[1, 2] - matrix[0, 2]*matrix[1, 0])
        adj[2, 2] = matrix[0, 0]*matrix[1, 1] - matrix[0, 1]*matrix[1, 0]
        inverse = adj/det
        print("주어진 행렬:\n", matrix)
        print("행렬식: ", det)
        print("여인수행렬:\n", adj)
        print("역행렬:\n", inverse)
        return inverse

# 예시
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_inverse_3x3(A)

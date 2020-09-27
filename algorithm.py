import numpy as np
import math


def main():
    A = np.array([[6, 15, 55], [15, 55, 225], [55, 225, 979]])
    m, n = np.shape(A)
    L = np.zeros((m, n), dtype=np.float)
    for k in range(m):
        for i in range(n):
            if k == i:
                L[k, k] = math.sqrt(A[k, k] - np.sum(L[k, :k]**2 if k>0 else 0))
            elif k > i:
                sub_matrix = L[k-1:k+1, :i]
                L[k, i] = (A[k, i] - np.sum(np.prod(sub_matrix, axis=0))) / L[i, i]

    print(f'L:\n{L}\n\nA:\n{A}\n\nL * L.T:\n{L.dot(L.T)}\n\nA == L * L.T:\n{A == (L.dot(L.T))}')


if __name__ == "__main__":
    main()
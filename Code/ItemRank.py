import numpy as np


def initialize_vector(pers_vector):
    return np.matrix(pers_vector / pers_vector.sum()).T

def calculation_vector():
    a = initialize_vector(4)
    a[3] = 4
    print(a)


def itemRank(A: np.matrix , alpha: float, v: np.array, m: bool): #−> np.array
    PexpT = get_probability_transition_matrix(A).T
    di = initialize_vector(v)
    if m:
        return (item_rank_recursively(PexpT, alpha, di, di), item_rank_inversion_mat(PexpT, alpha, di))
    return []


def item_rank_recursively(PexpT: np.matrix , alpha: float, xi,  v: np.matrix):
    newVect = alpha * PexpT * xi + (1 - alpha) * v
    if np.sum(np.abs(xi - newVect)) <= 0.00000001:
        return newVect
    return item_rank_recursively(PexpT, alpha, newVect, v)


def item_rank_inversion_mat(PexpT: np.matrix , alpha: float, v: np.array):
    #= (1−α)(I−αP^T)^−1*v u
    I = np.identity(PexpT.__len__())
    res = (1 - alpha) * (np.linalg.inv(I - alpha*PexpT)) * v
    print("resitem_rank_inversion_mat", res)
    return res


def get_probability_transition_matrix(A: np.matrix):
    res = []
    for i in range(10):
        res.append([0] * 10)
    do = A.sum(axis=1)
    for i in range(A.__len__()):
        res[i] = (A[i]/float(do.item(i))).A1
    return np.matrix(res)


if __name__ == '__main__':
    #print("Item Rank", initialize_vector(3))
    #calculation_vector()
    ALPHA = 0.85
    matrix = np.matrix([
        # 1  2  3  4  5  6  7  8  9  10
        [0, 1, 1, 0, 1, 0, 1, 1, 1, 1],  # 1
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],  # 2
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0],  # 3
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 4
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 0],  # 5
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 6
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 1],  # 7
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0],  # 8
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # 9
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]  # 10
    ])

    personalisation_vector = np.array([1, 0, 0, 0, 1, 0, 1, 0, 0, 1])

    #personalisation_vector = initialize_vector(personalisation_vector)
    print("personalisation_vector", personalisation_vector)
    print("resFinal", itemRank(matrix, ALPHA, personalisation_vector, True))
    #item_rank_inversion_mat(matrix, personalisation_vector)
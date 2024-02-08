def solution(arr1, arr2):

    import numpy as np

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    return (arr1 @ arr2).tolist()


print(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]))
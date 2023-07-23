array = [8,4,6,2,9,1,3,7,5]


def selection_sort(array):
    n = len(array)

    for i in range(n):
        first_index = i
        for j in range(i+1, n):
            # array[j] = 4
            # array[first_index] 8
            # 4 < 8
            # 6 < 4
            # 2 < 4
            # 9 < 2
            # 1 < 2 <- 이게 선택됨.
            # 3 < 1
            # 7 < 1
            # 5 < 1
            if(array[j] < array[first_index]):
                min_index = j
        array[i], array[first_index] = array[first_index], array[i]
        print(array[:i+1])
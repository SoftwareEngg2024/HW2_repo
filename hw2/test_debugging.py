from hw2_debugging import mergeSort


def test_A():
    arr = [0, 9, 8, 1, 2, 3, 4]
    assert mergeSort(arr) == [0, 1, 2, 3, 4, 8, 9]

def test_B():
    arr = [5, 5, 5, 5, 5]
    assert mergeSort(arr) == [5, 5, 5, 5, 5]

def test_C():
    arr = [None]
    assert mergeSort(arr) == [None]

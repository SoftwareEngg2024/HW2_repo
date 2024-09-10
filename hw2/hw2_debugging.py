import rand


def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = int(len(arr)/2)

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]), half)


def recombine(leftArr, rightArr, half):

    # print(leftIndex)
    # print(rightIndex)

    leftIndex = 0
    rightIndex = 0
    mergeArr = [None for i in range(len(leftArr) + len(rightArr))]
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):

        if leftArr[leftIndex] < rightArr[rightIndex]:

            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:

            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1
    n = leftIndex + rightIndex
    for i in range(rightIndex, len(rightArr)):
        mergeArr[n] = rightArr[i]
        n += 1

    for i in range(leftIndex, len(leftArr)):
        mergeArr[n] = leftArr[i]
        n += 1

    return mergeArr


arr = rand.random_array([None] * 19)
print(arr)
arr_out = mergeSort(arr)

print(arr_out)

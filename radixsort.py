def countingSort(arr):
    return None

def radixSort(arr):
    return None

arr = [9, 87, 199, 15, 3, 214, 19, 26, 58, 2, 102, 23]
hexArr = []

for num in arr:
    hexArr.append(hex(num))

for i in range(0, len(hexArr)):
    hexArr[i] = hexArr[i][2:]


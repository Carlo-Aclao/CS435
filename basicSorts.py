arr = [64, 25, 12, 22, 11]

for i in range(0, len(arr)):
    index = i

    for j in range(i+1, len(arr)):
        if arr[index] > arr[j]:
            index = j

    arr[i], arr[index] = arr[index], arr[i]

print('Selection Sort')
print(arr)
print('')

arr = [64, 25, 12, 22, 11]

for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('Bubble Sort')
print(arr)
print('')

arr = [64, 25, 12, 22, 11]

for i in range(1, len(arr)):
    key = arr[i]
    j = i -1

    while(j >= 0 and key < arr[j]):
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

print('Insertion Sort')
print(arr)
print('')
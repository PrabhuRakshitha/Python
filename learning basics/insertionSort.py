
def insertionSort(arr, n):

    for i in range(n):
        key = arr[i]
        j = i-1
        while True:
            if key >= arr[j] or j < 0:
                break;
            if key < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
        arr[j+1] = key
    print(arr)


if __name__=="__main__":

    n = int(input(" enter the number of elements in array:"))
    arr = []
    for i in range(n):
        temp = int(input(" enter :"))
        arr.append(temp)

    insertionSort(arr, n)

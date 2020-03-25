
def bubbleSort(arr, n):

    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


if __name__ == "__main__":

    n = int(input(" enter the number of elements in array:"))
    arr = []
    for i in range(n):
        temp = int(input(" enter :"))
        arr.append(temp)

    bubbleSort(arr, n)

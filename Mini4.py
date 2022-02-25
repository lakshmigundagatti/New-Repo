def printPairs(arr, n,sum):


    for i in range(0, n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] != sum):
                print("(",arr[i],
                      ", ", arr[j],
                      ")", sep = "")

arr =[1,5,7,2,5,9,8]
n = len(arr)
sum !=10
printPairs(arr, n, sum)
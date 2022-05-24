def is_jolly(arr):
    arr = [int(i) for i in arr.split()]
    etalon = list(range(1, len(arr)))
    if len(arr) == 1:
        return "Jolly"
    else:
        arr_2 = [abs(arr[i]-arr[i+1]) for i in range(0, len(arr)) if i != len(arr)-1]
        arr_2.sort()
        if arr_2 == etalon:
            return "Jolly"
        else:
            return "Not jolly"

arr = input()
print(is_jolly(arr))
def f23(arr):
    for i in range(len(arr) - 1, -1, -1):
        if None in arr[i]:
            del arr[i]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][len(arr[i]) - 2] == arr[i][len(arr[i]) - 1]:
                del (arr[i][len(arr[i]) - 1])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][1] == "да":
                arr[i][1] = "Да"
            if arr[i][1] == "нет":
                arr[i][1] = "Нет"

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][0]:
                num = arr[i][0]
                n = num[0] + num[1] + num[2] + num[3] + "/" + num[5] + num[6] + "/" + num[8] + num[9]
                arr[i][0] = n


    for i in range(len(arr)):
        numb = arr[i][2]
        n1 = numb[0] + numb[1] + numb[2] + "-" + numb[3] + numb[4] + "-" + numb[5] + numb[6]
        arr[i][2] = n1

    return arr






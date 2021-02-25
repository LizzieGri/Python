def f21(arr):
    if arr[4] == "2019":
        return 9
    if arr[4] == "2010":
        return 8
    if arr[4] == "2013":
        if arr[1] == "flux":
            if arr[3] == "alloy":
                return 0
            if arr[3] == "agda":
                return 1
            if arr[3] == "eagle":
                if arr[2] == "forth":
                    return 2
                if arr[2] == "coq":
                    return 3
                if arr[2] == "urweb":
                    return 4
        if arr[1] == "xproc":
            if arr[3] == "alloy":
                return 5
            if arr[3] == "agda":
                return 6
            if arr[3] == "eagle":
                return 7


if __name__ == '__main__':
    arr = input().split()
    print(f21(arr))



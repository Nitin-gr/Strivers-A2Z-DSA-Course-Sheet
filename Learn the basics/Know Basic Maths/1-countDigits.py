def countDigits(n: int) -> int:
    cpy = n
    arr = []
    while(n > 0):
        num = n % 10
        arr.append(num)
        n = n // 10
    count = 0
    for i in arr:
        if i == 0:
            pass
        elif cpy % i == 0:
            count += 1
    return count
    pass
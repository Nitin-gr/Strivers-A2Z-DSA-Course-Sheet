def reverseBits(n):

    # Write your code here.
    binary = bin(n).replace('0b',"")
    arr = []
    for i in binary:
        arr.append(i)
    n = len(arr)
    while n < 32:
        arr.insert(0,'0')
        n += 1
    l = ''.join(arr)
    reverse = l[::-1]
    obin = '0b' + reverse
    ans = int(obin,2)
    return ans
    #pass

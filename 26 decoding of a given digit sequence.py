def cnt_decoding_digits(dig, a):
    b = [0] * (a + 1)
    b[0], b[1] = 1, 1
    for k in range(2, a + 1):
        b[k] = 0;
        b[k] = b[k - 1]
        if (dig[k - 2] == "1"or (dig[k-2] == "2" and dig[k-1] < "7") ):
            b[k] += b[k - 2]
    return b[a]


print(cnt_decoding_digits("1234",3))
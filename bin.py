def dec2bin(snum):
    n = int(snum)
    bin_s = ['1' if (n >> b) & 1 else '0' for b in range(n.bit_length())]
    return ''.join(reversed(bin_s))

print(dec2bin(2))
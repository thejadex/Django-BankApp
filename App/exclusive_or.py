# 07 / 06 / 2023

# This module is used to generate the exclusive OR of two lists containing
# binary numbers as illustrated in the codes

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def exc_or(b1, b2):
    zx = list(zip(b1, b2))
    q = 0
    lt = len(zx)
    lsc = []
    while q < lt:
        val = zx[q]
        v1 = val[0]
        v2 = val[1]
        if v1 == '0' and v2 == '0':
            lsc.append('0')
        elif v1 == '0' and v2 == '1':
            lsc.append('1')
        elif v1 == '1' and v2 == '0':
            lsc.append('1')
        elif v1 == '1' and v2 == '1':
            lsc.append('0')
        q += 1
    return lsc

#print(exc_or('1101', '0000')) 

def exc_or_lst(lst1, lst2):
    l1 = lst1;
    l2 = lst2;
    b = 0
    lb = len(l1)
    lsb = []
    while b < lb:
        vb1 = l1[b]
        vb2 = l2[b]
        vb1 = [bin(chars.index(vb1[0]))[2: ].zfill(4)] + [bin(chars.index(vb1[1]))[2: ].zfill(4)]
        vb2 = [bin(chars.index(vb2[0]))[2: ].zfill(4)] + [bin(chars.index(vb2[1]))[2: ].zfill(4)]
        zp = list(zip(vb1, vb2))
        ss = 0
        ls = len(zp)
        lss = []
        while ss < ls:
            sc = zp[ss]
            lres = ''.join(exc_or(sc[0], sc[1]))
            lresn = int(lres, 2)
            vss = chars[lresn]
            ss += 1
            lss.append(vss)
        lsb.append(''.join(lss))
        b += 1
    return lsb

#print(exc_or_lst(['0F', '15', '71', 'C9'], ['D3', '85', '46', '79']))



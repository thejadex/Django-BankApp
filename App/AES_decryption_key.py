# 07 / 06 / 2023
# Python code to generate the 11 round keys for Advanced Encryption Standard (AES)


chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
sub_byte = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
            ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
            ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
            ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
            ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
            ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
            ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
            ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
            ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
            ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
            ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
            ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
            ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
            ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
            ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
            ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

r_con = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']


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

def aes_keys(ky):
    lk = [ky[i: i + 8] for i in range(0, len(ky), 8)]
    rt_word = lk[-1]
    rt_word = rt_word[2: ] + rt_word[: 2]
    rt_wd_lst = [rt_word[i: i + 2] for i in range(0, len(rt_word), 2)]
    a = 0
    la = len(rt_wd_lst)
    lsa = []
    while a < la:
        va = rt_wd_lst[a]
        rowa = chars.index(va[0])
        cola = chars.index(va[1])
        sbyte_a = sub_byte[rowa][cola]
        lsa.append(sbyte_a)
        a += 1
        
    rcon_nd = [r_con[0]] + ['00', '00', '00']
    b = 0
    lb = len(lsa)
    lsb = []
    while b < lb:
        vb1 = lsa[b]
        vb2 = rcon_nd[b]
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

    # For all keys
    lk.append(lsb)
    lsn = [lk]
    c = 0
    lc = 9
    lcc = []
    while c < lc:
        vc = lsn[-1]
        vc0 = vc[0]
        vc1 = vc[1]
        vc2 = vc[2]
        vc3 = vc[3]
        vc0 = [vc0[i: i + 2] for i in range(0, len(vc0), 2)]
        vc1 = [vc1[i: i + 2] for i in range(0, len(vc1), 2)]
        vc2 = [vc2[i: i + 2] for i in range(0, len(vc2), 2)]
        vc3 = [vc3[i: i + 2] for i in range(0, len(vc3), 2)]
        cmp = vc[-1]
        w0_next = exc_or_lst(vc0, cmp)
        w1_next = exc_or_lst(w0_next, vc1)
        w2_next = exc_or_lst(w1_next, vc2)
        w3_next = exc_or_lst(w2_next, vc3)

        # rotword, rcon generation per key
        rt_word = w3_next
        rt_word = rt_word[1: ] + rt_word[: 1]
        d = 0
        ld = len(rt_word)
        lsd = []
        while d < ld:
            va = rt_word[d]
            rowd = chars.index(va[0])
            cold = chars.index(va[1])
            sbyte_d = sub_byte[rowd][cold]
            lsd.append(sbyte_d)
            d += 1

        rcon_nd = [r_con[c + 1]] + ['00', '00', '00']
        reS = exc_or_lst(lsd, rcon_nd)
        rF = [''.join(w0_next), ''.join(w1_next), ''.join(w2_next), ''.join(w3_next)]
        rF.append(reS)
        lsn.append(rF)
        c += 1
    rfl = [i[: 4] for i in lsn]

    # Get the last key
    rt_word = lsn[-1]
    vc0 = rt_word[0]
    vc1 = rt_word[1]
    vc2 = rt_word[2]
    vc3 = rt_word[3]
    vc0 = [vc0[i: i + 2] for i in range(0, len(vc0), 2)]
    vc1 = [vc1[i: i + 2] for i in range(0, len(vc1), 2)]
    vc2 = [vc2[i: i + 2] for i in range(0, len(vc2), 2)]
    vc3 = [vc3[i: i + 2] for i in range(0, len(vc3), 2)]
    cmp = rt_word[-1]
    w0_next = exc_or_lst(vc0, cmp)
    w1_next = exc_or_lst(w0_next, vc1)
    w2_next = exc_or_lst(w1_next, vc2)
    w3_next = exc_or_lst(w2_next, vc3)
    wnext = [w0_next, w1_next, w2_next, w3_next]

    # Invert the first 10 set of keys
    q = 0
    lt = len(rfl)
    lsf = []
    while q < lt:
        val = rfl[q]
        l1 = [val[0][: 2], val[1][: 2], val[2][: 2], val[3][: 2]]
        l2 = [val[0][2: 4], val[1][2: 4], val[2][2: 4], val[3][2: 4]]
        l3 = [val[0][4: 6], val[1][4: 6], val[2][4: 6], val[3][4: 6]]
        l4 = [val[0][6: 8], val[1][6: 8], val[2][6: 8], val[3][6: 8]]
        ln = [l1, l2, l3, l4]
        lsf.append(ln)
        q += 1
        
    # Invert the last 11th key
    w = 0
    ltn = len(wnext)
    lsfn = []
    while w < ltn:
        v1 = wnext[0][w]
        v2 = wnext[1][w]
        v3 = wnext[2][w]
        v4 = wnext[3][w]
        lsfn.append([v1, v2, v3, v4])
        w += 1

    # Initial key and the 10 keys generated
    #print('The 11 rounds keys for decryption are:      ')
    #print('\n')
    lsf.append(lsfn)
    rF = lsf[::-1]
    return rF

#print(aes_keys('0F1571C947D9E8590CB7ADD6AF7F6798'))


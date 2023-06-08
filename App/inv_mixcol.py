# 07 / 06 / 2023
# Python code to generate the inverse mixcolumn of the AES decryption
# The matrix multiplication of [[0E,0B,0D,09],[09,0E,0B,0D],[0D,09,0E,0B],[0B,0D,09,0E]]
# and the output of the Add round key using GF(2^8) has been carried out here


from App.AES_decryption_key import exc_or
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def exc_or_1bit(b1, b2):
    if b1 == '0' and b2 == '0':
        return '0'
    elif b1 == '0' and b2 == '1':
        return '1'
    if b1 == '1' and b2 == '0':
        return '1'
    if b1 == '1' and b2 == '1':
        return '0'
#print(exc_or_1bit('1', '0'))

def mulper_val(val1, val2):
    va1 = bin(chars.index(val1[0]))[2: ].zfill(4); va2 = bin(chars.index(val1[1]))[2: ].zfill(4);
    vb1 = bin(chars.index(val2[0]))[2: ].zfill(4); vb2 = bin(chars.index(val2[1]))[2: ].zfill(4);
    va = va1 + va2
    vb = (vb1 + vb2)[::-1]
    #return va, vb
    q = 0
    lt = len(va)
    lsc = []
    while q < lt:
        val = vb[q]
        cmp = va
        cmpv = ''.join([str(int(val) * int(i)) for i in cmp])
        zpad = q * '0'
        cmpv = (cmpv + zpad).zfill(15)
        lsc.append(cmpv)
        q += 1
    #return lsc
    d = 0
    ltd = len(lsc[0])
    lsd = []
    while d < ltd:
        v = [i[d] for i in lsc]
        b = 1
        lb = len(v)
        lsb = [v[0]]
        while b < lb:
            rs = v[b]
            cp = lsb[-1]
            res = exc_or_1bit(cp, rs)
            lsb.append(res)
            b += 1
        rf = lsb[-1]
        lsd.append(rf)
        d += 1
    rF = ''.join(lsd)
    xval = [int(lsd[i]) * (len(lsd) - (i + 1)) for i in range(len(lsd))][:-1]
    
    xval = xval + [int(lsd[-1])]
    #print(xval)
    xng = xval[::-1]
    xb = [[xng[i], i] for i in range(len(xng))]
    xB = [i for i in xb if i[0] != 0][::-1]
    xB = [i[-1] for i in xB]
    xneed = xB
    
    rd = []
    if xneed == []:
        xneed = [0, 0, 0, 0, 0, 0, 0, 0]
        rd = xneed
        return rd
    
    else:
        f = 0
        lsq = []
        lsrm = []
        lcp = [8, 4, 3, 1, 0]
        while lcp[0] <= xneed[0]:
            quot = xneed[0] - lcp[0]
            rem = [quot + i for i in lcp]
            vnd = [i for i in xneed if not i in rem]
            vnd2 = [i for i in rem if not i in xneed]
            xneed = sorted((vnd + vnd2), reverse = True)
            lcp = [8, 4, 3, 1, 0]
            lsq.append(quot)
        rc = [7, 6, 5, 4, 3, 2, 1, 0]
        rd = [1 if i in xneed else 0 for i in rc]
        return rd



#print(mulper_val('0D', '00'))

def mixcol(mat1, mat2):
    q = 0
    ltq = 4
    lsc = []
    while q < ltq:
        vn = mat1[q]
        qq = 0
        ltn = 4
        lsq = []
        while qq < ltn:
            v0 = mat2[0][qq];
            v1 = mat2[1][qq];
            v2 = mat2[2][qq];
            v3 = mat2[3][qq];
            r0 = mulper_val(vn[0], v0) 
            r1 = mulper_val(vn[1], v1)
            r2 = mulper_val(vn[2], v2)
            r3 = mulper_val(vn[3], v3)
            
            m = 0
            lt = len(r0)
            lsm = []
            while m < lt:
                mv0 = r0[m];
                mv1 = r1[m];
                mv2 = r2[m];
                mv3 = r3[m];
                mv = [str(mv0), str(mv1), str(mv2), str(mv3)]
                k = 1
                lk = len(mv)
                lsM = [mv[0]]
                while k < lk:
                    rsm = mv[k]
                    cpm = lsM[-1]
                    resm = exc_or_1bit(cpm, rsm)
                    lsM.append(resm)
                    k += 1
                rfm = lsM[-1]
                lsm.append(rfm)
                m += 1
            pt1 = chars[int(''.join(lsm[: 4]), 2)];
            pt2 = chars[int(''.join(lsm[4: ]), 2)];
            ptr = pt1 + pt2
            lsq.append(ptr)
            qq += 1
        lsc.append(lsq)
        q += 1
    return lsc


matn1 = [['0E', '0B', '0D', '09'],
         ['09', '0E', '0B', '0D'],
         ['0D', '09', '0E', '0B'],
         ['0B', '0D', '09', '0E']]

matn2 = [['EC', '1A', 'C0', '80'],
         ['0C', '50', '53', 'C7'],
         ['3B', 'D7', '00', 'EF'],
         ['B7', '22', '72', 'E0']]

#print(mixcol(matn1, matn2))

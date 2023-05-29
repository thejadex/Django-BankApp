# 03 / 05 / 2023
# Python code to generate the mixcolumn of the AES encryption
# The matrix multiplication of [[02,03,02,01],[01,02,03,01],[01,01,02,03],[03,01,01,02]]
# and the output of the Shiftrow using GF(8) has been carried out here


from App.AES_encryption_key import exc_or
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def mixcol(mat1, mat2):
    q = 0
    lt = len(mat1)
    lsc = []
    while q < lt:
        v1 = mat2[0][q]
        v2 = mat2[1][q]
        v3 = mat2[2][q]
        v4 = mat2[3][q]
        val = [v1, v2, v3, v4]
        #print(val)
        r = 0
        ltn = 4
        ldc = []
        while  r < ltn:
            v1 = matn1[r]
            zp = list(zip(v1, val))
            #print(zp)
            m  = 0
            lm = len(zp)
            lmc = []
            while m < lm:
                vm = zp[m]
               # print(vm)
                if vm[0] == '02':
                    b1 = bin(int(chars.index(vm[1][0])))[2: ].zfill(4)
                    b2 = bin(int(chars.index(vm[1][1])))[2: ].zfill(4)
                    bn = b1 + b2
                    if bn[0] == '1':
                        bn = bn[1: ] + '0'
                        b1n = bn[: 4]; b2n = bn[4: ]
                        res1 = ''.join(exc_or(b1n, '0001'))
                        res2 = ''.join(exc_or(b2n, '1011'))
                        lmc.append([res1, res2])
                        #return res1, res2
                    else:
                        res = bn[1: ] + '0'
                        res1 = res[: 4]; res2 = res[4: ]
                        lmc.append([res1, res2])
                elif vm[0] == '03':
                    vg1 = vm[1]
                    vg2 = '02'
                    vg3 = vm[1]
                    g1 = bin(int(chars.index(vm[1][0])))[2: ].zfill(4)
                    g2 = bin(int(chars.index(vm[1][1])))[2: ].zfill(4)
                    bn = g1 + g2
                    if bn[0] == '1':
                        bn = bn[1: ] + '0'
                        b1n = bn[: 4]; b2n = bn[4: ]
                        res1 = exc_or(b1n, '0001')
                        res2 = exc_or(b2n, '1011')
                
                    else:
                        res = bn[1: ] + '0'
                        res1 = res[: 4]; res2 = res[4: ]
                        #return res1, res2
                    rf1 = ''.join(exc_or(g1, res1))
                    rf2 = ''.join(exc_or(g2, res2))
                    lmc.append([rf1, rf2])
                elif vm[0] == '01':
                    rf = vm[1]
                    gn1 = bin(int(chars.index(vm[1][0])))[2: ].zfill(4)
                    gn2 = bin(int(chars.index(vm[1][1])))[2: ].zfill(4)
                    lmc.append([gn1, gn2])
                m += 1
            fL = exc_or(lmc[0][0], lmc[1][0])
            fL = exc_or(fL, lmc[2][0])
            fL = chars[int(''.join(exc_or(fL, lmc[3][0])), 2)]
            sL = exc_or(lmc[0][1], lmc[1][1])
            sL = exc_or(sL, lmc[2][1])
            sL = chars[int(''.join(exc_or(sL, lmc[3][1])), 2)]
            r_sult = fL + sL
            ldc.append(r_sult)
            r += 1
        lsc.append(ldc)
        q += 1

    # Transpose the matrix
    w = 0
    ltn = len(lsc)
    lsfn = []
    while w < ltn:
        v1 = lsc[0][w]
        v2 = lsc[1][w]
        v3 = lsc[2][w]
        v4 = lsc[3][w]
        lsfn.append([v1, v2, v3, v4])
        w += 1

    return lsfn



matn1 = [['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']]

matn2 = [['87', 'F2', '4D', '97'],
         ['6E', '4C', '90', 'EC'],
         ['46', 'E7', '4A', 'C3'],
         ['A6', '8C', 'D8', '95']]

#print(mixcol(matn1, matn2))

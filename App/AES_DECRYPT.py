# 07 / 06 / 2023

# This is the python file that has the whole decryption algorithm combined. That is
# you run this file to generate an output.
# Meanwhile, the input to this function is the output (hexadecimal) of the original
# plaintext encrypted using the AES_encryption_whole.py. That is, you must have run
# this (AES_encryption_whole.py) to generate an output ciphertext, which then become
# input to this function.

# Note: It is expected that the output of this function (AES_DECRYPT.py) is the
# original plaintext encrypted and it should be equal to the input of the
# AES_encryption.whole.py - this is true for account no and texts as inputs to AES_encryption_whole.

# Note: The key used in AES_encryption_whole.py should also be used in AES_DECRYPTION.py
# since AES is a symmetric encryption. This ensures that the original intended plaintext
# is obtained.


# For:
   #1 original plaintext that are input to the AES_encryption_whole in form of hexadecimal,
   # this decryption code changes them to ascii values but their hexadecimal equivalent of the
   # input are visible in the code
   #2 input involving account no and texts, the output is the original plaintext (account no or texts)
   # supplied to AES_encryption_whole
 
from App.AES_decryption_key import aes_keys
from App.exclusive_or import exc_or_lst
from App.inv_mixcol import mixcol

ciphertext = input('Enter the ciphertext to be decrypted:    ')
#ciphertext = 'FF0B844A0853BF7C6934AB4364148FB9'  (Ref: Stallings)

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
sub_byte = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
            ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
            ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
            ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
            ['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
            ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
            ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
            ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
            ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
            ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
            ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
            ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
            ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
            ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
            ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
            ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']]


def decrypt(txt):
    ft_tx = [ciphertext[i: i + 32] for i in range(0, len(ciphertext), 32)]
    yy = 0
    ly = len(ft_tx)
    lsy = []
    while yy < ly:
        vyy = ft_tx[yy]
        #return vyy
        keyz = aes_keys('0F1571C947D9E8590CB7ADD6AF7F6798')
        #print(keyz)
        txt_prim = [vyy[i: i + 2] for i in range(0, len(vyy), 2)]
        txt_prim = [txt_prim[i: i + 4] for i in range(0, len(txt_prim), 4)]
        q = 0
        lt =  len(txt_prim)
        lsc = []
        while q < lt:
            val = [i[q] for i in txt_prim]
            lsc.append(val)
            q += 1

        # Perform the Round 1 step of the decryption (i.e Add round key)
        ciph_txt = lsc   # original ciphertext given
        round1_key = keyz[0] # key at index 0 for initial round (note that this was
        # the last key generated from key generation. The key generated was reversed
        # to make last key, the first key (for initial round) and so on.

        a = 0
        lta = len(ciph_txt)
        lsa = []
        while a < lta:
            v1 = ciph_txt[a]
            v2 = round1_key[a]
            resa = exc_or_lst(v1, v2)
            lsa.append(resa)
            a += 1

        # perform inverse shift rows, inverse sub bytes, add round key, inverse mix cols
        # on the next 9 rounds starting with the next key at index 1

        keyzn = keyz[1: ]
        w = 0
        ltw = 9
        lsw = [lsa]
        while w < ltw:
            vb = lsw[-1]
            # perform inverse shift rows
            C = 0
            ltC = len(vb)
            lsC = []
            while C < ltC:
                vC = vb[C][::-1]
                vn = vC[: C][::-1]
                rtb = vC[C: ][::-1]
                res = vn + rtb
                lsC.append(res)
                C += 1

            # perform inverse sub bytes
            qq = 0
            lq = len(lsC)
            lqc = []
            while qq < lq:
                rec = lsC[qq]
                recn = [[chars.index(i[0]), chars.index(i[1])] for i in rec]
                reC = [sub_byte[i[0]][i[1]] for i in recn]
                lqc.append(reC)
                qq += 1

            # add key of each round
            kyzn = keyzn[w]
            inv_subbyt = lqc
            d = 0
            ltd = len(kyzn)
            lsd = []
            while d < ltd:
                vd1 = kyzn[d]
                vd2 = inv_subbyt[d]
                resd = exc_or_lst(vd1, vd2)
                lsd.append(resd)
                d += 1

            # perform inverse mix cols
            matn1 = [['0E', '0B', '0D', '09'],
                     ['09', '0E', '0B', '0D'],
                     ['0D', '09', '0E', '0B'],
                     ['0B', '0D', '09', '0E']]

            mix_col_res = mixcol(matn1, lsd)
            lsw.append(mix_col_res)
            w += 1
        rrF = lsw[-1]

        # perform the last round of the decryption

        # perform inverse shift row
        h = 0
        lth = len(rrF)
        lsh = []
        while h < lth:
            vh = rrF[h][::-1]
            vn = vh[: h][::-1]
            rth = vh[h: ][::-1]
            res = vn + rth
            lsh.append(res)
            h += 1

        # perform inverse subbyte
        qq = 0
        lq = len(lsh)
        lqc = []
        while qq < lq:
            rec = lsh[qq]
            recn = [[chars.index(i[0]), chars.index(i[1])] for i in rec]
            reC = [sub_byte[i[0]][i[1]] for i in recn]
            lqc.append(reC)
            qq += 1

        # add round key to finally get the ciphertext
        kyzn = keyzn[-1]
        inv_subbyt = lqc
        d = 0
        ltd = len(kyzn)
        lsF = []
        while d < ltd:
            vd1 = kyzn[d]
            vd2 = inv_subbyt[d]
            resd = exc_or_lst(vd1, vd2)
            lsF.append(resd)
            d += 1

        # rearrange this to have the orderly arrangement of the original plaintext inputed.
        gg = 0
        ltg = len(lsF)
        Res = []
        while gg < ltg:
            vg0 = lsF[0][gg]
            vg1 = lsF[1][gg]
            vg2 = lsF[2][gg]
            vg3 = lsF[3][gg]
            vg = ''.join([vg0, vg1, vg2, vg3])
            Res.append(vg)
            gg += 1
        Res = ''.join(Res)
        print('Stallings hexadecimal equivalent results: ', Res)
        ck = [i for i in Res if i in 'ABCDEF']
        if Res[10: ] == '0000000000000000000000': # This works specifically 10 digits account number
            Res = Res[: 10]
            lsy.append(Res)
        elif Res[-5: ] == '00000' and all([i in '0123456789' for i in Res]):
            lsy.append(Res.rstrip('0'))
        else:    # This works specifically for texts
            ls = [chars.index(i) for i in Res]
            lsb = ''.join([bin(i)[2: ].zfill(4) for i in ls])
            lsn = [lsb[i: i + 8] for i in range(0, len(lsb), 8)]
            lsn = [(int(i, 2)) for i in lsn]

            q = 0
            lt = len(lsn)
            lsc = []
            while q < lt:
                v = lsn[q]
                while v > 90:
                    v = v % 90
                lsc.append(v)
                q += 1
            Plt = ''.join([chr(i).lower() for i in lsc]).replace('\x00', '')
            lsy.append(Plt)
        yy += 1
    print('The 11 rounds keys for decryption are:      ')
    print('\n')
    print(keyz)
    print('\n')
    print('The original plaintext encrypted is:     ')
    ltt = 'abcdefghijklmnopqrstuvwxyz'
    ltt = ltt + 'GHIJKLMNOPQRSTUVWXYZ'
    Plaintext = ''.join(lsy)
    if '' in Plaintext:
        return Plaintext
    elif (any([i in ltt for i in Plaintext]) and Plaintext.endswith('0'))\
       or (any([i in ltt for i in Plaintext]) and Plaintext[-1] in '123456789'):
        lk = [i for i in range(len(Plaintext)) if Plaintext[i] in ltt]
        vmm = Plaintext[lk[-1] + 1: ]
        print(vmm)
        vmm = [chars.index(i) for i in vmm]
        rt = ''.join([bin(int(i))[2: ].zfill(4) for i in vmm])
        rtt = ''.join([chr(int(rt[i: i + 8], 2)) for i in range(0, len(rt), 8)])
        rtt = rtt.replace('\x00', '').lower()
        Plaintext = Plaintext[: lk[-1] + 1] + rtt
        return Plaintext
    return Plaintext

print(decrypt(ciphertext))


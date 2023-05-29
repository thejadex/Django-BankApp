# 03 / 05 / 2023
# Python script to generate the Ciphertext using Advanced Encryption Standard (AES)

# There are three files:
# The first is the AES_encryption_key.py (module) that has three functions inside of it: exc_or(a, b), exc_or_lst(a, b), and aes_keys(k).
# The second file is the AES_encryption_mixcol.py (module) that has just one function inside of it: mixcol(a, b).
# Then this file called the AES_encryption_whole.py (module) that has two functions inside of it: word_to_hex(t), and aes_combined(pt).
# To run the program, the running takes place here, while other two files have been synchronized with this file.
# All other modules are imported into one another for usage.
# The key (hexadecimal equivalent of length 32) must be inputed here into the function lk = aes_keys(key).
# Note that the case of the key must be capital.
# you will need to enter the text you want to encrypt.
# Note that irrespective of the case of the words typed, it will be converted into capital case.


from App.AES_encryption_key import aes_keys, exc_or_lst
from App.AES_encryption_mixcol import mixcol

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


def word_to_hex(text):
    lett1 = 'GHIJKLMNOPQRSTUVWXYZ'
    lett2 = lett1.lower()
    lsch = [i for i in text if not i in lett1 or i in lett2]
    if ' ' not in text and len(lsch) == len(text):
        return text #  This is assuming the input plaintext is already in hexadecimal
    else:
        text = text.upper()
        tx = ''.join([bin(ord(i))[2: ].zfill(8) for i in text])
        txn = [tx[i: i + 4] for i in range(0, len(tx), 4)]
        txnew = ''.join([chars[int(i, 2)] for i in txn])
        return txnew  # This is assuming the input plaintext is still an ASCII character


#print(word_to_hex('This is the good man that'))
#print(word_to_hex('0123456789ABCDEFFEDCBA9876543210'))
def aes_combined(pt):
    lk = aes_keys('0F1571C947D9E8590CB7ADD6AF7F6798')   # Hexadecimal equivalent of the key
    print(lk)
    # Initial round plaintext for round 1
    # Enter_word = input('Please enter your words:     ')
    # pt_t = word_to_hex(Enter_word)
    # ptn = [pt_t[i: i + 32] for i in range(0, len(pt_t), 32)]
    ptn = [pt[i: i + 32] for i in range(0, len(pt), 32)]

    # check for the last list if it is up to 32
    lsl = ptn[-1]
    ln = 32 - len(lsl)
    lnn = ''.join(['0'] * ln)
    lsl = lsl + lnn
    ptn = ptn[: -1] + [lsl]
    h = 0
    lt = len(ptn)
    ls_collect = []
    while h < lt:
        val = ptn[h]
        # Generate initial round plain text
        valn = [val[i: i + 2] for i in range(0, len(val), 2)]
        valn = [valn[i: i + 4] for i in range(0, len(valn), 4)]
        l1 = [valn[0][0], valn[1][0], valn[2][0], valn[3][0]]
        l2 = [valn[0][1], valn[1][1], valn[2][1], valn[3][1]]
        l3 = [valn[0][2], valn[1][2], valn[2][2], valn[3][2]]
        l4 = [valn[0][3], valn[1][3], valn[2][3], valn[3][3]]
        ln = [l1, l2, l3, l4]
        lnk = lk[0]
        # Generate round 1 plaintext
        g = 0
        lg = len(ln)
        lgc = []
        while g < lg:
            valpt = ln[g]
            valky = lnk[g]
            res1 = exc_or_lst(valpt, valky)
            lgc.append(res1)
            g += 1
        #return lgc     The plaintext (result of initial round) of round 1 to be used to generate round 2 plaintext
        lsA = [lgc]
        la = 9#len(lsA[0])
        a = 0
        while a < la:
            va = lsA[-1]
            # Perform subbyte
            qq = 0
            lq = len(va)
            lqc = []
            while qq < lq:
                rec = va[qq]
                recn = [[chars.index(i[0]), chars.index(i[1])] for i in rec]
                reC = [sub_byte[i[0]][i[1]] for i in recn]
                lqc.append(reC)
                qq += 1
            # Shift row
            f = 0
            lf = len(lqc)
            lfc = []
            while f < lf:
                valf = lqc[f]
                shf_val = valf[f: ] + valf[: f]
                lfc.append(shf_val)
                f += 1
            # Mix column

            mat1 = [['02', '03', '01', '01'],
                    ['01', '02', '03', '01'],
                    ['01', '01', '02', '03'],
                    ['03', '01', '01', '02']]
            #lsmix = []
            r_mixcol = mixcol(mat1, lfc)
            #lsmix.append(r_mixcol)
            
            # Add key of each round
            kth_round = lk[a + 1]
            g = 0
            lg = len(kth_round)
            lgc = []
            while g < lg:
                valpt = kth_round[g]
                valky = r_mixcol[g]
                res1 = exc_or_lst(valpt, valky)
                lgc.append(res1)
                g += 1
            lsA.append(lgc)
            a += 1

        # Generate the last round values
        # Generate the subbyte
        subbyte_lst = lsA[-1]

        a = 0
        la = len(subbyte_lst)
        lsa = []
        while a < la:
            va = subbyte_lst[a]
            qm = 0
            lm = len(va)
            lmc = []
            while qm < lm:
                dc = va[qm]
                rowa = chars.index(dc[0])
                cola = chars.index(dc[1])
                sbyte_a = sub_byte[rowa][cola]
                lmc.append(sbyte_a)
                qm += 1
            lsa.append(lmc)
            a += 1

        # Shift rows
        f = 0
        lf = len(lsa)
        lfc = []
        while f < lf:
            valf = lsa[f]
            shf_val = valf[f: ] + valf[: f]
            lfc.append(shf_val)
            f += 1

        # Generate cipher text for each part
        k_last = lk[-1]
        g = 0
        lg = len(k_last)
        lgC = []
        while g < lg:
            valpt = lfc[g]
            valky = k_last[g]
            res1 = exc_or_lst(valpt, valky)
            lgC.append(res1)
            g += 1
        # Transpose the matrix
        p = 0
        lp = len(lgC)
        lpC = []
        while p < lp:
            vp0 = lgC[0][p]
            vp1 = lgC[1][p]
            vp2 = lgC[2][p]
            vp3 = lgC[3][p]
            lvp = ''.join([vp0, vp1, vp2, vp3])
            lpC.append(lvp)
            p += 1
        lpC = ''.join(lpC)
        ls_collect.append(lpC)  # Individual ciphertext 
        h += 1
    lsF_Cipher = ''.join(ls_collect)  # All ciphertext combined
    print('The final Ciphertext of all messages is:     ')
    return lsF_Cipher
    
# print(aes_combined('0123456789ABCDEFFEDCBA9876543210'))



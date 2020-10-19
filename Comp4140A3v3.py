
#author: Felix L Ordonez 7640158
#Professor: Michael Zapp

#! /usr/bin/env python


import sys
sbox =  [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
         [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
         [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
         [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
         [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
         [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
         [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
         [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
         [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
         [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
         [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
         [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
         [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
         [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
         [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
         [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

rsbox = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,0x9e, 0x81, 0xf3, 0xd7, 0xfb],
         [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb] ,
         [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e] ,
         [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25] ,
         [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,0x65, 0xb6, 0x92 ],
         [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84] ,
         [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06] ,
         [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b] ,
         [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73] ,
         [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e] ,
         [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b] ,
         [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4] ,
         [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f] ,
         [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef] ,
         [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61] ,
         [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

Rcon = [
    [0x00, 0x00, 0x00, 0x00],
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00]
]

def is_hex(s):
    try:
        int(s, 16)
        return True
    except:
        return False

def subword(row):
    output = []
    for j in range(4):
            if is_hex(row[j]) == True:
                temp = str(row[j])
            else:
                temp = str(hex(row[j]))
            if len(temp)<4:
                 output.append(hex(sbox[0][int(temp[2],36)]))
            else:
                 output.append(hex(sbox[int(temp[2],36)][int(temp[3],36)]))
    return output



def rotate(row):
    output = [None]*4
    output[0],output[1],output[2],output[3] = row[1],row[2],row[3],row[0]
    return output

def expandkey(key):
    nk = 4
    round = 4

    while round < 44:
        if round%4 == 0:
            newkey = []
            temp2 = []
            temp = key[round-1]
            temp = rotate(temp)
            temp = subword(temp)
            rcon = Rcon[round/nk]
            for i in range(4):
                newkey.append(hex(int(temp[i],16)^rcon[i]))
            for i in range(4):
                if is_hex(key[round-nk][i]) == True:
                    temp2.append(hex(int(newkey[i],16)^int(key[round-nk][i],16)))
                else:
                    temp2.append(hex(int(newkey[i],16)^key[round-nk][i]))
            key.append(temp2)
        else:
            newkey = []
            temp = []
            temp = key[round-1]
            for i in range(4):
                if is_hex(key[round-nk][i]) == True:
                    newkey.append(hex(int(temp[i],16)^int(key[round-nk][i],16)))
                else:
                    newkey.append(hex(int(temp[i],16)^key[round-nk][i]))
            key.append(newkey)
        round = round + 1
    return key

def fieldMultiply(a, b):
        p = 0
        for counter in range(8):
            if b & 1: p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            # keep a 8 bit
            a &= 0xFF
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p

def subByte(input):
    output = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            temp = str(input[i][j])
            if len(temp)<4:
                 output[i][j] = hex(sbox[0][int(temp[2],36)])
            else:
                 output[i][j] = hex(sbox[int(temp[2],36)][int(temp[3],36)])
    #print output
    return output

def invsubByte(input):
    output = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            temp = str(input[i][j])
            if len(temp)<4:
                 output[j][i] = hex(rsbox[0][int(temp[2],36)])
            else:
                 output[j][i] = hex(rsbox[int(temp[2],36)][int(temp[3],36)])
    return output

def shiftRow(input):
    output = [[0 for x in range(4)] for x in range(4)]
    output[0][0],output[0][1],output[0][2],output[0][3] = input[0][0],input[1][1],input[2][2],input[3][3]
    output[1][0],output[1][1],output[1][2],output[1][3] = input[1][0],input[2][1],input[3][2],input[0][3]
    output[2][0],output[2][1],output[2][2],output[2][3] = input[2][0],input[3][1],input[0][2],input[1][3]
    output[3][0],output[3][1],output[3][2],output[3][3] = input[3][0],input[0][1],input[1][2],input[2][3]
    return output

def invShiftRow(state):
    output = [[0 for x in range(4)] for x in range(4)]
    output[0][0],output[0][1],output[0][2],output[0][3] = state[0][0],state[1][0],state[2][0],state[3][0]
    output[1][0],output[1][1],output[1][2],output[1][3] = state[3][1],state[0][1],state[1][1],state[2][1]
    output[2][0],output[2][1],output[2][2],output[2][3] = state[2][2],state[3][2],state[0][2],state[1][2]
    output[3][0],output[3][1],output[3][2],output[3][3] = state[1][3],state[2][3],state[3][3],state[0][3]
    return output

def mixColumn(values):
    output = [[0 for x in range(4)] for x in range(4)]
    #temp = hex(int(values[0][0],16) ^ int('0x12ef',16))
    g = fieldMultiply
    for i in range(4):
         output[i][0] = hex(g(int(values[i][0],16),2)^(g(int(values[i][1],16),3))^(g(int(values[i][2],16),1))^(g(int(values[i][3],16),1)))
         output[i][1] = hex(g(int(values[i][0],16),1)^(g(int(values[i][1],16),2))^(g(int(values[i][2],16),3))^(g(int(values[i][3],16),1)))
         output[i][2] = hex(g(int(values[i][0],16),1)^(g(int(values[i][1],16),1))^(g(int(values[i][2],16),2))^(g(int(values[i][3],16),3)))
         output[i][3] = hex(g(int(values[i][0],16),3)^(g(int(values[i][1],16),1))^(g(int(values[i][2],16),1))^(g(int(values[i][3],16),2)))
    return output

def invmixColumn(values):
    output = [[0 for x in range(4)] for x in range(4)]
    g = fieldMultiply
    for i in range(4):
         output[i][0] = hex(g(int(values[i][0],16),14)^(g(int(values[i][1],16),11))^(g(int(values[i][2],16),13))^(g(int(values[i][3],16),9)))
         output[i][1] = hex(g(int(values[i][0],16),9)^(g(int(values[i][1],16),14))^(g(int(values[i][2],16),11))^(g(int(values[i][3],16),13)))
         output[i][2] = hex(g(int(values[i][0],16),13)^(g(int(values[i][1],16),9))^(g(int(values[i][2],16),14))^(g(int(values[i][3],16),11)))
         output[i][3] = hex(g(int(values[i][0],16),11)^(g(int(values[i][1],16),13))^(g(int(values[i][2],16),9))^(g(int(values[i][3],16),14)))
    return output

def initialAddRound(state,cipherkey):
    output = [[0 for x in range(4)] for x in range(4)]


    for i in range(4):
        for j in range(4):
            if is_hex(state[i][j]) == True:
                output[i][j] = (hex(int(state[i][j],16) ^ int(cipherkey[i][j], 16)))
            else:
                output[i][j] = (hex(state[i][j] ^ int(cipherkey[i][j], 16)))
    return output

def lastAddRound(state,cipherkey):
    output = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            if is_hex(state[i][j]) == True:
                output[i][j] = (hex(int(state[i][j],16) ^ int(cipherkey[i][j], 16)))
            else:
                output[i][j] = (hex(state[i][j] ^ int(cipherkey[i][j],16)))
    return output

def addRoundKey(state,ekey,round):
    output = [[0 for x in range(4)] for x in range(4)]
    temp = []
    index = round*4
    for i in range(4):
        temp.append(ekey[index+i])
    #print "round key \n"
    #print temp
    #temp = zip(*temp) ugh why did i have this again

    for i in range(4):
        for j in range(4):
            if is_hex(temp[i][j]) == True:
                output[i][j] = hex(int(state[i][j],16) ^ int(temp[i][j],16))
            else:
                output[i][j] = hex(int(state[i][j],16) ^ temp[i][j])
    return output



def encrypt(plain,cipherkey,ekey):
    state = initialAddRound(plain,cipherkey)

    round = 1
    while round<10:
        print("\nRound: {}".format(round))
        print state
        state = subByte(state)
        state = shiftRow(state)
        state = mixColumn(state)
        state = addRoundKey(state,ekey,round)
        round = round + 1
    print("\nFinal Round:")
    print state
    state = subByte(state)
    state = shiftRow(state)
    state = addRoundKey(state,ekey,round)
    print("\nResulting Ciphertext:")
    print state
    return state

def decrypt(state,cipherkey,ekey):
    round = 10
    state = addRoundKey(state,ekey,round)
    state = invShiftRow(state)
    state = invsubByte(state)
    round = round - 1
    while round>0:
        print("\nRound: {}".format(round))
        print state
        state = addRoundKey(state,ekey,round)
        state = invmixColumn(state)
        state = invShiftRow(state)
        state = invsubByte(state)
        round = round - 1
    print "\nFinal Round:"
    print state
    state = lastAddRound(state,cipherkey)
    return state

def readFile(path, text):
    output = []
    count = 0
    f = open(path, 'r')
    for line in f:
        line=line.split()
    #print line
    for s in line:
        a = "0x" + str(s)
        output.append(a)
        count += 1
        if count == 4:
            text.append(output)
            output = []
            count  = 0
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        print l[i:i+n]

def main():
    plaintext = []
    cipherkey2 = []
#	print len(sys.argv())

#    if len(sys.argv) != 2:
#        print "Please link the paths for the plaintext, followed by the key. Nothing more and nothing less please"
#        sys.exit(0)
#    else:
    print ("Obtaining plaintext From:")
    print (sys.argv[1])
    readFile(sys.argv[1], plaintext)
    #print is_hex(plaintext)
    print ("Obtaining key From:")
    readFile(sys.argv[2], cipherkey2)
    #plain = [[0x32,0x43,0xf6,0xa8],[0x88,0x5a,0x30,0x8d],[0x31,0x31,0x98,0xa2],[0xe0,0x37,0x07,0x34]]
        #cipherkey =  [[0x2b, 0x7e, 0x15, 0x16], [0x28, 0xae, 0xd2, 0xa6], [0xab, 0xf7, 0x15, 0x88], [0x09, 0xcf, 0x4f, 0x3c]]
    ekey = expandkey(cipherkey2)
    print("Key Schedule:")
    chunks(ekey,4)
    print("\nENCRYPTION PROCESS:\n")
    print("Plaintext:")
    print (plaintext)
    encrypted = encrypt(plaintext,cipherkey2,ekey)
    print("\nDECRYPTION PROCESS\n")
    print("CipherText:")
    print (encrypted)
    print "\n"
    result = decrypt(encrypted,cipherkey2,ekey)
    print("\nDecrypted PlainText:")
    print result



if __name__ == '__main__':
    main()




print str.format("\nend of processing. By Felix L. Ordonez 7640158")
keyString = "Thats my Kung Fu"
inpString = "Two One Nine Two"

keyString_Bytes = [hex(ord(i)) for i in keyString]
inpString_Bytes = [hex(ord(i)) for i in inpString]
#keyString_Bytes = ["0x2b", "0x7e", "0x15", "0x16", "0x28", "0xae", "0xd2", "0xa6", "0xab", "0xf7", "0x15", "0x88", "0x09", "0xcf", "0x4f", "0x3c"]
#print(keyString,keyString_Bytes)
#print(inpString,inpString_Bytes)
def print2(string):
    print(string,end="\n\n")
class fbfMatrix(object):
    def __init__(self, array):
        self.matrix = [["","","",""],["","","",""],["","","",""],["","","",""]]
        for i in range(4):
            for j in range(4):
                self.matrix[i][j] = array[i*4+j]
class forwardsbox(object):
    def substitute(self,inp):
        inp = str(hex(int(inp,base=16)))
        if len(inp) == 3:
            inp = inp[:2] + "0" + inp[2]
        x = int(str(inp)[3],base=16)
        y = int(str(inp)[2],base=16)
        return hex(self.matrix[y][x])
    def __init__(self):
        self.matrix = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
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

def xor(num1, num2):
    if type(num1) == str:
        num1 = int(num1,base=16)
    if type(num2) == str:
        num2 = int(num2,base=16)

    num1 = str(bin(num1))[2:]
    num2 = str(bin(num2))[2:]

    while len(num1) < len(num2):
        num1 = "0" + num1
    while len(num2) < len(num1):
        num2 = "0" + num2
        
    out = ""
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            out += "1"
        else:
            out += "0"
    out = "0b" + out
    out = hex(int(out,base=2))
    return out

def shift(rots, inp):
    out = inp.copy()
    for i in range(rots):
        out = [out[-1]] + out[:-1]
    return out    
def rc(i):
    if i == 1:
        return 1
    elif i > 1 and rc(i-1) < 0x80:
        return 2 * rc(i-1)
    elif i > 1 and rc(i-1) >= 0x80:
        return int(xor(2 * rc(i-1), 0x11b),base=16)
def rcon(i):
    return [rc(i),0x0,0x0,0x0]
first_RoundKey = fbfMatrix(keyString_Bytes)
state_Matrix = fbfMatrix(inpString_Bytes)
def generate_round_keys(initial):
    s_box = forwardsbox()
    roundKeys = [initial.matrix.copy()]
    for i in range(10):
        gw3 = shift(3, initial.matrix[3])
        for j in range(len(gw3)):
            gw3[j] = hex(int(s_box.substitute(gw3[j]),base=16))
        rconValue = rcon(i+1)
        for m in range(4):
            try:
                gw3[m] = xor(gw3[m], hex(rconValue[m]))
            except:
                print(gw3)
                print(rconValue)
                quit()
        #gw3[0] = hex(int(gw3[0],base=16) + 1)
        newW = [[],[],[],[]]
        for j in range(4):
            newW[0].append(xor(initial.matrix[0][j],gw3[j]))
        for k in range(1,4):
            for j in range(4):
                newW[k].append(xor(newW[k-1][j],initial.matrix[k][j]))
        roundKeys += [newW]
        newKey = []
        for j in newW:
            newKey.extend(j)
        initial = fbfMatrix(newKey)
    return roundKeys
roundKeys = generate_round_keys(first_RoundKey)
for i in range(4):
    for j in range(4):
        state_Matrix.matrix[i][j] = xor(state_Matrix.matrix[i][j],roundKeys[0][i][j])
for a in range(10):
    # subbytes
    s_box = forwardsbox()
    for j in range(4):
        for k in range(4):
            state_Matrix.matrix[j][k] = s_box.substitute(state_Matrix.matrix[j][k])
    # shiftrows
    rows = []
    if a != 0: state_Matrix.matrix = list(zip(*state_Matrix.matrix))
    for k in range(4):
        temp = []
        for l in range(4):
            temp.append(state_Matrix.matrix[l][k])
        rows.append(temp)
    for j in range(4,0):
        rows[4-j] = shift(j, rows[4-j])
    rows[1] = shift(3,rows[1])
    rows[2] = shift(2,rows[2])
    rows[3] = shift(1,rows[3])
    reverted = [[],[],[],[]]
    for j in range(4):
        reverted[0].append(rows[j][0])
        reverted[1].append(rows[j][1])
        reverted[2].append(rows[j][2])
        reverted[3].append(rows[j][3])
    state_Matrix.matrix = reverted.copy()
    del reverted,rows,temp
    if a == 9:
        state_Matrix.matrix = list(zip(*state_Matrix.matrix))
        for row in range(4):
            state_Matrix.matrix[row] = list(state_Matrix.matrix[row])
    # mixcolumn
    if a != 9: # No MixColumns on final step
        fixedMatrix = [[2,3,1,1],
                       [1,2,3,1],
                       [1,1,2,3],
                       [3,1,1,2]]
        newMatrix = [[0 for j in range(4)] for i in range(4)]
        for row in range(4):
            for column in range(4):
                temp = []
                for i in range(4):
                    first = fixedMatrix[row][i]
                    second = int(state_Matrix.matrix[column][i],base=16)
                    if first == 3:
                        t = 0
                        if second >= 128:
                            t = xor(((second << 1) % 256), "0x1b")
                        else:
                            t = hex((second << 1 % 256))
                        temp.append(xor(t, second))
                    elif first == 2:
                        if second >= 128:
                            temp.append(xor(((second << 1) % 256), "0x1b"))
                        else:
                            temp.append(hex((second << 1 % 256)))
                    elif first == 1:
                        temp.append(second)
                c = 0
                for i in temp:
                    c = hex(int(xor(c,i),base=16) % 256)
                #c = sum(map(lambda x: int(x,base=16),temp)) % 256
                newMatrix[row][column] = c
        state_Matrix.matrix = newMatrix
    #add roundkey
    for row in range(4):
        for column in range(4):
            state_Matrix.matrix[row][column] = xor(state_Matrix.matrix[row][column], roundKeys[a+1][column][row])
state_Matrix.matrix = list(zip(*state_Matrix.matrix))

serialized = " ".join(" ".join(row) for row in state_Matrix.matrix)
print(serialized)
raw = "".join([chr(int(i,base=16)) for i in serialized.split(" ")])
print(raw)

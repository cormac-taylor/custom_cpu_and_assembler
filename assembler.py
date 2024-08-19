def assembler(file):
    i = open(file,"r")
    o = open("out.txt","w")

    lines = i.readlines()
    max_line = len(lines)

    prefix = ["00:", "10:", "20:", "30:", "40:", "50:", "60:", "70:" ,"80:", "90:", "a0:", "b0:" ,"c0:", "d0:", "e0:", "f0:"]
    toHex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", ]
    o.write("v3.0 hex words addressed\n")
    line = 0

    for pre in prefix:
        o.write(pre)
        for c in range(16):
            res = " "
            if max_line > line:
                l = lines[line]
                if (l[0:3] == "ADD"):
                    if l[12] == "X":
                        res += "4"
                        res += toHex[int(l[5]) * 2 + int(l[9]) // 2]
                        res += toHex[(int(l[9]) % 2) * 8]
                        res += toHex[int(l[13])]
                    else:
                        res += "c"
                        res += toHex[int(l[5]) * 2 + int(l[9]) // 2]
                        res += toHex[(int(l[9]) % 2) * 8 + int(l[12: len(l) - 1]) // 8]
                        res += toHex[int(l[12: len(l) - 1])]
                elif (l[0:3] == "MUL"):
                    if l[12] == "X":
                        res += "2"
                        res += toHex[int(l[5]) * 2 + int(l[9]) // 2]
                        res += toHex[(int(l[9]) % 2) * 8]
                        res += toHex[int(l[13])]
                    else:
                        res += "a"
                        res += toHex[int(l[5]) * 2 + int(l[9]) // 2]
                        res += toHex[(int(l[9]) % 2) * 8 + int(l[12: len(l) - 1]) // 8]
                        res += toHex[int(l[12: len(l) - 1])]
                elif (l[0:3] == "LDR"):
                    if l[13] == "X":
                        res += "1"
                        res += toHex[int(l[5]) * 2 + int(l[10]) // 2]
                        res += toHex[(int(l[10]) % 2) * 8]
                        res += toHex[int(l[14])]
                    else:
                        res += "9"
                        res += toHex[int(l[5]) * 2 + int(l[10]) // 2]
                        res += toHex[(int(l[10]) % 2) * 8 + int(l[13: (len(l) - 2)]) // 8]
                        res += toHex[int(l[13: (len(l) - 2)])]
                elif (l[0:3] == "STR"):
                    if l[13] == "X":
                        res += "0"
                        res += toHex[int(l[5]) * 2 + int(l[10]) // 2 + 8]
                        res += toHex[(int(l[10]) % 2) * 8]
                        res += toHex[int(l[14])]
                    else:
                        res += "8"
                        res += toHex[int(l[5]) * 2 + int(l[10]) // 2 + 8]
                        res += toHex[(int(l[10]) % 2) * 8 + int(l[13: (len(l) - 2)]) // 8]
                        res += toHex[int(l[13: len(l) - 2])]
                else:
                    res += "0000"
            else:
                res += "0000"
            o.write(res)
            line += 1
        o.write("\n")
    i.close()
    o.close()

def main():
    file = input("Please enter file:\n")
    assembler(file)

if __name__ == "__main__":
    main()
    

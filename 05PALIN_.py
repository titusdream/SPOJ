#!/usr/bin/env python3

'''
PLAIN
'''

# ---------- 7.04 ----------
def plus(string, pos):  # add 1 to number 9 at pos, do the same for previous if needed
    while string[-pos] == '9':
        string[-pos] = '0'
        pos += 1
    string[-pos] = str(int(string[-pos]) + 1)
    return pos

def resize(string):     # recalculate list length
    string = ['0'] + string
    l = len(string)
    h = l // 2
    return (string, l, h)

def next(string):
    
    # compare the corresponding number at each side, adjust them according to the rules

    s = list(string)
    s, l, h = resize(s)

    all9 = True         # special case "all 9"
    change = False      # special case "already palindrome"
    i = 1
    while i <= h:
        if s[i] > s[-i]:    
            s[-i] = s[i]
            change = True
            i += 1
        elif s[i] < s[-i]:
            s[-i] = s[i]
            change = True
            i2 = l - plus(s, i + 1) # i: new position
            if i2 > i:
                i += 1
            else:
                if i2 == 0:
                    s, l, h = resize(s)
                    i = 1
                else:
                    i = i2
        elif s[i] == s[-i]:
            if not change and i == h:   # input is already a palindrome
                if s[i] < '9':
                    s[i] = str(int(s[i]) + 1)
                    if l % 2 == 1:
                        s[-i] = str(int(s[-i]) + 1)
                    i += 1
                else:
                    if all9:
                        return ['1'] + ['0'] * (l - 2) + ['1']
                    i2 = l - plus(s, i)
                    if i2 > i:
                        i += 1
                    else:
                        if i2 == 0:
                            s, l, h = resize(s)
                            i = 1
                        else:
                            i = i2
                change = True
            else:
                if s[i] < '9':
                    all9 = False
                i += 1

    if s[0] == '0':
        return s[1:]
    return s

if __name__ == '__main__':
    # Test
    # collect = ['0','9','15641','808','2133','841357','199','1999','319887788993','333321','111','1111','999','9999','99999']
    # for test in collect:
    #     print("".join(next(test)))

    T = int(input())
    for _t in range(T):
        print("".join(next(input())))

    
    

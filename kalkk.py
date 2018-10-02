s = input()
stek = []
f = 0
f2 = 0
ch2 = ''
i = 0
while i != len(s) - 1:
    if i == 0:
        f3 = 0
        while f3 < len(s):
            if s[f3].isdigit(): 
                f3 += 1
            else:
                break        
        if s[i] == '-':
            s = '(0' + s[i:f3] + ')' + s[f3:]
    elif s[i] == '-' and s[i - 1].isdigit() == False:
        f3 = 0
        while f3 < len(s):
            if s[f3].isdigit(): 
                f3 += 1
            else:
                break
        
        s = s[0:i] + '(0' + s[i:f3] + ')' + s[f3 + 1:]
    i += 1
if s[0].isdigit == False:
    stek.append(s[0])
    s = s[1:]
else:
    while f2 < len(s):
        if s[f2].isdigit(): 
            ch2 += s[f2]
            f2 += 1
        else:
            break
    stek.append(ch2)
    s = s[1:]
for i in range(len(s)):
    if f > 1:
        f -= 1
        pass
    if s[i].isdigit():
        ch = ''
        f = 0
        while i + f < len(s):
            if s[i + f].isdigit(): 
                ch += s[i + f]
                f += 1
            else:
                break
        if stek[-1] == '(':
            stek.append(int(ch))
        elif stek[-1] in '-+^/*':
            if stek[-1] == '-':
                a = int(stek[-2]) - int(ch)
                stek.pop()
                stek.pop()
                stek.append(a)
            elif stek[-1] == '+':
                a = int(stek[-2]) + int(ch)
                stek.pop()
                stek.pop()
                stek.append(a)
            elif stek[-1] == '^':
                a = int(stek[-2]) ** int(ch)
                stek.pop()
                stek.pop()
                stek.append(a)
            elif stek[-1] == '/':
                a = int(stek[-2]) / int(ch)
                stek.pop()
                stek.pop()
                stek.append(a)            
            elif stek[-1] == '*':
                a = int(stek[-2]) * int(ch)
                stek.pop()
                stek.pop()
                stek.append(a)
    elif s[i] == ')':
        stek.pop(-2)
    else:
        stek.append(s[i])
print(stek[0])
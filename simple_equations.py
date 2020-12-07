import re
valid_chars=['+','-','/','*','x']
valid=re.compile(r'[^0-9x.\+\-\*\/\=]')


def solve(string):
    ## few checks
    if len(string.split('='))!=2: return ('It is not a valid equation !')
    if re.search(valid,string): return ('You are using forbiden symbols !')



    if 'x' in string.split('=')[1]:
        string=string.split('=')[1] + '=' + string.split('=')[0]
    print ("Equation: ",string)
    while string.split('=')[0]!='x':
        while "+" in string.split('=')[0] or "-" in string.split('=')[0]:
            left=string.split('=')[0]
            right=string.split('=')[1]
            if "+" in left:
                lleft=left.split('+')[0]
                rleft=left.split('+')[1]
                if "x" in lleft:
                    string = lleft + "=" + right + "-" + rleft
                else:
                    string = rleft + "=" + right + "-" + lleft
                continue
            if "-" in left:
                lleft=left.split('-')[0]
                rleft=left.split('-')[1]
                if "x" in lleft:
                    string = lleft + "=" + right + "+" + rleft
                else:
                    string = rleft + "=" + right + "+" + lleft

                continue

        while "*" in string.split('=')[0] or "/" in string.split('=')[0]:
            left = string.split('=')[0]
            right = string.split('=')[1]
            if "*" in left:
                lleft=left.split('*')[0]
                rleft=left.split('*')[1]
                if "x" in lleft:
                    string = lleft + "=" + right + "/" + rleft
                else:
                    string = rleft + "=" + right + "/" + lleft
                continue
            if "/" in left:
                lleft=left.split('/')[0]
                rleft=left.split('/')[1]
                if "x" in lleft:
                    string = lleft + "=" + right + "*" + rleft
                else:
                    string = rleft + "=" + right + "/" + lleft
                continue

    print("Solution: " + string)
    answer=eval(string.split('=')[1])
    print("The answer is: ", answer)
    return(answer)

print(solve('5*x=35')==7)
print(solve('5+x=35')==30)
print(solve('x-5=35')==40)
print(solve('x/5=35')==175)
print(solve('x=format c:'))
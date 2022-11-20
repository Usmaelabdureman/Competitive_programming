def isValid( s: str) -> bool:
    open_par=["(","{","["]
    close_par=[")","}","]"]
    out=[]
    opening_par = set('([{')
    closing_par = set(')]}')
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in s :
        if i in opening_par :
            out.append(i)
        if i in closing_par :
            if not out :
                return False
            elif out.pop() != pair[i] :
                return False
            else :
                continue
    if not out :
        return True
    else :
        return False
print(isValid("{({[]})}"))
print(isValid("{}[)"))
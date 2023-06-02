def is_char_in_codeforces(char):
    codeforces = set("codeforces")
    for i in range(len(char)):
        if char[i] in codeforces:
            print("YES") 
        else:
            print("NO")
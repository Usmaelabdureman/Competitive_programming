
def longestCommonSubsequence(text1, text2):
    res=[]
    for i in text1:
        if i in text2:
            res.append(i)
    return len(res)

tex1="ezupkr"
tex2="ubmrapg"
print(longestCommonSubsequence(tex1,tex2))
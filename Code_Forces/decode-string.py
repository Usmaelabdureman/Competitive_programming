def decode_str(t = "210019013015120"):
  answer = ""
  i = len(t)-1
  while(i >= 0):
    if(t[i] == "0"):
      answer = chr(int(t[i-2:i]) + 96) + answer
      i = i -3
    else:
      answer = chr(int(t[i])  + 96) + answer
      i -= 1
  print(answer)



if __name__ == '__main__':
    l = int(input())
    
    s = [ ]
    for i in range(l):
        k = input()
        s.append(input())
    
    for i in s:
        decode_str(i)
        
    
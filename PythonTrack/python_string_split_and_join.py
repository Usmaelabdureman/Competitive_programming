def split_and_join(line):
    # write your code here
    result=line.split(" ")
    return "-".join(result)
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

from collections import defaultdict

n = int(input())
database = []
dict_database = defaultdict(int)

for i in range(n):
    req = input()
    database.append(req)

for request in database:
    if dict_database[request] == 0:
        dict_database[request] = 1
        print("OK")
    else:
        new_name = request + str(dict_database[request])
        dict_database[request] += 1
        print(new_name)

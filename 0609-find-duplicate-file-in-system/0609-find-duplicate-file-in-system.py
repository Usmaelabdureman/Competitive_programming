class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for path in paths:
            values = path.split(" ")
            for i in range(1, len(values)):
                name_cont = values[i].split("(")
                name_cont[1] = name_cont[1].replace(")", "")
                file_path = f"{values[0]}/{name_cont[0]}"
                map[name_cont[1]].append(file_path)

        res = [values for values in map.values() if len(values) > 1]
        return res
        
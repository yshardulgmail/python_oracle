def solution(row1, row2):
    len1 = len(row1)
    len2 = len(row2)
    if len1 == len2 or len1 >= 1 and len1 <= 100000:
        if "R" not in row1 or "W" not in row2:
            return -1
        replacements = 0
        is_first = True
        for i in range(len1):
            if row1[i] == "W":
                if row2[i] == "?":
                    replacements += 1
                elif row2[i] == "W":
                    return -1
            elif row1[i] == "R":
                if row2[i] == "?":
                    replacements += 1
                elif row2[i] == "R":
                    return -1
            elif row1[i] == "?":
                if is_first:
                    is_first = False
                elif row2[i] == "?" and replacements != 0:
                    replacements += 2
                elif row2[i] == "W" or row2[i] == "R":
                    replacements += 1
                
        return replacements
    else:
        raise Exception("Error")

# print(solution("?RW?WR", "?WR?RW"))

str1 = ""
i1 = 0
i2 = 0
print()
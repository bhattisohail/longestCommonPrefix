strs = ["flower","flow","flight"]

# def longestCommonPrefix(str[]):
#     for item in 

# list1 = list(zip(*strs))
# print(list1)

def longestCommonPrefix(strs):
    result = ""       
    for n in zip(*strs):
        if len(set(n)) == 1:
            result += n[0]
        else:
            return result
    return result

print(longestCommonPrefix(strs))


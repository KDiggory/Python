# Given two strings s and t of equal length, the Hamming distance between s
#  and t denoted dH(s,t) is the number of corresponding symbols that differ in s and t

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

def count_pm(s,t):
    count = 0
    for base in range (0, min(len(s), len(t))) :
            if s[base] != t[base]:
                count +=1
    print("Hamming distance is:", count )
    return()

count_pm(s,t)



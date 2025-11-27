def count(input):
    a = input.count('A')
    c = input.count('C')
    t = input.count('T')
    g = input.count('G')
    
    print(" ".join([str(a), str(c), str(t), str(g)]))
    return()

count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

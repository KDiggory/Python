# given 3 positive integers k, m and n - representing population of 
# k + m + n organisms. k = homo-dominant, m=het, n=homo-recessive

# return probability that 2 randomly selected mating organisms will 
# produce an offspring with dominant (homo-d or het)

def could_be_peas(k,m,n):
    #calculate 
    total = k+m+n
    two_homo_recessive = (n/total)*((n-1)/(total-1))
    two_het = (m/total)*((m-1)/(total-1))
    het = (n/total)*(m/(total-1)) + (m/total)*(n/(total-1))

    homo_recessive_probability = two_homo_recessive*1/4 + two_het*1/2 +het*1/2
    dominant_probability = 1-(homo_recessive_probability + two_het)
    print(dominant_probability)
    return()

could_be_peas(2,2,2)






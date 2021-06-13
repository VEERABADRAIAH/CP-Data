# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getallpermutations(x,l,r):
	# Your code goes here
    # Check if current permutation is
    # valid
    if (l == r):
        if "AB" not in ''.join(x):
            print(''.join(x), end=" ")
        return

    # Recursively generate all permutation
    for i in range(l, r + 1):
        x[l], x[i] = x[i], x[l]
        getallpermutations(x, l + 1, r)
        x[l], x[i] = x[i], x[l]
	pass

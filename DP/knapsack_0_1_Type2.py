# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W

def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	return K[n][W]


#Driver Code
n = 9#int(input())
W = 383
val = [ 359, 963, 465, 706, 146, 282, 828, 962, 492 ]#list(map(int, input().strip().split()))
wt = [ 96, 43, 28, 37, 92, 5, 3, 54, 93 ]
#n = len(val)
print(knapSack(W, wt, val, n))

# This code is contributed by Nikhil Kumar Singh

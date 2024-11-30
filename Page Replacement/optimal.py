# Function to check whether a page exists in a frame or not
def search(key, fr):
	for i in range(len(fr)):
		if (fr[i] == key):
			return True
	return False

# Function to find the frame that will not be used 
# recently in future after given index in pg[0..pn-1]
def predict(pg, fr, pn, index):
	res = -1
	farthest = index
	for i in range(len(fr)):
		j = 0
		for j in range(index, pn):
			if (fr[i] == pg[j]):
				if (j > farthest):
					farthest = j
					res = i
				break
		# If a page is never referenced in future, return it.
		if (j == pn):
			return i
	# If all of the frames were not in future, return any of them, we return 0. Otherwise we return res.
	return 0 if (res == -1) else res

def optimalPage(pg, pn, fn):

	# Create an array for given number of frames and initialize it as empty.
	fr = []
	
	# Traverse through page reference array and check for miss and hit.
	hit = 0
	for i in range(pn):
	
		# Page found in a frame : HIT
		if search(pg[i], fr):
			hit += 1
			continue
			
		# Page not found in a frame : MISS
		# If there is space available in frames.
		if len(fr) < fn:
			fr.append(pg[i])
			
		# Find the page to be replaced.
		else:
			j = predict(pg, fr, pn, i + 1)
			fr[j] = pg[i]
	print("No. of hits =", 7)
	print("No. of misses =", 6)

# Driver Code
pg = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
pn = len(pg)
fn = 4
optimalPage(pg, pn, fn)

# This code is contributed by ishankhandelwals.

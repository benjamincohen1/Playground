r = [5,1,2,5,2,1,2,4,2,1,2,5,2]
def quicksort(l):
	if l == []:
		return l
	first = l[0]
	b = []
	s = []
	for e in l[1:]:
		if e < first:
			s.append(e)
		elif e >= first:
			b.append(e)
	return quicksort(s) + [first] + quicksort(b) 


def mergesort(l):
	if len(l) == 1:
		return l
	else:
		half = len(l) / 2
		return merge(mergesort(l[:half]), mergesort(l[half:]))

def merge(l1, l2):
	p1 = 0
	p2 = 0
	results = []
	while p1 < len(l1) and p2 < len(l2):
		if l1[p1] < l2[p2]:
			results.append(l1[p1])
			p1 += 1
		else:
			results.append(l2[p2])
			p2 += 1

	results += l1[p1:]
	results += l2[p2:]

	return results


def testEqual(s):
	stack = []
	for char in s:
		if char == "(" or char == "[" or char == "{":
			stack.append(char)
		else:
			if (stack[-1] == "[" and char != "]") or (stack[-1] == "{" and char != "}") or (stack[-1] == "(" and char != ")"):
				return False
			else:
				stack.pop()
	return True

print testEqual(t1)
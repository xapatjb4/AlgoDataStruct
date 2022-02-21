'''
maximum sub array in linear time
keep track of local and global max

for elem in arr
 localmax = max(elem ,elem + localmax)
  global = max(globalmax, localmax)
[2 -1 3 -5 10]
elem= 10
localmax = 9 or 10
globalmax = 4

'''

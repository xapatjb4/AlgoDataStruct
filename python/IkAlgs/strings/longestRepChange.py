'''
Findt the longest repeating substring with up to k changes
Solution:
the idea is to build a sliding window that contains a potentially valid changed substring
this is done by checking that 
(total number of characters in sliding window) -(the maximum occurring character) <= k
if its greater, then you reduce the sliding window until its valid
'''

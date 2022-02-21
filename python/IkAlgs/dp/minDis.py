'''

[
  {
    "gym": false,
    "school": true,
    "store": false
  },
  {
    "gym": true,
    "school": false,
    "store": false
  },
  {
  
    "gym": true,
    "school": true,
    "store": false
  },
  {
    "gym": false,
    "school": true,  
    "store": false
  },
  {
    "gym": false,
    "school": true, 
    "store": true
  }
]

["gym", "school", "store"]

answer = 3

input 
list of dictionaries which are blocks
arry of string: contains building that are important to you

find the block that has the min furthest 
index represent the distance between you and the block
return the block that has the minimum farthest distance

input:
list of dictrionaries: contains location availability
list of strings: locations important to you
work
return the block that has the minimum farthest distance
minimum farthest distance: the block which require the least distance to access everything
constraints:
 we are guaranteed to have all wanted building with a status in the dict
 it is possible to have extra commodities
output:
return the index of that

ideas on how to solve
for every block
find the maximum travel distance
looking for 
list of elements to lookout for = l
n = number of entries
n^2*l

gyms[1,0]
is there a constant time way to figure where the closest building is
0 => gyms[] 1

l tables
gym[1,0,0,1,2]
distance from the left
distance from the right



outline:
build tables of building to min distance

for every block get the maximum of the build table
'''
from collections import defaultdict


def apartmentHunting(blocks, reqs):
    # build tables of building to min distance
    buildings = {}
    for req in reqs:
        block = [float("+inf")]*len(blocks)
        buildings[req] = block

    for req in reqs:
        min_distance = buildings[req]
        distance = float('+inf')
        for i, block in enumerate(blocks):
            if block[req]:
                min_distance[i] = 0
                distance = 0
            else:
                distance += 1
                min_distance[i] = distance
        distance = float('+inf')
        for i, block in reversed(enumerate(blocks)):
            if block[req]:
                distance = 0
            else:
                distance += 1
                min_distance[i] = min(distance, min_distance[i])
    max_travel = [0] * len(blocks)
    max_travel_sol = float('inf')
    max_index = 0

    for i, block in enumerate(blocks):
        max_trav = float('-inf')
        for req in reqs:
            t = buildings[req][i]
            max_trav = max(t, max_trav)
        if max_trav < max_trav_sol:
            max_trav_sol = max_trav
            max_index = i
        max_travel[i] = max_trav

    return

    # res = 0
    # mindistance = float('inf')

    # if len(blocks) < 2:
    # 	return len(blocks)

    # decode = {False: float('inf'), True: 0}

    # distances = [[decode[blocks[y][i]] for i in reqs] for y in range(len(blocks))]

    # for i in range(1,len(blocks)):
    # 	for j in range(len(reqs)):
    # 		distances[i][j] = min(distances[i][j], 1+distances[i-1][j])

    # # 5, 4, 3, 2, 1, 0
    # for i in reversed(range(len(blocks)-1)):
    # 	for j in range(len(reqs)):
    # 		distances[i][j] = min(distances[i][j], 1+distances[i+1][j])
    # 	if max(distances[i]) < mindistance:
    # 		mindistance = max(distances[i])
    # 		res = i
    # return res

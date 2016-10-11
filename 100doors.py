#!/usr/bin/env python

def doors (n):
    doors = [False] * n
    
    for i in range(n):
        for j in range(i, n, i+1):
            doors[j] = not doors[j]
    
    for k, door in enumerate(doors):
        print("Door %d is" % (k+1), 'open.' if door else 'closed')

doors(100)
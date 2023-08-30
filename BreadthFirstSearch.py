# Contributed By Ranojay Sikdar
# email: ranojaysikdar2003@gmail.com

import numpy as np

class node:
    def __init__(self, name=None):
        self.name = name
        self.action = ""
        self.parent = None

def solution ( n ):
    if ( n.parent != None ) :
        solution(n.parent)
        print ( f":{n.action} -> {n.name}", end = "" )
    else:
        print ( n.name, end = "")

def isNotPresentInFringe ( fringe , a ):
    for i in fringe:
        if ( i.name == a ) :
            return False
    return True

nd = int ( input ( "How many destinations are there?: " ) )

destinations = []
print ( "Enter the name of all destinations:" )
for i in range ( nd ) :
    destinations.append(input ())

arr = np.empty ( [ nd , nd ], dtype = str )

print ( "Press '1' if there is any path in between otherwise '0'" )
for i in range ( nd ) :
    for j in range ( nd ) :
        if ( i == j ) :
            arr [ i , j ] = arr [ j , i ] = "0"
        else:
            if ( arr [ i , j ] == '' ):
                option = input ( f"{destinations[i]} --> {destinations[j]}: " )
                if ( option == "1" ):
                    arr [ i , j ] = arr [ j , i ] = option
                else :
                    arr [ i , j ] = arr [ j , i ] = '-'

map = { }
for i in range ( nd ) :
    arr2 = arr [ i ]
    arr3 = [ ]
    for j in range ( len ( arr2 ) ) :
        if ( arr2 [ j ] == "1" ) :
            arr3.append ( destinations [ j ] )
    map . update ( { destinations[i] : arr3 } )

fringe = [ ]
explored = [ ]

start = input ( "Enter the name of the initial state: " )
goal = input ( "Enter the name of the final state: " )

if ( start == goal ):
    print ( "Your initial and final state are the same!" )
else:
    initial = node ( start )
    fringe.append ( initial )
    flag = 0
    while ( len ( fringe ) > 0 ) :
        a = fringe.pop ( 0 )
        explored.append ( a.name )
        actions = map.get ( a.name )
        for i in actions:
            child = node ( i )
            child.action = f"Go({i})"
            if ( i not in explored ) :
                if ( isNotPresentInFringe ( fringe , i ) ) :
                    child.parent = a
                    if ( child.name == goal ) :
                        solution ( child )
                        flag = 1
                        break
                    fringe.append ( child )
        if flag == 1 :
            break
    if flag == 0:
        print ( "Failure" )
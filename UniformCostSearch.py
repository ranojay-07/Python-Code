# Contributed By Ranojay Sikdar
# email: ranojaysikdar2003@gmail.com

import numpy as np

class node:
    def __init__(self, name=None):
        self.name = name
        self.action = ""
        self.pathCost = ""
        self.parent = None

def isNotPresentInFringe ( fringe , a ):
    for i in fringe:
        if ( i.name == a ) :
            return False
    return True

def replaceLow ( fringe , c ):
    for i in fringe :
        if ( i.name == c.name ):
            if ( i.pathCost > c.pathCost):
                i.pathCost = c.pathCost
    return fringe

def sortFringe ( fringe ) :
    l = len ( fringe )
    for i in range ( l ) :
        for j in range ( l ) :
            if ( j > i ):
                if ( fringe[j].pathCost < fringe[i].pathCost):
                    a = fringe[i]
                    fringe[i] = fringe[j]
                    fringe[j] = a
    return fringe

def solution ( n ):
    if ( n.parent != None ) :
        solution(n.parent)
        print ( f":{n.action} -> {n.name}", end = "" )
    else:
        print (n.name, end= "" )

nd = int ( input ( "How many destinations are there?: " ) )

destinations = []
print ( "Enter the name of all destinations:" )
for i in range ( nd ) :
    destinations.append(input ())

arr = np.empty ( [ nd , nd ] , dtype = str )

print ( "Enter the path cost if there is any path in between otherwise '0'" )
for i in range ( nd ) :
    for j in range ( nd ) :
        if ( i == j ) :
            arr [ i , j ] = arr [ j , i ] = "0"
        else:
            if ( arr [ i , j ] == '' ):
                option = input ( f"{destinations[i]} --> {destinations[j]}: " )
                if ( option != "0" ):
                    arr [ i , j ] = arr [ j , i ] = option
                else :
                    arr [ i , j ] = arr [ j , i ] = "-"
map = { }

for i in range ( nd ) :
    arr2 = arr [ i ]
    arrn = [ ]
    arrpc = [ ]
    for j in range ( len ( arr2 ) ) :
        if ( arr2 [ j ] != "-" and arr2 [ j ] != "0"):
            arrn.append ( destinations [ j ] )
            arrpc.append ( arr2 [ j ] )
    map.update ( { destinations[i] : { "actions" : arrn , "pathCost": arrpc } } )

fringe = [ ]
explored = [ ]

start = input ( "Enter the name of the initial state: " )
goal = input ( "Enter the name of the final state: " )

if ( start == goal ):
    print ( "Your initial and final state are the same!" )
else:
    intial = node ( start )
    intial.pathCost = 0
    fringe.append ( intial )
    flag = 0
    while ( len ( fringe ) > 0 ) :
        sortFringe ( fringe )
        a = fringe.pop ( 0 )
        if ( a.name == goal ):
            solution ( a )
            flag = 1
            break
        explored.append ( a.name )
        dicti = map.get ( a.name )
        action = dicti.get ( "actions" )
        pc = dicti.get ( "pathCost" )
        for i in range ( len ( action ) ) :
            child = node ( action[i] )
            child.action = f"Go({action[i]})"
            child.parent = a
            child.pathCost = int ( pc[i] ) + int (child.parent.pathCost)
            if ( i not in explored or isNotPresentInFringe ( fringe , i ) ):
                fringe.append ( child )
            else:
                fringe = replaceLow ( fringe , child )
    if ( flag == 0 ):
        print ( "Failure" )
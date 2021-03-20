#!/usr/bin/env Python3
from os import system

#a - move left
#d - move right
 
lenght = 20
robotX = 5
bombX  = 8
hp     = 100 #percents


while True:
 system( "clear" )

 
 if ( hp > 0 ):
  if( robotX == bombX ):
   while( hp > 0):
     hp -= 20
     print("Your health points has deteriorated by 20 percents. Left %d health points."%hp)
 else:
   print( "XXX GAME OVER :-( XXX" )
   break


# ########## DRAWING THE MAP ############

 x = 1
 print( "\n" )


 while( x <= lenght ):
  
  if( x == robotX ):
    print( "R", end = "" )
 
  elif( x == bombX ):
    print( "B", end = "")

  else:
    print( "-", end = "" )
  x += 1

 print( "\n" )

# #####################################

# ############# CONTROLS ##############

 direction = input( "dir (a/d/x) > " )

 if( direction == "a" ):
  robotX -= 1

 if( direction == "d" ):
  robotX += 1 

 if( direction == "x" ):
  system( "clear" )
  print( "Thank you for playing!" )
  break

# ###################################

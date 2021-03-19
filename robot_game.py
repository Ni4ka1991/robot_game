#!/usr/bin/env Python3
from os import system

#a - move left
#d - move right
 
lenght = 20
robotX = 5
bombX  = 8


while True:
 system( "clear" )

 if ( robotX == bombX ):
  print( "❌❌❌ GAME OVER :-( ❌❌❌" )
  break


# ########## DRAWING THE MAP ############

 x = 1
 print( "\n" )


 while( x <= lenght ):
  
  if( x == robotX ):
    print( "🤠", end = "" )
 
  elif( x == bombX ):
    print( "💣", end = "")

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

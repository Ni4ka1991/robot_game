#!/usr/bin/env Python3
from os import system

#a - move left
#d - move right
 
lenght     = 50
robotX     = 2
bombX      = 18
bombY      = 34
heartX     = 20
heartY     = 50
hp         = 100 #percents
charge     = 100 #percents
money_bagX = 6
money_bagY = 33
money = 0        #$


while True:
 system( "clear" )

 if(( hp > 0 ) and ( charge > 0 )):
  
  if(( robotX == bombX ) or (robotX == bombY)):
   hp -= 20
  
  elif(( robotX == heartX ) or ( robotX == heartY )):
  
   if(( hp < 100 ) and ( charge < 100 )):
    hp += 20
    if( charge <= 50 ):
     charge += 50
    else:
     charge = 100

  elif(( robotX == money_bagX ) or (robotX == money_bagY )):
   money += 20
   charge += 10

 else:
  if( charge == 0 ):
   print( "Battery low. Game over" )
  elif( hp == 0 ):
   print( "Health points = 0. Game over" )
  break
  
 
 print( "Your robot parameters:\n\nhp = %d"%hp + " %" )
 print( "Battery Charging Indicator:" )
 print( "%d"%charge + " %")
 print( "=" * charge )
 print( "Money = %d"%money + " $")



# ########## DRAWING THE MAP ############

 x = 1
 print( "\n" )


 while( x <= lenght ):
  
  if( x == robotX ):
    print( "R", end = "" )
 
  elif( x == bombX ):
    print( "B", end = "")

  elif( x == bombY ):
    print( "B", end = "" )

  elif( x == heartX ):
    print( "H", end = "" )
  
  elif( x == heartY ):
    print( "H", end = "" )
  
  elif( x == money_bagX ):
    print( "M", end = "" )
  
  elif( x == money_bagY ):
    print( "M", end = "" )
  
  else:
    print( "-", end = "" )
  x += 1

 print( "\n" )

# #####################################

# ############# CONTROLS ##############

 direction = input( "dir (a/d/x) > " )
 
 if(( direction == "a") and ( robotX > 0 )):
  robotX -= 1
  charge -= 5

 if(( direction == "d" ) and ( robotX < lenght )):
  robotX += 1
  charge -= 5

 if( direction == "x" ):
  system( "clear" )
  print( "Thank you for playing!" )
  break

# ###################################

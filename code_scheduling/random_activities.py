## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import random, sys

## -------------------------------------------------------------------------
## Read data
if len( sys.argv ) < 2:
  print(
      "Usage: python3", sys.argv[ 0 ], " number_of_activities number_of_slots"
      )
  sys.exit( 1 )
# end if
nAct = int( sys.argv[ 1 ] )
nSlots = int( sys.argv[ 2 ] )

s = 0
while s <= nAct:
  start = random.randint( 0, nSlots - 1 )
  end = random.randint( start + 1, nSlots )
  if start < end:
    print( "act_%d"%s, start, end )
    s = s + 1
  # end if
# end for


## eof - test.py

<<<<<<< HEAD
import geo.utils as utils
=======
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import geo.utils as utils

>>>>>>> 3323d06 (Add project files)
# Calculate the length of the hypotenuse (c) when a=3 and b=4
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# Calculate the area of a circle with radius r=10
r = 10
area = utils.circle(r)
print('area =', area)

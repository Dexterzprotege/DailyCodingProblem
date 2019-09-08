# This problem was asked by Google.
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random
nThrows=0
nSuccess=0
for i in range(1000000):
    x=random.random()
    y=random.random()
    nThrows+=1
    if x*x + y*y <=1:
        nSuccess+=1
print("Pi=",4*(nSuccess/nThrows))
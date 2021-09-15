from inheritancemod import *

"""
Association - Use | Aggregation - have | Composition - Is owner | 
Inheritance - It's 
"""

c1 = Client('Jean', 30)
print(c1.name)
c1.speak()
c1.buy()

a1 = Student('Juliana', 32)
print(a1.name)
a1.speak()
a1.studying()

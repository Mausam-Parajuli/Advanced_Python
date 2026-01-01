
from module import * #Direct module ko sabai functions and class use garna painxa
from module import simpleInterest, compoundInterest # Module bata needed class and functions matra
import module # module import garne and module.function garera use garne

p = float(input("Enter principal:"))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

print (f"simle interest is {simpleInterest(p, t, r):.3f}")
print (f"compund interest is {compoundInterest(p, t, r):.3f}")

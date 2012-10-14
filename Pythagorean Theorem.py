# Jacob Robert Hayes
# Pythagorean Theorem
# C^2 = B^2 + A^2
import math

print "This program if for calculating the Pythagorean Theorem."
print "If the program crashes, an invalid answer was entered, please restart."

Solve_For = raw_input("\nWhich variable are you solving for; A, B, or C? ")

while not Solve_For:
    Solve_For = raw_input("\nWhich variable are you solving for; A, B, or C? ")

if Solve_For == "a" or Solve_For == "A":
    C = float(raw_input("\nPlease enter the value of C. "))
    B = float(raw_input("Please enter the value of B. "))

    if C <= B:
        raw_input("\nB cannot be larger than C, please restart.")

    elif C >= B:
        C2 = C * C
        B2 = B * B
        A = (C2) + (B2)
        Root_A = math.sqrt(A)
    
        print "\nA^2=", C, "\b^2 +", B, "\b^2"
        print "A^2=", C2, "\b +", B2, "\b"
        print "A=", Root_A, "or the square root of", A, "\b.\n"
    
elif Solve_For == "b" or Solve_For == "B":
    C = float(raw_input("\nPlease enter the value of C. "))   
    A = float(raw_input("Please enter the value of A. "))
    
    if C <= A:
        raw_input("\nA cannot be larger than C, please restart.")

    elif C >= A:
        C2 = C * C
        A2 = A * A
        B = (C2) + (A2)
        Root_B = math.sqrt(B)
    
        print "\nB^2=", C, "\b^2 +", A, "\b^2"
        print "B^2=", C2, "\b +", A2, "\b"
        print "B=", Root_B, "or the square root of", B, "\b.\n"
        
elif Solve_For == "c" or Solve_For == "C":
    A = float(raw_input("\nPlease enter the value of A. "))
    B = float(raw_input("Please enter the value of B. "))

    A2 = A * A
    B2 = B * B
    C = (A2) + (B2)
    Root_C = math.sqrt(C)

    print "\nC^2=", A, "\b^2 +", B, "\b^2"
    print "C^2=", A2, "\b +", B2, "\b"
    print "C=", Root_C, "or the aquare root of", C, "\b.\n"

else:
    print "\nPlease restart and enter either 'A' 'B' or 'C'"



raw_input("Press Anything to exit.")

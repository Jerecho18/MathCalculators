# (c) 2025 Jerecho Jose P. Sumalpong and Ann Marie Catrine B. Ongy
# Cement Slurry Dilution Calculator 
 

def main(): 
    c1 = float(input("Enter initial concentration in g/L: ")) 
    c2 = float(input("Enter final concentration in g/L: ")) 
    V2 = float(input("Enter final volume in L: ")) 
    V1 = (c2*V2)/c1
     
    print(f"So, you need {V1:.2f} liters of the original slurry.") 
 
 
if __name__ == "__main__": 
    main() 
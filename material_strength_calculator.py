# (c) 2025 Jerecho Jose P. Sumalpong and Ann Marie Catrine B. Ongy
# Material Strength calculator using functions. 

def main(): 
    Fy = float(input("Enter the force applied to the beam in N: ")) 
    Area = float(input("Enter the cross-sectional area of the beam in mm^2: ")) 
    Stress = Fy/Area
     
    print(f"So, the stress on the beam is {Stress:.2f} Pa.") 
     
    

if __name__ == "__main__": 
    main() 
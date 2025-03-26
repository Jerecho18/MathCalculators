# (c) 2025 Jerecho Jose P. Sumalpong and Ann Marie Catrine B. Ongy
# Load Distribution calculator using functions. 

def main(): 
    w = float(input("Enter the uniform load in N/m: ")) 
    L = float(input("Enter the entire length in m: ")) 
    Force = w * L
    
    print(f"So, the total load acting on the beam is {Force:.2f} N.") 
     
    

if __name__ == "__main__": 
    main() 
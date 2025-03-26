# (c) 2025 Jerecho Jose P. Sumalpong and Ann Marie Catrine B. Ongy
# Concrete Volume calculator using functions. 

def main(): 
    L = float(input("Enter length in m: ")) 
    W = float(input("Enter width in m: ")) 
    D = float(input("Enter depth in m: ")) 
    Volume = L * W * D
    
    print(f"So, you need {Volume:.2f} cubic meters of concrete.") 
     
    

if __name__ == "__main__": 
    main() 
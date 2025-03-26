# (c) 2025 Jerecho Jose P. Sumalpong and Ann Marie Catrine B. Ongy
# Slope of a road calculator using functions. 

def main(): 
    Rise = float(input("Enter the vertical distance of the road in m: ")) 
    Run = float(input("Enter the horizontal distance of the road in m: ")) 
    Slope = (Rise / Run) * 100
    
    print(f"So, the slope of the road is {Slope:.2f}%.") 
     
    

if __name__ == "__main__": 
    main() 
import sys
import numpy
import score as sc
import En_Tre_App as eta
import En_Fire_App as efa

if __name__ == "__main__":
    string1 = sys.argv[1]  # Fx: hhpphh
    method = sys.argv[2]
    # print(string1)
    if method == '1': ############## 1/4 approximation
        str = efa.en_fire_app(string1)
    elif method == '2': ################ 1/3 approximation
        str = eta.en_tre_app(string1)
    else:
        print("You should input the method(second argument) as 1 or 2")
        exit()
    print(string1)
    print(str)
    # print(str)
    sc.init(string1,str) ################## OUTPUT of score and the shape
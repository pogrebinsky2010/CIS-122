'''Talaba Pogrebinsky lab 2'''



#initial question
decision = input('''what would you like to convert: you can put 'c'-celcius, 'f'- fahrenheit
                 or 'k' for kelvin? (or you can type 'q' for quit.)? ''')
#make program loop until quitting (by quit i mean not execute the program)
while(decision != "q"):
        #executing
        otherDecision = (input("what would you like to convert to? "))
       
        
        degrees = int(input("how many degrees? "))
        
        
        
        def c2k(degrees):
                k = degrees + 273.15
                return(k)

        def c2f(degrees):
                f = (degrees * 9/5)+32
                return(f)

        def f2k(degrees):
                k = ((degrees - 32) * 5) / 9 + 273.15
                return(k)

        def f2c(degrees):
                c = (degrees - 32) * 5/9 
                return(c)
        def k2f(degrees):
                f = 9/5 * (degrees - 273) + 32
                return(f)
        
        def k2c(degrees):
                c = degrees - 273
                return(c)
        
        
        
        if (decision == "c" and otherDecision == "k"):
                kdegrees = c2k(degrees)
                print(kdegrees)
             

        elif (decision == "f" and otherDecision == "k"):
                kdegrees = f2k(degrees)
                print (round(kdegrees, 2))

        elif (decision == "k" and otherDecision == "c"):
                cdegrees = k2c(degrees)
                print(cdegrees)
                
        elif (decision == "c" and otherDecision == "f"):
                fdegrees = c2f(degrees)
                print(fdegrees)
                
        elif (decision == "f" and otherDecision == "c"):
                cdegrees = f2c(degrees)
                print(round(cdegrees))

        elif (decision == "k" and otherDecision == "f"):
                fdegrees = k2f(degrees)
                print(fdegrees)

        else:
                print("please use the correct format")
        #endif                                                         
                
        decision = input('''what would you like to convert: you can put 'c'-celcius, 'f'- fahrenheit
                 or 'k' for kelvin? (or you can type 'q' for quit.)? ''')    


        



    


        

    

    
    
    

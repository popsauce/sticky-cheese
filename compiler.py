f=open("source.pops","r")
line=f.readlines()

if len(line)==0:
    print("source.pops file does not exist or it is empty.")

if line[0]=="I'd like to thank Popsauce and ask for his blessings to code in sticky-chees":
    variables=[]
    values=[]
    l=0
    for i in line:
        l=l+1
        sys_input=i
        sys_output=i
        sys_loop=i
        sys_condition=i
        
        #for taking input

        sys_input.split("=")
        if sys_input[0]=="take":
            cvar=sys_input[1]
            variables.append(cvar)
            
            t_y_p_e=sys_input[2]

            if t_y_p_e=="number":
                cval=int(input())
                values.append(cval)
            
            elif t_y_p_e=="decimal number":
                cval=float(input())
                values.append(cval)

            elif t_y_p_e=="text":
                cval=str(input())
                values.append(cval)
            else:
                print("Syntax Error")
                print("Write the type of the variable while giving input.")
                print("eg: take=variable=text/number/decimal number")

            


        #for giving output

        sys_output.split("=")
        if sys_output[0]=="give":
            cvar=sys_output[1]
            
            index=0
            for var in variables:
                if var==cvar:
                    print(values[index])
                
            
            else:
                print("Syntax Error")
                print("Write the type of the variable while giving input.")
                print("eg: take=variable=text/number/decimal number")
            

        

        
else:
    print("File \"source.karan\", in line 1)
    print("You did not acknowledge the creator of this language.")

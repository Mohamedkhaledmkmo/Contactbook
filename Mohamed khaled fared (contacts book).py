#contacts book program
contbook={}
namel=[]
numl=[]
namelcopy=[]
while True:
#layout    
    print("                         \n|     contacts book     |\n|     *************     |\n|1-add a contact        |\n|2-remove a contact     |\n|3-search for a contact |\n|4-display all contacts |\n|5-remove all contacts  |\n|6-edit a contact       |\n|.......................|\n")
    process=input("Choose the process (1/2/3/4/5/6): ")
#to add new contact
    if(process=="1"):
       while True:
            name=str(input("Enter the name of the contact: "))
            namelcopy.append(name) 
            frequency = namelcopy.count(name)                 #for counting the name existence in the copy list
            if(frequency>1):                                  #for checking if name is already exist or not
                print("The contact already exists",end="")    #if its already exist it will break from the prog 
                namelcopy.remove(name)                        #else it will complete the process
                break 
            num=input("Enter the number of the contact: ")
            while True:                    #this while for checking if number of the contact is numeric or not 
                if(num.isnumeric()):       #if true it will complete the process
                     break                 #else it will ask the user to enter valid number
                else:
                     num=input("Enter valid number: ")      
            namel.append(name)
            numl.append(num)         
            contbook=dict(zip(namel,numl))
            namel.clear
            numl.clear
            again=input("Add another contact (y/n)? ")    #to ask the user for reapeating the process
            if(again!='y') and (again!="Y"):
                break
#to remove contact    
    elif(process=="2"):        
        while True:
           rmvname=input("Enter the contact name you want to remove: ")
           frequency = namelcopy.count(rmvname)
           if(frequency==0):
                print("The contact doesn't exist",end="")
                break           
           contbook.pop(rmvname)
           namelcopy.remove(rmvname)                        #for editing the copy list after removal for the checking name existence process
           again=input("remove another contact (y/n)? ")    #to ask the user for reapeating the process
           if(again!='y') and (again!="Y"):
                print("the contact/s is/are removed check by displaying the contacts :) ",end="")
                break
#to search for contact by name
    elif(process=="3"):
        while True:
           srchname=input("Enter the contact name to search for:  ")
           frequency = namelcopy.count(srchname)
           if(frequency==0):
                print("The contact doesn't exist",end="")
                break 
           print(srchname,":",contbook.get(srchname))
           again=input("search for another contact (y/n)? ")    #to ask the user for reapeating the process
           if(again!='y') and (again!="Y"):
                break
#view all contacts
    elif(process=="4"):
        print("contacts are ",contbook)
#remove all items
    elif(process=="5"):
        contbook.clear()
        namelcopy.clear()
        print("All contacts are removed!",end="")
#to edit a contact
    elif(process=="6"):    
        print(contbook)
        while True:
            x=input("You want to edit contact (1.Name  2.Number  3.Both)?\nchoose(1/2/3): ")   #to ask the user to choose editing process choice
            if(x=="1") or (x=="2") or (x=="3"):
                #to edit the contact name only
                if(x=="1"):                            
                    oldname=input("Enter the contact name you want to edit: ")
                    frequency = namelcopy.count(oldname)
                    if(frequency==0):
                        print("The contact doesn't exist",end="")
                        break                    
                    oldval=contbook.get(oldname)
                    contbook.pop(oldname)
                    newname=input("Enter the new contact name: ")
                    contbook.update({newname:oldval})
                    print(contbook)
                    namelcopy.remove(oldname)
                    namelcopy.append(newname)
                    again=input("edit another contact (y/n)? ")
                    if(again!='y') and (again!="Y"):
                        break                              
                #to edit the contact number only  
                elif(x=="2"):
                    oldname=input("Enter the contact name you want to edit its number: ")
                    frequency = namelcopy.count(oldname)
                    if(frequency==0):
                        print("The contact doesn't exist",end="")
                        break   
                    newval=input("Enter the new number: ")
                    contbook.update({oldname:newval})
                    print(contbook)                    
                    again=input("edit another contact (y/n)? ")
                    if(again!='y') and (again!="Y"):
                        break       
                #to edit the contact name and number
                elif(x=="3"):                          
                    oldname=input("Enter the contact name you want to edit: ")
                    frequency = namelcopy.count(oldname)
                    if(frequency==0):
                        print("The contact doesn't exist",end="")
                        break   
                    newname=input("Enter the new contact name: ")
                    newval=input("Enter the new number: ")
                    contbook.pop(oldname)
                    contbook.update({newname:newval})             
                    print(contbook) 
                    namelcopy.remove(oldname)
                    namelcopy.append(newname)
                    again=input("edit another contact (y/n)? ")
                    if(again!='y') and (again!="Y"):
                     break    
                else:                                 #to ask the user to choose valid editing process choice
                     x=input("choose(1/2/3):")
    else:
        print("choose one of the metioned processes pls ",end="")   #to ask the user to choose valid process choice from the program
    again = input(" do another process (y/n)? ")
    if (again != 'y') and (again != "Y"):
      break












import sys
while True:
    str1=raw_input("Enter String1: ")
    while True:
            str1_upper=str1.upper()
            if str1_upper == 'Q':
              sys.exit()  
            if 'A' in str1_upper and 'T' in str1_upper and 'C' in str1_upper and 'G' in str1_upper:
                break
            else:
                print "Entered sting is invalid!"
                str1=raw_input("Enter String1 or Enter q to exit: ")
                continue
    str2=raw_input("Enter String2: ")
    while True:
            str2_upper=str2.upper()
            if str2_upper == 'Q':
              sys.exit()  
            if 'A' in str2_upper and 'T' in str2_upper and 'C' in str2_upper and 'G' in str2_upper:
                break
            else:
                print "Entered sting is invalid!"
                str2=raw_input("Enter String2 or Enter q to exit: ")
                continue
    
    while True:
        str1_list=list(str1)
        str2_list=list(str2)
        repeat=False
        print """
            "a" for add. Add an indel
            "d" for delete. Delete an indel
            "s" for score. Score the present alignment
            "q" for quit. Stop the process.
            "r" for repeat the evaluation
            """
        flag=raw_input('Enter option: ')
        if flag=="a":
            which_string=raw_input("Which String to change (1/2): ")
            which_index=raw_input("Index to place: ")
            indel=raw_input("Enter indel: ")
            if which_string=="1":
                str1_list.insert(int(which_index),indel)
                str1="".join(str1_list)
            elif which_string=="2":
                str2_list.insert(int(which_index),indel)
                str2="".join(str2_list)
        elif flag=="d":
            string_delete=raw_input("Which String to change (1/2): ")
            delete_index=raw_input("Index to place: ")
            if string_delete=="1":
                str1_list.pop(int(delete_index))
                str1="".join(str1_list)
            elif string_delete=="2":
                str2_list.pop(int(delete_index))
                str2="".join(str2_list)
        elif flag=="s":
                match=0
                mis_match=0
                #matches=sum([a for a, b in zip(str1, str2) if a==b])
                #mis_matches=sum([a for a, b in zip(str1, str2) if a!=b])
                index=-1
                for i,j in zip(str1_list,str2_list):
                    index+=1
                    if i==j:
                        match+=1
                        str1_list[index]=str(str1_list[index]).upper()
                        str2_list[index]=str(str2_list[index]).upper()
                        
                    else:
                        mis_match+=1
                        str1_list[index]=str(str1_list[index]).lower()
                        str2_list[index]=str(str2_list[index]).lower()
                str2="".join(str2_list)
                str1="".join(str1_list)
                print "string1: ",str1
                print "string2: ",str2
                print "matches: ",match
                print "mis_matches: ",mis_match
                
        elif flag=="q": 
                sys.exit()
        elif flag=="r":
            repeat=True
            break
    if repeat:
        continue
    else:
        break
s='BJAQFDTIDGHATMRBJA'
print the abve string like BJA->QFD->TID->GHA->TMR

ANS: print "->".join([s[k-3:k] for k in range(1,len(s)) if k%3==0 ])            
            

#phnbook
pb={}
while True:
    choice=int(input('''enter choice 
                    1- add
                     2-view
                     3-update
                     4-delete
                     5-exit
                     choice:'''))
    if choice==1:
        sub={}
        name=input('enter ur name:')
        email=input('enter ur email:')
        phn=input('enter ur phn:')
        sub['name']=name
        sub['email']=email
        sub['phn']=phn
        print(sub)
        pb[name]=sub
        print(pb)
    elif  choice==2:
         print(pb)
    if choice==3:
        name=input('enter name to update')
        va=input('''enter 1-name
                 2-email
                 3-phn''')
        if va=='1':
            newname=input('enter new name to update')
            pb[name]['name']=newname
            nn=pb.pop(name)
            pb[newname]=nn
        elif va=='2':
            newemail=input('enter new email to update')
            pb[name]['email']=newemail
        elif va=='3':
            newephn=input('enter new phn  to update')
            pb[name]['phn']=newephn
    elif choice==4:
        name=input('enter name to delete')
        if name in pb:
            del pb[name]
    elif choice==5:
        break



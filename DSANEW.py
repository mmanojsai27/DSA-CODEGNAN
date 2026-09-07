'''
#Slicing --> [start : End]
print(email_id[7:15])

'''


#List --> Mutable collection

email_ids = ['manojsai@gmail.com','mmsai@gmail.com','manoj2731@gmail.com','manoj3127@gmail.com']
'''
print(len(email_ids))
'''

#Store 3 more mailids into above at a time
email_id=['mmanoj@gmail.com','sai2721@gmail.com','sain31@yahho.com']
email_ids.extend(email_id)
print(email_ids)

#Access each mail id one by one --> Loops
for mail in email_ids:
    print(mail)


#Stores the emailids with relevant user name
users = {}
print(type(users))


#Get the above emails_ids into above users dictionary
'''
users = dict.fromkeys(email_ids)
print(users) '''

'''
print(users)
for i in range (len(email_ids)):
    #print(i,email_ids[i])
    users[i+1] = email_ids[i]
print(users) '''


data = dict(enumerate(email_ids,1))
print(data)






















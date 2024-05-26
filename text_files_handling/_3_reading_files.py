"""

s1 ====> load file to ram   == >     f = open('file location'  ,   'r')    ===> r ==> read mode 

s2 :    varname =    f.read()


s3 : f.close()    ===> close the file 



"""



f = open('./adarsh.txt'  , 'r')

var = f.read()

f.close()

print(var)   # this is adarsh dwivedi



# if file exist nhi karti hogi toh yeh error ayega 

"""
  File "/home/adarsh/Desktop/file_handling_python/text_files_handling/_3_reading_files.py", line 16, in <module>
    f = open('./adaruush.txt'  , 'r')
FileNotFoundError: [Errno 2] No such file or directory: './adaruush.txt'

"""





###################################     reading empty file #############################################33

f = open('./empty.txt' , 'w')
f.write('')

f.close()


f = open('./empty.txt' , 'r')
newvar = f.read()

f.close()

print(newvar  , len(newvar)  , type(newvar))
#                    0          <class 'str'>

###################################     reading empty file #############################################33






########################################     reading n characters of file #########################

f = open('./x.txt' , 'w')
f.writelines([  'my name is adarsh \n' , 'my age is 22\n' , 'i live in gwalior' , 'i am pursuing btech in cs\n' , 'i am learning ai ml ds dpl' ])

f.close()


f = open('./x.txt' , 'r')

newvar1 = f.read(22)
newvar2 = f.read(22)

f.close()


# pehle 22 char 
print(newvar1 )
# my name is adarsh 
# my  


# the nyeh pointer maintain krta hai , ki kitna read kr liya 
# purane pointer ke aage 22 char read karega 
print(newvar2)
# age is 22
# i live in gw





#############################  vimp eg ###########################################

f = open('./x.txt' , 'r')

newvar1 = f.read(1000)


f.close()

print(newvar1)
"""
my name is adarsh 
my age is 22
i live in gwaliori am pursuing btech in cs
i am learning ai ml ds dpl
"""

#==============================================================================



# vvvimp eg 


f = open('./x.txt' , 'r')

newvar1 = f.read(1000)
newvar2 = f.read(10)
newvar3 = f.read(20)

f.close()



print( len(newvar2) , len(newvar3))  #==> 0  0 

# reason of empty str 

# as f.read(100) chala toh usne puer file ke char ko read kr liya , now pointer is at end , to ab wo kuch bhi read nhi kar sakta

# seek and tell mei naur acche se samjh aa jayega 








#-=====================   reading line by line =======================================

f = open('./x.txt' , 'r')

newvar1 = f.readline()
newvar2 = f.readline()
newvar3 = f.readline()

f.close()

print(newvar1 , newvar2 , newvar3)

"""
my name is adarsh 
 my age is 22
 i live in gwaliori am pursuing btech in cs


 line by line read kr lena , pointer ka concept yaha nbhoi hai 

"""
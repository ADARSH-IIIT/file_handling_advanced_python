"""

writing consist of two thing 

writing in a non exisitng file

writing in existion file 



s1 open the file
s2 write in file
s3 close the file 

"""


# writing in non exisiting file 

f = open('./adarsh.txt' , 'w')
# w======> write 

f.write('this is adarsh dwivedi')

f.close()

# this is will write this is adarsh dwivedi in file 

# by these methods  we can only write strings to file , even pure integer tak nhi likh sakte 

# f.write(5)    ===> error dega ki input str nhi hai 




#=========================================   error 
# f.write("\n this is seconfd line ")

# f.write("\n this is seconfd line ")
# ValueError: I/O operation on closed file.


#reason ==>  f.open krne se file harddrive se ram mein aa gyi
# and f.close krne se file ram se wapas harddrive ,mein ja chuki hai , thats why we cant read or write in it 








###########################################################################################################
g = open('/home/adarsh/Desktop/file_handling_python/new.txt' , 'w')

g.writelines(['str1\n' , 'str2' , 'str3\n' , 'str4'])

g.close()

# pure system ke kisi bhi folder , jo ki bina root ke access ho sakta hai , wahan i/o operation kar sakte hai by providing its path
# if we want to multiple lines together we can use \n and put them in a list 

# bus f.write ki jagah f.writelines()  likhna hoga


# or 

# f.write("l1\n")
# f.write("l2\n")
# f.write("l3\n")

# bhi kar sakte hai , but this is not recommended  
#####################################################################################################################################






############################

"""
WRITING IN EXISITING FILE 

if write method ===== >    'w'  toh purana sara content delete ho jayega and new content add ho jayega 
to solve this we use append mode , 'a'
jo ki new contetnt ko new line mein add karega 
"""


k = open('./salman.txt' , 'w')
k.write("this is old line\n")
k.close()


m = open('./salman.txt' , 'a')
m.write("this is new line line")
m.close()
################################################################################################






#################################################    ERROR 
m = open('./error_eg.txt' , 'a')
m.write(5)
m.close()


"""
m.write(5)
TypeError: write() argument must be str, not int

"""

# error 2 nd line mein aaya hai 
# as python interpreter line by line read krta hai toh line 1 sucessfully run ho jayegi and file ka creation ho hi jayega 
# file close python ak garbage collector kar dega 
bien=0
file1 = open("C:\\Users\\user\\Desktop\\rl_human\\test.txt","r") 
file2 = open("C:\\Users\\user\\Desktop\\rl_human\\test2.txt","r+")
data="678991" 
#file2.write(data)
e=""
try:
    while True:
       
       d=file1.readline()
       
       if (d):
        print('read ok')
        
        if (d=='r'):
         print ('rrrrrrrr')
         e=d
        if (d=='e'):
         print ('eeeeeeeee')
         e=d
        #file1.truncate(0)
        file1.close()
        file1 = open("C:\\Users\\user\\Desktop\\rl_human\\test.txt","r+") 
        file1.truncate(0)
        file1.close()
        file1 = open("C:\\Users\\user\\Desktop\\rl_human\\test.txt","r")
       else:
        print("nothing")
       print(e)
       
       #file2.truncate(0)
       file2.write(data)
       file2 .close()
       file2 = open("C:\\Users\\user\\Desktop\\rl_human\\test2.txt","r+") 
except KeyboardInterrupt:
    pass

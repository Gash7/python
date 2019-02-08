file=open(r'C:\Users\AMIT_GORE\Desktop\abc.txt','r+')
abc=file.readlines()
for item in abc:
    print(item)
file.close()
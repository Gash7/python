import json
d={}
d['ashish']={'name':'Ashish',
             'Address':'Pune',
             'Phone':242526}
d['amit']={'name':'Amit',
             'Address':'Pune',
             'Phone':24252}
s=json.dumps(d)

with open(r'C:\Users\AMIT_GORE\Desktop\d.txt','w+') as f:
    f.write(s)
namelist=["safal","Dipsikha","Rashmi","Niraj","Bibek","Ayam","Aayush"]
for name in namelist:
    print(name)

#How to Extract columns from a 2d list
data=[[1,2,3],[4,5,6],[7,8,9]]
column1=[row[0]for row in data]
print(column1)
column2=[row[1]for row in data]
print(column2)
column3=[row[2]for row in data]
print(column3)

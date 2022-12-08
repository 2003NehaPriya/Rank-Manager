#creating a class
class Student:
 def __init__(self,name,marks,r1,upd,update,r2,rank):
     self.name=name
     self.marks=marks
     self.r1=r1
     self.update=update
     self.upd=upd
     self.r2=r2
     self.rank=rank
 
 def display(self):
     print(" ",self.name,"\t\t",self.marks,"\t\t",self.r1,"\t\t",self.update,"\t\t\t",self.upd,"\t\t\t",self.r2,"\t\t",self.rank)
 def disp(self):
     print("NAME:",self.name,"\tMARKS:",self.marks,"\tPREVIOUS RANK:",self.r1,"\t MARKS TO BE UPDATED:",self.update,"\tUPDATED MARKS:",self.upd,"\tUPDATED RANK:",self.r2,"\t JUMP IN RANK:",self.rank)

#initializing the values
name=["Arya","Tarun","Priti","Abhi","Puja","Rohit","Mahi","Roohi","Piyush","Pihu"]
marks=[90,85,75,83,94,78,91,93,89,82]
update=[7,3,5,-1,6,-3,8,-4,1,2]
r1=[1,2,3,4,5,6,7,8,9,10]
r2=[1,2,3,4,5,6,7,8,9,10]
obj=[]
obj1=[]

#calculation of origional rank
m=sorted(marks)
m.reverse()
d1=dict(zip(r1,m))
for i in d1: 
 for j in range(0,10):
     if marks[j]==d1[i]:
         r1[j]=i
#updating the marks
upd=[]
for i in range(0,10):
 upd.append(update[i]+marks[i])
 
#calculation of updated rank
u=sorted(upd)
u.reverse()
d2=dict(zip(r2,u))
for i in d2:
 for j in range(0,10):
     if upd[j]==d2[i]:
         r2[j]=i

#rank up or down
r3=[]
for i in range(0,10):
 r3.append(r1[i]-r2[i])
rank=[]
a=""
for i in r3:
 if i==0:
     a="No change"
     rank.append(a)
 elif i<0:
     a=str(abs(i))
     a="Decrease by "+a
     rank.append(a)
 else:
     a=str(abs(i))
     a="Increase by "+a
     rank.append(a)

#calling the object and printing the values
print("______________________________________________________________________________________________________________________________")
print()
print(" NAME\t\t MARKS\t\tRANK\t MARKS TO BE UPDATED \t UPDATED MARKS\t\t UPDATED RANK\t\t CHANGE IN RANK")
print("______________________________________________________________________________________________________________________________")
print()
for i in range(0,10):
 obj.append(Student(name[i],marks[i],r1[i],upd[i],update[i],r2[i],rank[i]))
for i in range(0,10):
 obj[i].display()

#find name of student with highest mark of after updation
print()
print("...........................................................................................................\"Student With Maximum Marks After Updation in Marks\"........................................................................................................")
print()
p=0
for i in range(0,10):
 if r2[i]==1:
     obj1=Student(name[i],marks[i],r1[i],upd[i],update[i],r2[i],rank[i])
 p=i
for i in range(0,10):
 if i==p:
     obj1.disp()




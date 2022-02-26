#Q2:
#5**9=1953125
#3//2=1
#7//3=2
#7/3=2.3333333333333335
#6==6 = True
#a=20; a+=30; a%=3; print(a) = 2
#True * False = 0
#True & False = False
#True and False = False
#((6>3) and (7<4) or(18==3)) and (9>3)
#True is False = False
#False in 'False' = error
#((True==False) or (False>True)) and (False<=True)


#Q3:
s1="Nice to have it"
s2="here"
print("Question 3. Output : "+s1+" "+s2)


#Q4:
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
index1=a[3]
index2=index1[1]
index3=index2[2]
index=index3[0]
print("Question 4. Result : ",index)


#Q5:
a.insert(0,s1)
a.append(s2)
print("Question 5. Final List : ",a)


#Q6:

numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
print("Question 6. Even Numbers :")
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        break


#Q7:
color_list_1=set(["White","Black","Red"])
color_list_2=set(["Red","Green"])
print("Question 7. Output : ",color_list_1.difference(color_list_2))


#Q8:
def pangram(s):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    for ch in alphabets:
        if ch not in s.lower():
            return False
    return True
st=str(input("Question 8. Enter a String : "))
if(pangram(st)==True):
    print("The entered String is Pangram.")
else:
    print("The entered String is not a Pangram.")


#Q9:
n=input("Question 9. Enter a Number : ")
print("Output : ",(int(n)+int(n*2)+int(n*3)))


#Q10:
number=input("Question 10. Enter the Input : ")
num_split=number.split("#")
for i in range(len(num_split)):
    num_split[i]=num_split[i].split(" ")
ns_x=num_split[0]
ns_y=num_split[1]
x=[]
y=[]
for i in ns_x:
    x.append(int(i))
for i in ns_y:
    y.append(int(i))
print("x = ",x)
print("y = ",y)


#Q11:
word=input("Question 11. Enter words seperated with commas : ")
initial_list=word.split(",")
initial_list.sort()
final_list=','.join(initial_list)
print("Final List : ",final_list)


#Q12:
d={'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
student=d['Student']
marks=d['Marks']
mm=max(marks)
index=marks.index(mm)
print("Question 12. Output : ", student[index])


#Q13:
sentence=input("Question 13. Enter a Sentence : ")
l=0
digi=0
for i in sentence:
    if i.isalpha()==True:
        l+=1
    if i.isdigit()==True:
        digi+=1
print("Number of letters : ",l)
print("Number of digits : ",digi)


#Q14:
d={'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name=d['Name']
subject=d['Subject']
rating=d['Ratings']
input=input("Question 14. Input: ")
x=[]
y=[]
z=[]
length=subject.count(input)
for i in range(length):
    index= subject.index(input)
    x.append(name[index])
    y.append(subject[index])
    z.append(rating[index])
    del name[index]
    del subject[index]
    del rating[index]
new_list= dict()
new_list['Name'] = x
new_list['Subject'] = y
new_list['Ratings'] = z
print("Final List : ",new_list)


#Q15:
n=int(input("Question 15. Enter an Integer: "))
div= [i for i in range(0,n) if(i%7==0)]
print(div)

def divisible_by_7(n):
    for i in range(n): 
        if i%7==0:
            value=True
        else:
            value=False
        print(i,value)

divisible_by_7(n)


#Q16:
import math
x, y = 0, 0
while True:
    move=input("Question 16. Type in UP/DOWN/LEFT/RIGHT #move number: ")
    if move=="":
        break
    else:
        move=move.split(" ")
        
        if move[0]=="UP":
            y=y+int(move[1])
        elif move[0]=="DOWN":
            y=y-int(move[1])
        elif move[0]=="LEFT":
            x=x-int(move[1])
        elif move[0]=="RIGHT":
            x=x+int(move[1])

dist=math.sqrt(x**2 + y**2)
print("Distance : ",dist)


skills = ["foot ball", "sleep", "coding", "singing"]
cv = {}
cv['name']= input("what is your name ?")
cv['age']= int(input("how old are you ?"))
cv['experience']= int(input("how many years of experience"))
cv['skills']= []

counter = 0
for skill in skills:
    print("%d. %s" %(counter+1, skill))
    counter+1

#print(skills['skills'])
#for key in skills:
    #print()

cv['skills'].append(skills[int(input("choose a skill"))-1]) 
print(cv)

cv['skills'].append(skills[int(input("choose a skill"))-1]) 
print(cv)

if cv['age'] < 30 and cv['experience'] > 5 :
    print("accept")

else:
    print("go out")      








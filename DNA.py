DNA=open("DNA.txt").read()
c=0
g=0

for i in range(1,18):
    if DNA[i]=='C':
        num=len(DNA[i])
        c=c+num
    if DNA[i]=='G':
        num1=len(DNA[i])
        g=g+num1
        
per=((c+g)/18.0)*100
print("The percent of C+G is",per,"%")
 

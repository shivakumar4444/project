v=open("present.txt","r")
#opened present file
#fetch data from present textfile store it in to string
s=v.read()
#spliting with dot(.) and store in a list
l=list(s.split("."))
#student name list
studentlist=["shiva","malli","lilli"]
#present days list
presentdays=[]
#percentage list
percent=[]
for i in studentlist:
    nod=l.count(i)
    presentdays.append(nod)
    percent.append(int((nod/30)*100))
#storing result into another file
p=open("result.txt","w")
p.write("    studentname           attendedperiods         percentage\n\n")
for i in range(len(percent)):
    p.write("     ")
    p.write(str(studentlist[i]))
    p.write("                ")
    p.write(str(presentdays[i]*3))
    p.write("                       ")
    p.write(str(percent[i]))
    p.write('%\n')
p.close()

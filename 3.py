t=0
infile=open("t.txt",'r')
outfile=open("out.txt","w")
ala=[line.rstrip() for line in infile]
l=[]
for i in ala:
    print(i[0:i.index('=')])
    ans=input('answer ')
    if ans==i[i.index("=")+1:]:
        t+=1
        l.append(i[0:i.index('=')]+ans+"\n")
n=input("input your name")
print(t)
print(n)
l.append("\n\n"+n+str(t))
outfile.writelines(l)
outfile.close()
infile.close()

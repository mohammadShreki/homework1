def main():
    d=int(input('enter decimal: '))
    b=func(d)
    for i in b:
        print(i,end='')
def func(d):
    binary = []
    while d!=0:
        binary.append(d%2)
        d//=2
    binary.reverse()
    return binary
if __name__=="__main__":
    main()
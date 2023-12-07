def compare(a,b):
    if a>b:
        return 1
    if a == b:
        return 0
    if a<b:
        return -1
    
def main():
    a=int(input())
    b=int(input())
    print(compare(a,b))

if __name__ =="__main__":
    main()
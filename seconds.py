def to_secs(h,m,s):
    s+=(h*3600)+(m*60)
    return s

def main():
    h=int(input())
    m=int(input())
    s=int(input())
    print(to_secs(h,m,s))

if __name__ =="__main__":
    main()
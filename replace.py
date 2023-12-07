def replace(a,b,c):
    #a=phrase="something old, somethhing blue, something borrowed, something new"
    


#def replace(stringname,oldletter,newletter):
    newstring = ''
    for i in range(len(stringname)):
        if stringname[i] == oldletter:
            newstring = newstring + newletter
        else:
            newstring = newstring + stringname[i]
    return newstring

#stringorig = "Hello World!"
#displayname = replace(stringorig,'l','o')
#print displayname


#test(replace("Mississippi", "i", "I") == "MIssIssIppI")

#s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
#test(replace(s, "om", "am") ==
#    "I love spam! Spam is my favorite food. Spam, spam, yum!")

#test(replace(s, "o", "a") ==
#    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Such a triangle exists")
    else:
        print("Such a triangle cannot exist")

def print_names(name1, name2, name3):
    names_list = [name1, name2, name3]
    print(names_list)

triangle(3, 4, 5)  
triangle(1, 1, 3)  


print_names("Leon", "Bob", "Rick") 


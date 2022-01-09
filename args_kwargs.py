# def print_name(a,b,c,d,e):
#     print(a,b,c,d,e)

def funargs(normal, *args, **kwargs): # you can use anything instead of *args as *siddharth
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our personlaties")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

# print_name("Siddharth", "Parth", "Shreyas", "Vats", "Computer")

sid = ["Siddharth", "Parth", "Shreyas", "Vats", "Computer", "Hacker"]
normal = "I am a normal function"
kw = {"Siddharth":"Student", "Hacker":"Computer Teacher", "Vats":"principle"}
funargs(normal, *sid, **kw)
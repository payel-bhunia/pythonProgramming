def outfunc():
    st = 'Hii'
    def innerfunc():
        nonlocal st
        st = 'Hello'
        print(st)
    innerfunc()
    print(st)




print(outfunc())
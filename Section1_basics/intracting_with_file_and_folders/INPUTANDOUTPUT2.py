with open("myfile2.txt",mode="r") as mf2:
    print(mf2.read())
    mf2.seek(0)
    print(mf2.readlines())

    with open("myfile2.txt",mode="a") as mf2:
        mf2.write("\nsix")

with open("myfile3.txt",mode="w") as mf3:
    mf3.write ("hello world")

with open("myfile4.txt",mode="w+") as mf4:
    mf4.write( "hello world")
    mf4.seek(0)
    print(mf4.read())
# this creates a new file and writes hello world in it and then reads it

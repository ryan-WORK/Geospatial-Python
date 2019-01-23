def main():
    mytxt = "./mydata/sample.txt"
    myout = "./output/sample.txt"

    f = open(mytxt, 'r')
    print(f)
    if mytxt == None:
        print("no data")

    fr1 = f.readline()
    fr2 = f.readline()
    fr3 = f.readline()
    print(fr1)
    print(fr2)
    print(fr3)
    frA = f.readlines()
    print(frA)
    print("-----------------------")
    f.close()
    f2 = open(mytxt, 'a')
    f2.write("added 1 line\n")
    f2.write("added 2 lines\n")
    f2.write("added 3 lines\n")
    f2.close()
    f2a = open(mytxt, 'r')
    string = f2a.read()
    print(string)
    f2a.close()
    f2b = open(myout, 'w')
    f2b.write(string)
    f2b.close()



main()

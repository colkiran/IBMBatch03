
FA = open("myfile.txt", "a")

txt = input("Enter the contents of the file :")

FA.write(txt + "\n")

FA.close()
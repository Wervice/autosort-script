import os
for file in os.listdir():
    try:
        ext = file.split(".")[1]
        if not os.path.exists(ext):
            os.mkdir(ext)
        if not os.path.exists(ext+"/"+file):
            open(ext+"/"+file, "wb").write(\
            open(file, "rb").read())
            os.unlink(file)
            print("Moved "+file+" to "+ext+"/"+file)
        else:
            new_file = input("There is already a\
                            file called "+file+"\
             in "+ext+". Please rename "+file+":\n")
            open(ext+"/"+new_file, "wb").write(\
                open(file, "rb").read())
            os.unlink(file)
            print("Moved "+file+" to "+ext+"/"+new_file)
    except IndexError:
        pass
    
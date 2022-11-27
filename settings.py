import sys
if len(sys.argv)==3:
    setting = sys.argv[1]
    language = sys.argv[2]
    if setting=="1" and language=="RO":
        f=open("settings.txt", "r")
        sir= f.read()






        f.write(setting)
        f.write14("\n")
        f.write(language)
        f.close()
    elif setting=="0":
        f = open("settings.txt", "w")
        f.write(setting)
        f.close()

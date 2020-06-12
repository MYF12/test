import  os
pid = os.fork()
if pid==0:
    print("dddd")
else:
    print("aaaa")

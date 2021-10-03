


with open("artifects_01.txt","r") as f:
    text=f.read()

with open("artifects_02.txt","w+") as f:
    text=f.write(text+"added lines")


print("end of stage 3")
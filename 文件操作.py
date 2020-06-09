import  os
def look_pwd():
    pwd = os.getcwd()
    print(os.listdir(pwd))
#f = open("haha.txt","w")
#f.write("haha")
# 1. 获取要复制的文件名
old_file_name = input("请输入一个文件名：")
# 2. 打开要复制的文件
f_read = open("haha.txt","r")
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position]+"bak"+old_file_name[position:]
print("备份的文件名是："+new_file_name)
# 3. 创建一个新文件
f_write = open(new_file_name,"w")
# 4. 从旧文件中读取内容都新文件
cencont = f_read.read()
f_write.write(cencont)
# 5. 关闭两个文件
f_read.close()
f_write.close()
#6. 打印当前目录的文件
look_pwd()

res = input("是否要删除文件？（y or n）").lower()
if res == "y" :
    os.remove(new_file_name)
    print("文件已删除。")
    look_pwd()





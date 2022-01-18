import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ## basic
    subprocess.run(["ls", "-l"])
    for i in [2,5,6,8]:
        subprocess.run(["python", "python_script_101.py", "9", "--x", f"{i}", "--yval", "2"])
    

    ## use output of subprocess
    pro = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = pro.communicate()
    print(out.decode('utf-8'))


    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ
    print('start HW')
    for i in [2,5,6,8]:
        process = subprocess.Popen(["python", "python_script_101.py", "9", "--x", f"{i}", "--yval", "2"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        print(out.split()[-1].decode('utf-8'))
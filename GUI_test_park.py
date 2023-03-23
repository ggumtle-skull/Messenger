from tkinter import *

def btncmd():
    global txt
    print(txt.get("1.0", END))
    txt.delete("1.0", END)

root = Tk()
root.title("GUI TEST")  # GUI 제목
root.geometry("540x380")  # 가로 * 세로

txt = Text(root, width=20, height=3)
txt.pack()

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
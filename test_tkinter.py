import tkinter
import tkinter.filedialog 
import tkinter.messagebox




tk_window=tkinter.Tk()

tk_window.title("test_tkinter")
tk_window.geometry("400x400")
tkinter.Button(master=tk_window,text="Click Button", width=19,bg="red",fg="blue").pack()

#tk_window.withdraw()
#select_file=tkinter.filedialog.askopenfilename()
#filename=tkinter.filedialog.askdirectory()
#print(select_file)
tk_window.mainloop()



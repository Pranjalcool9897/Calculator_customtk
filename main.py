import customtkinter as ctk

##-------------------main------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root=ctk.CTk()

root.geometry("500x580")
root.title("calculator")
root.resizable(False ,False)
##----------constants-----------------------------------------------------------------
font1=("arial",40,"bold")
##============================functions==================================================

def clear():
    pass



##====================Entry=======================
result_entry=ctk.CTkEntry(root,text_font=font1,width=500,height=70,corner_radius=10,border_color="lightgreen")
result_entry.place(x=0,y=0)
##============================buttons============================
button1=ctk.CTkButton(root,text="C",command=clear,text_font=font1,relief="raised",width=130,height=80,fg_color="#b5520b")
button1.place(x=0,y=80)
button2=ctk.CTkButton(root,text="%",command=clear,text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b")
button2.place(x=140,y=80)
button3=ctk.CTkButton(root,text="/",command=clear,text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b")
button3.place(x=260,y=80)
button4=ctk.CTkButton(root,text="x",command=clear,text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b")
button4.place(x=380,y=80)
button5=ctk.CTkButton(root,text="C",command=clear,text_font=font1,relief="raised",width=130,height=80)
button5.place(x=0,y=170)




root.mainloop()

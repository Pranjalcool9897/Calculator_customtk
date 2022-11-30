import customtkinter as ctk

##-------------------main------------------------------
ctk.set_appearance_mode("dark")

root=ctk.CTk()

root.geometry("500x580")
root.title("calculator")
root.resizable(False ,False)
##----------constants-----------------------------------------------------------------
font1=("arial",40,"bold")
i=0
equation=""

##============================functions==================================================

def clear():
    result_entry.delete(0,END)
def show(value):
    global i
    global equation
    equation+=value
    result_entry.insert(i,value)
    i+=1


##====================Entry=====================================================================
result_entry=ctk.CTkEntry(root,text_font=font1,width=500,height=90,corner_radius=10,border_color="lightgreen")
result_entry.place(x=0,y=0)



##============================buttons===============================================================================
button1=ctk.CTkButton(root,text="C",command=clear,text_font=font1,relief="raised",width=130,height=80,fg_color="#b5520b",hover_color="skyblue")
button1.place(x=5,y=100)
button2=ctk.CTkButton(root,text="%",command=lambda :show("%"),text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b",hover_color="skyblue")
button2.place(x=140,y=100)
button3=ctk.CTkButton(root,text="/",command=lambda :show("/"),text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b",hover_color="skyblue")
button3.place(x=260,y=100)
button4=ctk.CTkButton(root,text="x",command=lambda :show("*"),text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b",hover_color="skyblue")
button4.place(x=380,y=100)
button5=ctk.CTkButton(root,text="7",command=lambda :show("7"),text_font=font1,relief="raised",width=130,height=80,fg_color="grey",hover_color="purple")
button5.place(x=5,y=190)
button6=ctk.CTkButton(root,text="8",command=lambda :show("8"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button6.place(x=140,y=190)
button7=ctk.CTkButton(root,text="9",command=lambda :show("9"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button7.place(x=260,y=190)
button8=ctk.CTkButton(root,text="+",command=lambda :show("+"),text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b",hover_color="skyblue")
button8.place(x=380,y=190)
button9=ctk.CTkButton(root,text="4",command=lambda :show("4"),text_font=font1,relief="raised",width=130,height=80,fg_color="grey",hover_color="purple")
button9.place(x=5,y=280)
button10=ctk.CTkButton(root,text="5",command=lambda :show("5"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button10.place(x=140,y=280)
button11=ctk.CTkButton(root,text="6",command=lambda :show("6"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button11.place(x=260,y=280)
button12=ctk.CTkButton(root,text="-",command=lambda :show("-"),text_font=font1,relief="raised",width=110,height=80,fg_color="#b5520b",hover_color="skyblue")
button12.place(x=380,y=280)
button13=ctk.CTkButton(root,text="0",command=lambda :show("0"),text_font=font1,relief="raised",width=130,height=80,fg_color="grey",hover_color="purple")
button13.place(x=5,y=370)
button14=ctk.CTkButton(root,text="1",command=lambda :show("1"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button14.place(x=140,y=370)
button15=ctk.CTkButton(root,text="2",command=lambda :show("2"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button15.place(x=260,y=370)
button16=ctk.CTkButton(root,text="3",command=lambda :show("3"),text_font=font1,relief="raised",width=110,height=80,fg_color="grey",hover_color="purple")
button16.place(x=380,y=370)
button17=ctk.CTkButton(root,text=".",command=lambda :show("."),text_font=font1,relief="raised",width=130,height=115,fg_color="grey",hover_color="purple")
button17.place(x=5,y=460)
button18=ctk.CTkButton(root,text="=",command=clear,text_font=font1,relief="raised",width=350,height=115,fg_color="#b5520b",hover_color="skyblue")
button18.place(x=140,y=460)




root.mainloop()

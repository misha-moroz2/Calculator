import tkinter as tk
withe='#fff'
black='#000'
seru='#828182'
red='#f74343'
blue='#007bc2'
shrift_font=("Arial",24,"bold")
small_font=('Arial',16)
big_font=('Arial',40,'bold')
class Calcylator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title('каЛкульАтор')
        self.dis_frm=self.create_dis_frm()
        self.both_frm=self.create_botn_frme()
        self.totl_exp=''
        self.curent_exp=''
        self.digits={7:(1,1),8:(1,2),9:(1,3),
                    4:(2,1),5:(2,2),6:(2,3),
                    1:(3,1),2:(3,2),3:(3,3),
                    0:(4,1),'.':(4,2)}
        self.operations={'/':'\u00F7','*':'\u00D7','+':'+','-':'-'}
        self.cret_digit_buttn()
        self.cret_operator_buttn()
        self.cret_scr_bttn()
        self.square_btn()
        self.clear_btn()
        self.ravno_btn()
        self.both_frm.rowconfigure(0,weight=1)
        for i in range(1,5):
            self.both_frm.rowconfigure(i,weight=1)
            self.both_frm.columnconfigure(i,weight=1)
        self.totl_lbl,self.label=self.display()
    def create_dis_frm(self):
        frame=tk.Frame(self.window,height=221,bg=seru)
        frame.pack(expand=True,fill='both')
        return frame
    def create_botn_frme(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill='both')
        return frame
    def cret_digit_buttn(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.both_frm,text=str(digit),bg=withe,font=shrift_font,command=lambda x=digit : self.add_to_exp(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    def cret_operator_buttn(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.both_frm,text=symbol,bg=withe,font=shrift_font,command=lambda x=operator : self.add_aper(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def sqrt(self):
        self.curent_exp=str(eval(f'{self.curent_exp}**0.5'))
        self.update_lbl()
    def square(self):
        self.curent_exp=str(eval(f'{self.curent_exp}**2'))
        self.update_lbl()
    def cret_scr_bttn(self):
        buttn=tk.Button(self.both_frm,text="\u221ax",bg=withe,font=shrift_font,command=self.sqrt)
        buttn.grid(row=0,column=3,sticky=tk.NSEW)
    def square_btn(self):
        buttn=tk.Button(self.both_frm,text="x\u00b2",bg=withe,font=shrift_font,command=self.square)
        buttn.grid(row=0,column=2,sticky=tk.NSEW)
    def clear(self):
        self.curent_exp=''
        self.totl_exp=''
        self.update_lbl()
        self.updt_totl_lbl()
    def clear_btn(self):
        buttn=tk.Button(self.both_frm,text="c",bg=withe,font=shrift_font,command=self.clear)
        buttn.grid(row=0,column=1,sticky=tk.NSEW)
    def ravno_btn(self):
        buttn=tk.Button(self.both_frm,text="=",bg=withe,font=shrift_font,command=self.evaluate)
        buttn.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
    def evaluate(self):
        self.totl_exp+=self.curent_exp
        try:
            self.curent_exp=str(eval(self.totl_exp))
            self.totl_exp=''
        except Exception:
            self.curent_exp='Error'
        finally:
            self.update_lbl()
    def add_to_exp(self,value):
        self.curent_exp+=str(value)
        self.update_lbl()
    def add_aper(self,operator):
        self.curent_exp+=operator
        self.totl_exp+=self.curent_exp
        self.curent_exp=''
        self.update_lbl()
        self.updt_totl_lbl()
    def display(self):
        label=tk.Label(self.dis_frm,text=self.curent_exp,bg=withe,fg=red,font=big_font)
        label.pack(expand=True,fill='both')
        totl_lbl=tk.Label(self.dis_frm,text=self.totl_exp,bg=withe,fg=red,font=small_font)
        totl_lbl.pack(expand=True,fill='both')
        return label,totl_lbl
    def updt_totl_lbl(self):
        exp=self.totl_exp
        for opert,simvol in self.operations.items():
            exp=exp.replace(opert,f'{simvol}') 
        self.totl_lbl.config(text=exp)
    def update_lbl(self):
        self.label.config(text=self.curent_exp[:11])
    def run(self):
        self.window.mainloop()
calc=Calcylator()
calc.run()
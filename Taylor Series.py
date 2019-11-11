import tkinter
import tkinter.messagebox
import math

class TaylorSeries():
    def __init__(self):
        self.window = tkinter.Tk()
        
        #----Frames----#
        self.lframe = tkinter.Frame(self.window) #label frame
        self.eframe = tkinter.Frame(self.window) #Entry frame
        
        #----Labels----#
        self.lbl_choose_function = tkinter.Label(self.lframe,
            text = "Enter the function to approximate:")
        
        self.lbl_choose_terms = tkinter.Label(self.lframe,                       
            text = "Enter amount of terms to generate:")
        
        ########
        self.stvar_msg = tkinter.StringVar()
        self.stvar_msg.set("***")
        self.txt_desmos_result = tkinter.Text(self.window, width = 50, height = 20)
        
        #----Entries----#
        self.ent_function = tkinter.Entry(self.eframe, width = 20)
        self.ent_terms = tkinter.Entry(self.eframe, width = 20)

        #----Buttons----#
        self.btn_approximate = tkinter.Button(self.window, text = "Approximate",
            command = self.btn_approximate_event_handler)
        
        #----Pack Widgets----#
        self.lbl_choose_function.pack(side = 'left')
        self.lbl_choose_terms.pack(side = 'right')
        self.lframe.pack()
        
        self.ent_function.pack(side = 'left')
        self.ent_terms.pack(side = 'right')
        self.eframe.pack()
        
        self.btn_approximate.pack()
        self.txt_desmos_result.pack()

        #----Set main message----#
        self.disp_msg = "Choose 'cosine', sine, or 'e' "
        self.stvar_msg.set(self.disp_msg)
        self.txt_desmos_result.insert(1.0, self.disp_msg)
   
        
    def btn_approximate_event_handler(self):
        str_var = str("x")
        self.txt_desmos_result.delete(1.0, tkinter.END)
        self.lst_poly = []
        str_function = str(self.ent_function.get())
        print(str_function)
        self.str_sign = ""
        #self.str_approx = str(input("Enter the equation to approximate:"))
        self.terms = int(self.ent_terms.get())
        
        #----Cosine for Desmos----#                 
        if str_function == "cosine":
            for i in range(self.terms):
                if i % 2 == 0:
                    self.str_sign = "-"
                else:
                    self.str_sign = "+"
                self.str_poly = str("\\left(\\frac{" + str_var +"^{" + str(i * 2) + "}}{" + str(i * 2) + "!}\\right) " + self.str_sign)

                if i == (self.terms -1):
                    self.str_poly = self.str_poly.replace(self.str_sign, "")
                    
                self.lst_poly.append(self.str_poly)
            self.lst_poly.pop(0)
            self.disp_msg = ("1 -", *self.lst_poly)

        #----Sine for Desmos----#
        if str_function == "sine":
            
            for i in range(self.terms):
                k = i * 2 + 1
                if i % 2 == 0:
                    self.str_sign = "-"
                else:
                    self.str_sign = "+"
                self.str_poly = str("\\left(\\frac{x^{" + str(k) + "}}{" + str(k) + "!}\\right) " + "+")

                if i ==(self.terms - 1):
                    self.str_poly = self.str_poly.replace("+", "")
                    
                self.lst_poly.append(self.str_poly)
                
            self.lst_poly.pop(0)
            self.disp_msg = ("x-", *self.lst_poly)
            
        #----e^x for Desmos----#
        if str_function == "e":
            
            for i in range(self.terms):
                self.str_poly = str("\\left(\\frac{x^{" + str(i) + "}}{" + str(i) + "!}\\right) " + "+")

                if i ==(self.terms - 1):
                    self.str_poly = self.str_poly.replace("+", "")
                    
                self.lst_poly.append(self.str_poly)
                
            self.lst_poly.pop(0)
            self.disp_msg = ("1 +", *self.lst_poly)

        #----Code in Progress----#
        '''#----Cosine approximation----#    
        if str_function == "math.cosine":
            
            for i in range(self.terms):
                if i % 2 == 0:
                    self.str_sign = "-"
                else:
                    self.str_sign = "+"
                self.str_poly = str(("(x**" + str(2*i) + ")/(" + str(math.factorial(i * 2)) + ") " + self.str_sign))

                if i == (self.terms -1):
                    self.str_poly = self.str_poly.replace(self.str_sign, "")

                
                self.lst_poly.append(self.str_poly)
                    
            self.lst_poly.pop(0)
            self.disp_msg = ("1 -", *self.lst_poly)
            
            str_eq = self.txt_desmos_result.get(1.0, tkinter.END)
            print(str_eq)'''
        
        #----Set Result String----#
        self.stvar_msg.set(self.disp_msg)
        self.txt_desmos_result.insert(1.0, self.disp_msg)

        #----Code in progress----#
        '''str_eq = self.txt_desmos_result.get(1.0, tkinter.END)
        str_eq = str_eq.replace("{", "")
        str_eq = str_eq.replace("}", "")
        x = 1
        str_answer = eval(str_eq)
        str_answer_fmt = format(str_answer, ".49f")
        print(str_answer_fmt)'''

        
def main():
    window1 = TaylorSeries()

main()

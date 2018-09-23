from tkinter import *
from tkinter import messagebox


from tkinter.messagebox import *

class Calc():

    def __init__(self,master):
        
        

        master.configure(background='light gray')
        master.title("Dprog")
        master.attributes('-topmost', True)
        master.update()

#############################LABELS##################################################################################################################################        

        Label(master, text = "Preis Kalculator\n",bg = "light gray",fg="black",font=('Courier', 16, 'bold underline italic')).grid(row=0,column=1,columnspan=4)
        Label(master, text = "Weitergabe:",bg = "light gray",fg="black",font=("Courier",13,'bold ')).grid(row=1,column=1,sticky=E)
        Label(master, text = "01",bg = "light gray",fg="black",font=("Courier", 13,'bold underline')).grid(row=2,column=1,pady=7,sticky=E)
        Label(master, text = "RIP",bg = "light gray",fg="black",font=("Courier", 13,'bold underline')).grid(row=3,column=1,pady=7,sticky=E)
        Label(master, text = "10 pk1",fg="black",font=("Courier", 13,'bold underline')).grid(row=4,column=1,pady=7,sticky=E)
        Label(master, text = "10 pk2",bg = "light gray",fg="black",font=("Courier", 11,'bold ')).grid(row=5,column=1,pady=7,sticky=E)
        Label(master, text = "11 pk1",fg="black",font=("Courier", 13,'bold underline')).grid(row=6,column=1,pady=7, sticky=E)
        Label(master, text = "11 pk2",bg = "light gray",fg="black",font=("Courier", 11,'bold ')).grid(row=7,column=1,pady=7,sticky=E)

        
        Label(master, text ="      ANBRUCH      ",bg="green4",fg="black",font=("Courier", 15, 'bold underline ')).grid(row=8,column=1,columnspan=4,pady=7)




        Label(master, text = "10 pk1",fg="black",font=("Courier", 13,'bold underline')).grid(row=9,column=1,pady=7,sticky=E)
        Label(master, text = "10 pk2",bg = "light gray",fg="black",font=("Courier", 11,'bold ')).grid(row=10,column=1,pady=7,sticky=E)
        Label(master, text = "11 pk1",fg="black",font=("Courier", 13,'bold underline')).grid(row=11,column=1,pady=7,sticky=E)
        Label(master, text = "11 pk2",bg = "light gray",fg="black",font=("Courier", 11,'bold ')).grid(row=12,column=1,pady=7,sticky=E)
        Label(master, text = "30er",fg="black",font=("Courier", 13,'bold underline')).grid(row=13,pady=7,column=1,sticky=E)
        Label(master, text = "31er",fg="black",font=("Courier", 13,'bold underline')).grid(row=14,pady=7,column=1,sticky=E)
        Label(master, text = "65er",fg="black",font=("Courier", 13,'bold underline')).grid(row=15,pady=7,column=1,sticky=E)



        Label(master, text = "€",bg="yellow",fg="black",font=("Courier", 10)).grid(row=1,column=3,sticky=W)
        Label(master, text = "Nicht\ngerundet",bg="light gray",fg="black",font=("Courier", 8, 'bold underline ')).grid(row=1,column=3,columnspan=3,sticky=W)
        Label(master, text = " ",bg="black",fg="black",font=("Courier", 10)).grid(row=3,column=3,sticky=W)
        Label(master, text = "I",bg="black",fg="black",font=("Courier", 10)).grid(row=4,column=3,sticky=W)
        Label(master, text = "C",bg="black",fg="black",font=("Courier", 10)).grid(row=5,column=3,sticky=W)
        Label(master, text = "H",bg="black",fg="black",font=("Courier", 10)).grid(row=6,column=3,sticky=W)
        Label(master, text = "T",bg="black",fg="black",font=("Courier", 10)).grid(row=7,column=3,sticky=W)
        Label(master, text = "R",bg="black",fg="black",font=("Courier", 10)).grid(row=9,column=3,sticky=W)
        Label(master, text = "U",bg="black",fg="black",font=("Courier", 10)).grid(row=10,column=3,sticky=W)
        Label(master, text = "N",bg="black",fg="black",font=("Courier", 10)).grid(row=11,column=3,sticky=W)
        Label(master, text = "D",bg="black",fg="black",font=("Courier", 10)).grid(row=12,column=3,sticky=W)
        Label(master, text = " ",bg="black",fg="black",font=("Courier", 10)).grid(row=13,column=3,sticky=W)
        Label(master, text = " ",bg="black",fg="black",font=("Courier", 10)).grid(row=14,column=3,sticky=W)
        Label(master, text = " ",bg="black",fg="black",font=("Courier", 10)).grid(row=15,column=3,sticky=W)

############################################### ENTRYS RUND #######################################################################
        self.Preis = Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank = Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank1 = Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank2 =  Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank3 =  Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank4 =  Entry (master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank5 =  Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank6 =  Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank7 =  Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank8 = Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank9 =  Entry(master, font = "Helvetica 15 bold",width=5,fg="red")
        self.blank10 = Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank11 =  Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")
        self.blank12 = Entry(master, font = "Helvetica 15 bold",width=5,bg="blue",fg="white")

#########################################ENTRYS NRUND ##############################################################################
        self.blankn = Entry(master,width=4)
        self.blank1n = Entry(master,width=4)
        self.blank2n =  Entry(master,width=4)
        self.blank3n = Entry(master,width=4)
        self.blank4n =  Entry(master,width=4)
        self.blank5n =  Entry(master,width=4)

        self.blank6n =  Entry(master,width=4)
        self.blank7n =  Entry(master,width=4)
        self.blank8n = Entry(master,width=4)
        self.blank9n =  Entry(master,width=4)

        self.blank10n = Entry(master,width=4)
        self.blank11n =  Entry(master,width=4)
        self.blank12n = Entry(master,width=5)
##########################################################################################################################################
            
        self.fields = (self.blank,self.blankn,self.blank1,self.blank2,self.blank3,self.blank4,self.blank5,self.blank6,self.blank7,self.blank8,
        self.blank9,self.blank10,self.blank11,self.blank12,self.blank1n,self.blank2n,self.blank3n,self.blank4n,
                  self.blank5n,self.blank6n,self.blank7n,self.blank8n,self.blank9n,self.blank10n,self.blank11n,self.blank12n)
###### ALIGNMENT         ###gerundet
        self.Preis.grid(row=1, column=2)
        self.blank.grid(row=2, column=2)
        self.blank1.grid(row=3, column=2)
        self.blank2.grid(row=4, column=2)
        self.blank3.grid(row=5, column=2)
        self.blank4.grid(row=6, column=2)
        self.blank5.grid(row=7, column=2)

        self.blank6.grid(row=9, column=2)
        self.blank7.grid(row=10, column=2)
        self.blank8.grid(row=11, column=2)
        self.blank9.grid(row=12, column=2)
        self.blank10.grid(row=13, column=2)
        self.blank11.grid(row=14, column=2)
        self.blank12.grid(row=15, column=2)
#### ALIGNMENT        ####nicht Nrundet
        self.blankn.grid(row=2, column=4)
        self.blank1n.grid(row=3, column=4)
        self.blank2n.grid(row=4, column=4)
        self.blank3n.grid(row=5, column=4)
        self.blank4n.grid(row=6, column=4)
        self.blank5n.grid(row=7, column=4)


        self.blank6n.grid(row=9, column=4)
        self.blank7n.grid(row=10, column=4)
        self.blank8n.grid(row=11, column=4)
        self.blank9n.grid(row=12, column=4)
        self.blank10n.grid(row=13, column=4)
        self.blank11n.grid(row=14, column=4)
        self.blank12n.grid(row=15, column=4)
######################## BUTTONS ###################################################################################################
        Button(master, text='Berechnen',command = self.Zajedno ,bg="yellow",fg="black").grid(row=16, column=2, pady=7)

        btn = Button(master, text="Reset",command = self.delete_entries,bg="yellow",fg="black").grid(row=16,column=4,sticky=E)
     

    
    def RundPreis(self,x,y,w):# x = prozent, y = Mesto na GUI, z = nicht gerundet mesto,
        #w = Preis
        preiz = w.get()
        
        
        pajs = preiz.replace(",", ".")

        prizes = float(pajs)

        rip = (prizes)* float(x)
        strRIP = (str(rip))
        
        
        if len(strRIP) == 3:
            strRIP = strRIP[0]+strRIP[1]+strRIP[2]+ "0"
           
        if strRIP[2] =="." and len(strRIP) == 4 and strRIP[3]=="0":
            strRIP = strRIP[0]+strRIP[1]+strRIP[2]+ "0"+"0"

        if strRIP[1] == ".":
                    
            if strRIP[3] == "6" or strRIP[3] == "7" or strRIP[3] == "8":
                rip = strRIP[0] + strRIP[1] + strRIP[2] + "9"
                    
                y.insert(0,rip)
                return rip
            if  strRIP[3]== "9":
                rip = strRIP[0]+strRIP[1]+strRIP[2]+strRIP[3]
                y.insert(0,rip)
                    
                return rip
            if strRIP[3] == "0" or strRIP[3]== "1" or strRIP[3] == "2" or strRIP[3] == "3" or strRIP[3] == "4" or strRIP[3] == "5" :
                
                if strRIP[2] == "0" :
                    prvi = int(strRIP[0])
                    rip = str(prvi -1) +  strRIP[1] +  "9"+"9"
                    y.insert(0,rip)
                    return rip
                   
                drugi = int(strRIP[2]) - 1
                rip =strRIP[0] + strRIP[1] + str(drugi) + "9"
                y.insert(0,rip)
                return rip
        if strRIP[2] == ".":
      
            if len(strRIP) == 4:
                strRIP = strRIP[0]+strRIP[1]+strRIP[2]+strRIP[3]+"0"
         
            if strRIP[4]== "9":
                 
                rip = strRIP[0]+strRIP[1]+strRIP[2]+strRIP[3]+strRIP[3]
                y.insert(0,rip)
                return rip
                    
            if strRIP[4] == "0" or strRIP[4]== "1" or strRIP[4] == "2" or strRIP[4] == "3" or strRIP[4] == "4":
                if strRIP[3] == "0":
                        
                        
                    drugi = int(strRIP[1])
                    rip = strRIP[0] + str(drugi-1) + strRIP[2] + "9" + "9"
                    y.insert(0,rip)
                    return rip
                drugi = int(strRIP[3])
                rip =strRIP[0] + strRIP[1] + strRIP[2] + str(drugi -1) + "9"
                y.insert(0,rip)
                return rip
                           
            if strRIP[4] == "5" or strRIP[4] == "6" or strRIP[4] == "7" or strRIP[4] == "8":
                rip = strRIP[0] + strRIP[1] + strRIP[2] + strRIP[3] + "9"   

                y.insert(0,rip)
                return rip


    def NrundPreis(self,x,y,w):#x = prozent, y = mesto  na gui,
        #w = odkoga preisa da uzne i da kalkulise
        pajs = w.get().replace(",", ".")
        if len(pajs) == 3:
            pajs = pajs[0]+pajs[1]+pajs[2]+ "0"

        PreisCCpk2 =  float(pajs) * float(x)
        y.insert(0,round(PreisCCpk2,3))
        

        
        return(round(PreisCCpk2,3))

    def Zajedno(self):
        pajs = self.Preis.get().replace(",", ".")
        
        if float(pajs)> 0.56:
                
            

            
            self.NrundPreis(1.30,self.blank,self.Preis)#N&F EK  
            self.RundPreis(1.45,self.blank1,self.blank)# RIP PREIS
         
            self.RundPreis(1.45,self.blank2,self.Preis)# CCpk1 preis
            self.NrundPreis(1.45,self.blank2n,self.Preis)#  nrund CCpk1
            
            self.NrundPreis(0.97,self.blank3,self.blank2)#CCpk2 Preis
            self.NrundPreis(0.97,self.blank3n,self.blank2n)# nrund CCpk2
            
         
            self.RundPreis(1.55,self.blank4,self.Preis)#ISpk1 Preis
            self.NrundPreis(1.55,self.blank4n,self.Preis)# nrund ISpk1
            
            self.NrundPreis(0.97,self.blank5,self.blank4)#ISpk2 Preis
            self.NrundPreis(0.97,self.blank5n,self.blank4n)# nrund ISpk2

            
            ##########################################################################
          
            self.RundPreis(1.10,self.blank6,self.blank2)#Anbruch CCpk1
            self.NrundPreis(1.10,self.blank6n,self.blank2n)#nrund
            
            self.NrundPreis(1,self.blank7,self.blank3)#Anbruch CCpk2
            self.NrundPreis(1,self.blank7n,self.blank3n)#nrund
            
            self.RundPreis(1.10,self.blank8,self.blank4)#Anbruch ISpk1
            self.NrundPreis(1.10,self.blank8n,self.blank4n)#nrund
            
            self.NrundPreis(1,self.blank9,self.blank5)#Anbruch ISpk2
            self.NrundPreis(1,self.blank9n,self.blank5n)#nrund
          
            self.RundPreis(1,self.blank10,self.blank2)# 30er preis
            self.NrundPreis(1,self.blank10n,self.blank2n)#nrund
            
            self.RundPreis(1,self.blank11,self.blank4)# 31er
            self.NrundPreis(1,self.blank11n,self.blank4n)#nrund
            
            self.RundPreis(1,self.blank12,self.blank2)# 65er
            self.NrundPreis(1,self.blank12n,self.blank2n)#nrund

        else:

            
            self.NrundPreis(1.30,self.blank,self.Preis)#N&F EK  
            self.RundPreis(1.45,self.blank1,self.blank)# RIP PREIS
         
 
            self.NrundPreis(1.45,self.blank2n,self.Preis)#  nrund CCpk1
            
          
            self.NrundPreis(0.97,self.blank3n,self.blank2n)# nrund CCpk2
            
         

            self.NrundPreis(1.55,self.blank4n,self.Preis)# nrund ISpk1
            
            self.NrundPreis(0.97,self.blank5n,self.blank4n)# nrund ISpk2

            
            ##########################################################################
          
            
            self.NrundPreis(1.10,self.blank6n,self.blank2n)#nrund cc
            
            
            self.NrundPreis(1,self.blank7n,self.blank3n)#nrund cc pk2
            
            
            self.NrundPreis(1.10,self.blank8n,self.blank4n)#nrund is 
            

            self.NrundPreis(1,self.blank9n,self.blank5n)#nrund is pk2
          
            self.NrundPreis(1,self.blank10n,self.blank2n)#nrund 30
            
            self.NrundPreis(1,self.blank11n,self.blank4n)#nrund 31
            
            self.NrundPreis(1,self.blank12n,self.blank2n)#nrund 60

           
           

    def delete_entries(self):
    
      for field in self.fields:
        field.delete(0,END) 

main = Tk()

Darko = Calc(main)


mainloop()

from tkinter import *
from tkinter import messagebox
import sys



class TIC_TAC_TOY:

    def __init__(self,master):

        self.master=master
        self.master.config(bg='powder blue')
        self.master.title('TIC_TAC_TOE GAME')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.key=True


        self.grid_button=[(i,j)    for i in range(1,4) for j in range(3) ]

        self.end_b=Button(self.frame,width=20,height=2,padx=10,command=sys.exit,pady=10,font=(20),relief=GROOVE,text='END',bg='powder blue')
        self.end_b.grid(row=4,column=2)

        self.reset_b=Button(self.frame,width=20,height=2,padx=10,command=self.reset,pady=10,font=(20),relief=GROOVE,text='Reset',bg='powder blue')
        self.reset_b.grid(row=4,column=1)
        
        self.score1=0
        self.score2=0

        self.score_label=Label(self.frame,bg='powder blue',width=22,height=3,padx=6,pady=6
        ,relief=GROOVE,font=(21),text='player1_score: {} \n player2_score: {}'.format(self.score1,self.score2))
        self.score_label.grid(row=4,column=0)


        self.player1_label=Label(self.frame,width=20,height=2,padx=10,
        pady=10,font=(20),relief=GROOVE,text='Player1',bg='powder blue')
        self.player1_label.grid(row=0,column=0)

        self.player2_label=Label(self.frame,width=20,height=2,padx=10,
        pady=10,font=(20),relief=GROOVE,text='Player2',bg='powder blue')


        self.game_label=Label(self.frame,width=20,height=2,padx=10,
        pady=10,font=(20),relief=GROOVE,text='Tic Tac Toe',bg='powder blue')

        self.game_label.grid(row=0,column=1)

        self.stringvar=[StringVar()  for i in range(len(self.grid_button))]

        for i in self.stringvar:
            i.set(self.stringvar.index(i))


        
        
        self.buttons=[Button(self.frame,width=20,height=3,padx=10,pady=20,font=(20),bg='white',textvariable=self.stringvar[i])  

              for i in range(len(self.grid_button))]

             


        # print(self.buttons[0]==self.buttons[1])



        self.buttons[0].config(command=lambda:self.change(0))
        self.buttons[1].config(command=lambda:self.change(1))
        self.buttons[2].config(command=lambda:self.change(2))
        self.buttons[3].config(command=lambda:self.change(3))
        self.buttons[4].config(command=lambda:self.change(4))
        self.buttons[5].config(command=lambda:self.change(5))
        self.buttons[6].config(command=lambda:self.change(6))
        self.buttons[7].config(command=lambda:self.change(7))
        self.buttons[8].config(command=lambda:self.change(8))

     

        
        for i in range(len(self.grid_button)):
            self.buttons[i].grid(row=self.grid_button[i][0],column=self.grid_button[i][1])  
        


        self.position=[False       for _ in self.grid_button[:]]

        self.position2=[False     for _ in self.grid_button[:]]

        

        # all(self.position[:3]) or all(self.position[3:6]) or all(self.position[6:]) or all(self.position[::6]) or all(self.position[1::3]) or all(self.position[2::3]) or all(self.position[::4]) or all(self.position[2:7:2]):



    def player1_wins(self):
        self.player1_win_conditions=[all(self.position[:3]) , all(self.position[3:6]) ,
         all(self.position[6:]) , all(self.position[1::3]),
        all(self.position[::3]),all(self.position[2::3]),
        all(self.position[::4]),all(self.position[2:7:2]) ]


        if any(self.player1_win_conditions):
            for i in self.buttons:
                i['state']='disabled'
        
            messagebox.showinfo('win','player1 win')
            self.score1+=1
            self.score_label['text']="player1: {} \n player2: {}".format(self.score1,self.score2) 

            self.equality1=False

            
            
            # messagebox.showinfo('win','player2 win')

        else:
            self.equality1=True 

        

        

       
    def player2_wins(self):
        self.player2_win_conditions=[all(self.position2[:3]) , all(self.position2[3:6]) ,
         all(self.position2[6:]) , all(self.position2[1::3]),
        all(self.position2[::3]),all(self.position2[2::3]),
        all(self.position2[::4]),all(self.position2[2:7:2]) ]

        if  any(self.player2_win_conditions):

            for i in self.buttons:
                i['state']='disabled' 
            
            messagebox.showinfo('win','player2 win')
            self.score2+=1
            self.score_label['text']="player1: {} \n player2: {}".format(self.score1,self.score2)
            


            self.equality2=False
           
            # messagebox.showinfo('win','player1 win')

        else:
            self.equality2=True
        



    def tie(self):
        tie=[]

        for i in self.position:
            if i:
                tie.append(i)

        for j in self.position2:
            if j:
                tie.append(j)

        if len(tie)==9 and self.equality1==True and self.equality2==True:
            messagebox.showerror('OOps',"that's a Tie ")              

        

       

         
        




        

        

    def reset(self):
        self.key=True
        self.player1_label.grid(row=0,column=0)
        self.player2_label.grid_forget()

        self.position.clear()
        self.position=[False       for _ in self.grid_button[:]]
        self.position2=[False     for _ in self.grid_button[:]]

        for i in self.buttons:
            i['state']='normal'   
        print(self.position)
        for i in self.buttons:
            i.config(text=self.buttons.index(i),bg='white')

        for i in self.stringvar:
            i.set(self.stringvar.index(i))    

         
        

        

    def change(self,n):

        

        



        if self.key:
            
            if self.stringvar[n].get()!='X':

                self.buttons[n].config(bg='red')
                self.stringvar[n].set('X')

                ##################################
                del self.position[n]
                self.position.insert(n,True)
                print('self.position=',self.position)
                ###################################
                


                self.player2_label.grid(row=0,column=2)
                self.player1_label.grid_forget()

                

                self.buttons[n]['state']='disabled'

        else:
            
            if self.stringvar[n].get()!='O':
                self.buttons[n].config(bg='green')
                self.stringvar[n].set('O')

                ########################################
                del self.position2[n]
                self.position2.insert(n,True)
                print('self.position2=',self.position2)
                ##########################################


                self.player1_label.grid(row=0,column=0)
                self.player2_label.grid_forget()

                
                self.buttons[n]['state']='disabled'


        if self.key:
            self.key=False

        else:
            self.key=True

        self.player1_wins()
        self.player2_wins()
        
        self.tie()
         

              







root=Tk()

TIC_TAC_TOY(root)


root.mainloop()
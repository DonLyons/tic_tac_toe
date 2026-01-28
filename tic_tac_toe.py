import tkinter as tk
from tkinter import messagebox
#determine if there is a winner 
def check_winner():
    for combination in [[0,1,2], [3,4,5], [6,7,8], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        #if all 2 positions in a winning combination is the same symbol and not empty then a winner is present
        if buttons[combination[0]]["text"] == buttons[combination[1]]["text"] == buttons[combination[2]]["text"] != "":
            #visually shows a winning combination
            buttons[combination[0]].config(bg="green")
            buttons[combination[1]].config(bg="green")
            buttons[combination[2]].config(bg="green")
            #tells user which player won
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combination[0]]['text']} wins!")
            root.quit() #exits program, could be changed in future

#buttons click event
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player #sets buttons text to players symbol(X or O)
        check_winner() #see if there is a winning combination
        change_player() #next player

def change_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text = f"player {current_player}'s turn")

root = tk.Tk() #create window
root.title("Tic-Tac-Toe") #window title

#create button list
buttons = [] 
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    buttons.append(button)
    
#create grid of buttons
for grid_row in range(3):
    for grid_column in range(3):
        buttons[grid_row * 3 + grid_column].grid(row=grid_row, column=grid_column)

#starts with player X
current_player = "X"
winner = False
label = tk.Label(root, text=f"player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
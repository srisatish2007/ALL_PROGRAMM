from customtkinter import *

root = CTk()
root.geometry("550x630")
lab1 = CTkLabel(
    root, text="", width=500, height=580, fg_color="#32f4ca", corner_radius=20
)
lab1.place(x=25, y=25)
text_2 = "#272727"
fg_2 = "#9eff00"
#################################################
lab2 = CTkLabel(
    lab1,
    text="",
    width=450,
    height=530,
    fg_color="white",
    corner_radius=20,
)
lab2.place(x=25, y=25)

player_1 = ""
player_2 = ""
but_val_1 = ""
but_val_2 = ""
but_val_3 = ""
but_val_4 = ""
but_val_5 = ""
but_val_6 = ""
but_val_7 = ""
but_val_8 = ""
but_val_9 = ""
iteration = 0
SUB = 0
white = "#ff8c04"
orange = "#02fff0"
#################################################
lab_GAM = CTkLabel(
    lab2,
    text="TIC-TAC-TOE GAME!",
    text_color="#272727",
    width=150,
    height=30,
    fg_color="#9eff00",  # 272727
    corner_radius=20,
    font=("helvetica", 18, "bold"),
)
lab_GAM.place(x=125, y=10)

lab_det = CTkLabel(
    lab2,
    text="PLAYER DETAILS",
    text_color="white",
    width=80,
    height=30,
    fg_color="orange",
    corner_radius=20,
    font=("helvetica", 18, "bold"),
)
lab_det.place(x=135, y=135)

entry_1 = CTkEntry(
    lab2,
    placeholder_text="Player Name (X)",
    corner_radius=15,
    fg_color="grey",
    width=140,
    placeholder_text_color="white",
    font=("helvetica", 15, "bold"),
    text_color="white",
    border_color="orange",
    border_width=2.9,

)
entry_1.place(x=55, y=180)

entry_2 = CTkEntry(
    lab2,
    placeholder_text="Player Name (O)",
    corner_radius=15,
    width=142,
    fg_color="grey",
    placeholder_text_color="white",
    font=("helvetica", 15, "bold"),
    text_color="white",
    border_color="orange",
    border_width=2.9,
)
entry_2.place(x=255, y=180)


def entry():
    global player_1, player_2
    player_1 = entry_1.get()
    player_1=player_1.upper()
    player_2 = entry_2.get()
    player_2=player_2.upper()
    main()


sub_but = CTkButton(
    lab2,
    text="Submit",
    text_color="white",
    fg_color="#32f4ca",
    font=("Helvetica", 18, "bold"),
    corner_radius=15,
    border_width=2.9,
    border_color="orange",
    hover_color="orange",
    command=entry,
)
sub_but.place(x=155, y=220)

#################################################

def main():

    entry_2.place(x=255, y=90)
    entry_1.place(x=55, y=90)
    sub_but.place(x=155, y=130)
    lab_det.place(x=135, y=45)

    def color_changer(but_num1, but_num2, but_num3, name):
        if name == "X":
            win_name = "WINNER : " + player_1
        else:
            win_name = "WINNER : " + player_2
        if but_num1 == 1:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_1.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 2:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_2.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 3:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_3.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 4:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_4.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 5:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_5.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 6:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_6.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 7:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_7.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 8:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_8.configure(text_color=text_2, fg_color=fg_2)
        if but_num1 == 9:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_9.configure(text_color=text_2, fg_color=fg_2)

        #################################################################

        if but_num2 == 1:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_1.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 2:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_2.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 3:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_3.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 4:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_4.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 5:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )

            lab_fin.place(x=125, y=165)
            but_5.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 6:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_6.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 7:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_7.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 8:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_8.configure(text_color=text_2, fg_color=fg_2)
        if but_num2 == 9:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_9.configure(text_color=text_2, fg_color=fg_2)

        #################################################################

        if but_num3 == 1:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_1.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 2:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_2.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 3:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_3.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 4:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_4.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 5:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_5.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 6:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_6.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 7:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_7.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 8:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_8.configure(text_color=text_2, fg_color=fg_2)
        if but_num3 == 9:
            lab_fin = CTkLabel(
                lab2,
                text=win_name,
                text_color=white,
                width=80,
                height=30,
                fg_color=orange,
                corner_radius=20,
                font=("helvetica", 18, "bold"),
            )
            lab_fin.place(x=125, y=165)
            but_9.configure(text_color=text_2, fg_color=fg_2)

    # color_changer_calling
    print("hello")

    # button function

    def if_but_1():
        global iteration, but_val_1
        iteration += 1
        if iteration % 2 == 0:
            but_1.configure(text="O", hover=OFF)
            but_val_1 = "O"
        else:
            but_1.configure(text="X", hover=OFF)
            but_val_1 = "X"
        if but_val_1 == but_val_2 == but_val_3 == "X":
            color_changer(1, 2, 3, but_val_1)
        if but_val_1 == but_val_4 == but_val_7 == "X":
            color_changer(1, 4, 7, but_val_1)
        if but_val_1 == but_val_5 == but_val_9 == "X":
            color_changer(1, 5, 9, but_val_1)

        if but_val_1 == but_val_2 == but_val_3 == "O":
            color_changer(1, 2, 3, but_val_1)
        if but_val_1 == but_val_4 == but_val_7 == "O":
            color_changer(1, 4, 7, but_val_1)
        if but_val_1 == but_val_5 == but_val_9 == "O":
            color_changer(1, 5, 9, but_val_1)

    def if_but_2():
        global iteration, but_val_2
        iteration += 1
        if iteration % 2 == 0:
            but_2.configure(text="O", hover=OFF)
            but_val_2 = "O"
        else:
            but_2.configure(text="X", hover=OFF)
            but_val_2 = "X"

        if but_val_1 == but_val_2 == but_val_3 == "X":
            color_changer(1, 2, 3, but_val_2)
        if but_val_2 == but_val_5 == but_val_8 == "X":
            color_changer(2, 5, 8, but_val_2)
        if but_val_1 == but_val_2 == but_val_3 == "O":
            color_changer(1, 2, 3, but_val_2)
        if but_val_2 == but_val_5 == but_val_8 == "O":
            color_changer(2, 5, 8, but_val_2)

    def if_but_3():
        global iteration, but_val_3
        iteration += 1
        if iteration % 2 == 0:
            but_3.configure(text="O", hover=OFF)
            but_val_3 = "O"
        else:
            but_3.configure(text="X", hover=OFF)
            but_val_3 = "X"

        if but_val_1 == but_val_2 == but_val_3 == "X":
            color_changer(1, 2, 3, but_val_3)
        if but_val_3 == but_val_6 == but_val_9 == "X":
            color_changer(3, 6, 9, but_val_3)
        if but_val_3 == but_val_5 == but_val_7 == "X":
            color_changer(3, 5, 7, but_val_3)

        if but_val_1 == but_val_2 == but_val_3 == "O":
            color_changer(1, 2, 3, but_val_3)
        if but_val_3 == but_val_6 == but_val_9 == "O":
            color_changer(3, 6, 9, but_val_3)
        if but_val_3 == but_val_5 == but_val_7 == "O":
            color_changer(3, 5, 7, but_val_3)

    def if_but_4():
        global iteration, but_val_4
        iteration += 1
        if iteration % 2 == 0:
            but_4.configure(text="O", hover=OFF)
            but_val_4 = "O"
        else:
            but_4.configure(text="X", hover=OFF)
            but_val_4 = "X"
        if but_val_4 == but_val_5 == but_val_6 == "X":
            color_changer(4, 5, 6, but_val_4)
        if but_val_1 == but_val_4 == but_val_7 == "X":
            color_changer(1, 4, 7, but_val_4)

        if but_val_4 == but_val_5 == but_val_6 == "O":
            color_changer(4, 5, 6, but_val_4)
        if but_val_1 == but_val_4 == but_val_7 == "O":
            color_changer(1, 4, 7, but_val_4)

    def if_but_5():
        global iteration, but_val_5
        iteration += 1
        if iteration % 2 == 0:
            but_5.configure(text="O", hover=OFF)
            but_val_5 = "O"
        else:
            but_5.configure(text="X", hover=OFF)
            but_val_5 = "X"
        if but_val_4 == but_val_5 == but_val_6 == "X":
            color_changer(4, 5, 6, but_val_5)
        if but_val_2 == but_val_5 == but_val_8 == "X":
            color_changer(2, 5, 8, but_val_5)
        if but_val_1 == but_val_5 == but_val_9 == "X":
            color_changer(1, 5, 9, but_val_5)
        if but_val_3 == but_val_5 == but_val_7 == "X":
            color_changer(3, 5, 7, but_val_5)

        #################################################
        if but_val_4 == but_val_5 == but_val_6 == "O":
            color_changer(4, 5, 6, but_val_5)
        if but_val_2 == but_val_5 == but_val_8 == "O":
            color_changer(2, 5, 8, but_val_5)
        if but_val_1 == but_val_5 == but_val_9 == "O":
            color_changer(1, 5, 9, but_val_5)
        if but_val_3 == but_val_5 == but_val_7 == "O":
            color_changer(3, 5, 7, but_val_5)

    def if_but_6():
        global iteration, but_val_6
        iteration += 1
        if iteration % 2 == 0:
            but_6.configure(text="O", hover=OFF)
            but_val_6 = "O"
        else:
            but_6.configure(text="X", hover=OFF)
            but_val_6 = "X"
        if but_val_4 == but_val_5 == but_val_6 == "X":
            color_changer(4, 5, 6, but_val_6)
        if but_val_3 == but_val_6 == but_val_9 == "X":
            color_changer(3, 6, 9, but_val_6)

        if but_val_4 == but_val_5 == but_val_6 == "O":
            color_changer(4, 5, 6, but_val_6)
        if but_val_3 == but_val_6 == but_val_9 == "O":
            color_changer(3, 6, 9, but_val_6)

    def if_but_7():
        global iteration, but_val_7
        iteration += 1
        if iteration % 2 == 0:
            but_7.configure(text="O", hover=OFF)
            but_val_7 = "O"
        else:
            but_7.configure(text="X", hover=OFF)
            but_val_7 = "X"

        if but_val_8 == but_val_7 == but_val_9 == "X":
            color_changer(8, 7, 9, but_val_7)
        if but_val_1 == but_val_4 == but_val_7 == "X":
            color_changer(1, 4, 7, but_val_7)
        if but_val_3 == but_val_5 == but_val_7 == "X":
            color_changer(3, 5, 7, but_val_7)

        if but_val_8 == but_val_7 == but_val_9 == "O":
            color_changer(8, 7, 9, but_val_7)
        if but_val_1 == but_val_4 == but_val_7 == "O":
            color_changer(1, 4, 7, but_val_7)
        if but_val_3 == but_val_5 == but_val_7 == "O":
            color_changer(3, 5, 7, but_val_7)

    def if_but_8():
        global iteration, but_val_8
        iteration += 1
        if iteration % 2 == 0:
            but_8.configure(text="O", hover=OFF)
            but_val_8 = "O"
        else:
            but_8.configure(text="X", hover=OFF)
            but_val_8 = "X"
        if but_val_8 == but_val_7 == but_val_9 == "X":
            color_changer(8, 7, 9, but_val_8)
        if but_val_2 == but_val_5 == but_val_8 == "X":
            color_changer(2, 5, 8, but_val_8)
        if but_val_3 == but_val_6 == but_val_9 == "X":
            color_changer(3, 6, 9, but_val_8)

        if but_val_8 == but_val_7 == but_val_9 == "O":
            color_changer(8, 7, 9, but_val_8)
        if but_val_2 == but_val_5 == but_val_8 == "O":
            color_changer(2, 5, 8, but_val_8)
        if but_val_3 == but_val_6 == but_val_9 == "O":
            color_changer(3, 6, 9, but_val_8)

    def if_but_9():
        global iteration, but_val_9
        iteration += 1
        if iteration % 2 == 0:
            but_9.configure(text="O", hover=OFF)
            but_val_9 = "O"
        else:
            but_9.configure(text="X", hover=OFF)
            but_val_9 = "X"

        if but_val_8 == but_val_7 == but_val_9 == "X":
            color_changer(7, 8, 9, but_val_9)
        if but_val_1 == but_val_5 == but_val_9 == "X":
            color_changer(1, 5, 9, but_val_9)
        if but_val_8 == but_val_7 == but_val_9 == "O":
            color_changer(7, 8, 9, but_val_9)
        if but_val_1 == but_val_5 == but_val_9 == "O":
            color_changer(1, 5, 9, but_val_9)

    but_7 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_7,
        # font=('helvetica',28,'bold')
    )
    but_7.place(x=105, y=410)

    but_8 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_8,
    )
    but_8.place(x=187, y=410)

    but_9 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_9,
    )
    but_9.place(x=269, y=410)

    but_4 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_4,
    )
    but_4.place(x=105, y=310)

    but_5 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_5,
    )
    but_5.place(x=187, y=310)

    but_6 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_6,
    )
    but_6.place(x=269, y=310)

    but_1 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_1,
    )
    but_1.place(x=105, y=210)

    but_2 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_2,
    )
    but_2.place(x=187, y=210)
    but_3 = CTkButton(
        lab2,
        text="",
        height=95,
        width=75,
        font=("Helvetica", 25, "bold"),
        text_color="#9eff00",
        fg_color="#272727",
        corner_radius=8,
        hover_color="#9eff00",
        command=if_but_3,
    )

    but_3.place(x=269, y=210)
root.mainloop()

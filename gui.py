from tkinter import *
from tkinter import messagebox
import random
import game_logic as logic
import time


class GUI():
    def __init__(self):
        self.window = Tk()
        self.window.title('Rock, Paper, Scissors!')

        self.window.geometry('580x400')
        self.window.config(bg='#0935ce', pady=1, padx=10)  # 082eaf
        self.window.resizable(False, False)

        ## Current Card display:
        self.card_background_photo = PhotoImage(file=r'sprites\Waiting_Question.png').subsample(3, 3)

        ## Display background:
        self.background = Label(image=self.card_background_photo, bg='#0935ce')  # 082eaf
        self.background.grid(row=2, column=2, pady=10)

        self.scoreboard = Label(text=f"Score:\n {logic.score}", fg='pink', bg='#0935ce',
                                font=("Calibri", 16, "bold"), pady=4)
        self.scoreboard.grid(row=2, column=3)

        ## Button sprites:
        self.rock_photo = PhotoImage(file=r'sprites\rock_button.png')
        self.rock_photo = self.rock_photo.subsample(6, 6)

        self.paper_photo = PhotoImage(file=r'sprites\paper_button.png')
        self.paper_photo = self.paper_photo.subsample(6, 6)

        self.scissors_photo = PhotoImage(file=r'sprites\scissors_button.png')
        self.scissors_photo = self.scissors_photo.subsample(8, 8)

        ## Buttons:
        self.choose_rock_button = Button(text='Rock', image=self.rock_photo,
                                         command=lambda: self.user_choice('r'),
                                         width=72, height=55)
        self.choose_rock_button.grid(row=3, column=1, pady=1)

        self.choose_paper_button = Button(text='Paper', image=self.paper_photo,
                                          command=lambda: self.user_choice('p'),
                                          width=72, height=55)
        self.choose_paper_button.grid(row=3, column=2, pady=1)

        self.choose_scissors_button = Button(text='Scissors', image=self.scissors_photo,
                                             command=lambda: self.user_choice('s'),
                                             width=72, height=55)
        self.choose_scissors_button.grid(row=3, column=3, pady=1)

        self.quit_game = Button(text='Quit', command=lambda: self.save_score('y')) #self.window.destroy
        self.quit_game.grid(row=4, column=2, pady=1)


        ## Card sprites:

        # LOADING - Waiting for cpu choice #
        self.loading_both = PhotoImage(file=r'sprites\Waiting_Question.png').subsample(3, 3)
        self.rock_loading = PhotoImage(file=r'sprites\Rock_Question.png').subsample(3, 3)
        self.paper_loading = PhotoImage(file=r'sprites\Paper_Question.png').subsample(3, 3)
        self.scissors_loading = PhotoImage(file=r'sprites\Scissors_Question.png').subsample(3, 3)

        # ROCK Results #
        self.rock_win = PhotoImage(file=r'sprites\Rock_Win_Result.png').subsample(3, 3)
        self.rock_lose = PhotoImage(file=r'sprites\Rock_Lose_Result.png').subsample(3, 3)
        self.rock_draw = PhotoImage(file=r'sprites\Rock_Draw_Result.png').subsample(3, 3)

        # PAPER Results #
        self.paper_win = PhotoImage(file=r'sprites\Paper_Win_Result.png').subsample(3, 3)
        self.paper_lose = PhotoImage(file=r'sprites\Paper_Lose_Result.png').subsample(3, 3)
        self.paper_draw = PhotoImage(file=r'sprites\Paper_Draw__Result.png').subsample(3, 3)

        # SCISSORS Results #
        self.scissors_win = PhotoImage(file=r'sprites\Scissors_Win_Result.png').subsample(3, 3)
        self.scissors_lose = PhotoImage(file=r'sprites\Scissors_Lose_Result.png').subsample(3, 3)
        self.scissors_draw = PhotoImage(file=r'sprites\Scissors_Draw_Result.png').subsample(3, 3)

        ## Display text:
        self.banner = Canvas(width=400, height=50)
        self.banner.grid(row=1, column=2, pady=10)

        self.banner_text = Label(text="Jan! Ken! Pon!", fg='black', font=("Calibri", 18, "bold"))
        self.banner_text.grid(row=1, column=2, pady=1)


        ## Result lists:
        self.rock_results = [self.rock_win, self.rock_lose, self.rock_draw]
        self.paper_results = [self.paper_win, self.paper_lose, self.paper_draw]
        self.scissors_results = [self.scissors_win, self.scissors_lose, self.scissors_draw]
        # double index possible?

        self.window.mainloop()

    ## MAJOR Functions:
    def cpu_choice(self):
        cpu_play = random.choice(logic.gambits)
        time.sleep(2)
        return cpu_play

    def user_choice(self, user_play):
        print(user_play)
        # call function to update BG, send user_play
        self.game_bg_update(user_play)

        cpu_current_play = self.cpu_choice()
        print(user_play, cpu_current_play)

        result = logic.find_status(user_play, cpu_current_play)
        # call function to update BG, send result and user_play
        self.game_bg_update(user_play, result)
        print(f"{result}\n")

        logic.get_score(result)
        self.scoreboard.config(text=f"Score: {logic.score}")
        return result

    def game_bg_update(self, user_play, result=-10):
        if user_play == 'r':
            if result == -10:
                self.background.config(image=self.rock_loading)
                self.banner_text.config(text="Jan! Ken! ...Pon?", fg='black', font=("Calibri", 18, "bold"))
            elif result == 1:
                self.background.config(image=self.rock_win)
                self.banner_text.config(text="You WIN! ^_^", fg='green', font=("Calibri", 18, "bold"))
            elif result == -1:
                self.background.config(image=self.rock_lose)
                self.banner_text.config(text="You LOSE! :'(", fg='#b92f2d', font=("Calibri", 18, "bold"))
            else:
                self.background.config(image=self.rock_draw)
                self.banner_text.config(text="It's a draw!", fg='#3b77d3', font=("Calibri", 18, "bold"))
        elif user_play == 'p':
            if result == -10:
                self.background.config(image=self.paper_loading)
                self.banner_text.config(text="Jan! Ken! ...Pon?", fg='black', font=("Calibri", 18, "bold"))
            elif result == 1:
                self.background.config(image=self.paper_win)
                self.banner_text.config(text="You WIN! ^_^", fg='green', font=("Calibri", 18, "bold"))
            elif result == -1:
                self.background.config(image=self.paper_lose)
                self.banner_text.config(text="You LOSE! :'(", fg='#b92f2d', font=("Calibri", 18, "bold"))
            else:
                self.background.config(image=self.paper_draw)
                self.banner_text.config(text="It's a draw!", fg='#3b77d3', font=("Calibri", 18, "bold"))
        else:
            if result == -10:
                self.background.config(image=self.scissors_loading)
                self.banner_text.config(text="Jan! Ken! ...Pon?", fg='black', font=("Calibri", 18, "bold"))
            elif result == 1:
                self.background.config(image=self.scissors_win)
                self.banner_text.config(text="You WIN! ^_^", fg='green', font=("Calibri", 18, "bold"))
            elif result == -1:
                self.background.config(image=self.scissors_lose)
                self.banner_text.config(text="You LOSE! :'(", fg='#b92f2d', font=("Calibri", 18, "bold"))
            else:
                self.background.config(image=self.scissors_draw)
                self.banner_text.config(text="It's a draw!", fg='#3b77d3', font=("Calibri", 18, "bold"))

        self.window.update()

    def save_score(self, quit_game):
        if quit_game == 'y':
            answer = messagebox.askyesno('Save Score', "Wait! Do you want to save your score?")
            if answer:
                self.scoreboard.config(text="Loading...")
                with open ("scoreboard.txt", "a") as file:
                    file.write(f"{logic.score}")
                self.scoreboard.config(text="Saved!")
                self.window.update()

                time.sleep(2)
                self.window.destroy()
            else:
                self.window.destroy()

            # YAY! Thanks Greg! :)
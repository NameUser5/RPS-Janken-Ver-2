from tkinter import *
import random
import game_logic as logic

# window = Tk()
# window.title('Rock, Paper, Scissors!')
#
# window.geometry('580x400')
# window.config(bg='#0935ce', pady=10, padx=10) #082eaf
# window.resizable(False, False)

class GUI():
    def __init__(self):
        self.window = Tk()
        self.window.title('Rock, Paper, Scissors!')

        self.window.geometry('580x400')
        self.window.config(bg='#0935ce', pady=10, padx=10)  # 082eaf
        self.window.resizable(False, False)


        ## Current Card display:
        self.card_background_photo = PhotoImage(file=r'sprites\Waiting_Question.png')  # change this to list w idx
        self.card_background_photo = self.card_background_photo.subsample(3, 3)

        ##Display background:
        self.background = Label(image=self.card_background_photo, bg='#0935ce')  # 082eaf
        self.background.grid(row=2, column=2, pady=10)

        ## Button sprites:
        self.rock_photo = PhotoImage(file=r'sprites\rock_button.png')
        self.rock_photo = self.rock_photo.subsample(6, 6)

        self.paper_photo = PhotoImage(file=r'sprites\paper_button.png')
        self.paper_photo = self.paper_photo.subsample(6, 6)

        self.scissors_photo = PhotoImage(file=r'sprites\scissors_button.png')
        self.scissors_photo = self.scissors_photo.subsample(8, 8)

        ## Buttons:
        self.choose_rock_button = Button(text='Rock', image=self.rock_photo, width=72, height=55)  # after img: command=lambda: user_choice('r'),
        self.choose_rock_button.grid(row=3, column=1, pady=1)

        self.choose_paper_button = Button(text='Paper', image=self.paper_photo, width=72, height=55)  # command=lambda: user_choice('p'),
        self.choose_paper_button.grid(row=3, column=2, pady=1)

        self.choose_scissors_button = Button(text='Scissors', image=self.scissors_photo, width=72, height=55)  # command=lambda: user_choice('s'),
        self.choose_scissors_button.grid(row=3, column=3, pady=1)

        self.quit_game = Button(text='Quit', command=self.window.destroy)
        self.quit_game.grid(row=4, column=2, pady=1)

        ## Card sprites:

        # LOADING - Waiting for cpu choice #
        self.loading_both = PhotoImage(file=r'sprites\Waiting_Question.png')
        self.rock_loading = PhotoImage(file=r'sprites\Rock_Question.png')
        self.paper_loading = PhotoImage(file=r'sprites\Paper_Question.png')
        self.scissors_loading = PhotoImage(file=r'sprites\Scissors_Question.png')

        # ROCK Results #
        self.rock_win = PhotoImage(file=r'sprites\Rock_Win_Result.png')
        self.rock_lose = PhotoImage(file=r'sprites\Rock_Lose_Result.png')
        self.rock_draw = PhotoImage(file=r'sprites\Rock_Draw_Result.png')

        # PAPER Results #
        self.paper_win = PhotoImage(file=r'sprites\Paper_Win_Result.png')
        self.paper_lose = PhotoImage(file=r'sprites\Paper_Lose_Result.png')
        self.paper_draw = PhotoImage(file=r'sprites\Paper_Draw__Result.png')

        # SCISSORS Results #
        self.scissors_win = PhotoImage(file=r'sprites\Scissors_Win_Result.png')
        self.scissors_lose = PhotoImage(file=r'sprites\Scissors_Lose_Result.png')
        self.scissors_draw = PhotoImage(file=r'sprites\Scissors_Draw_Result.png')


        ##Display text:
        self.banner = Canvas(width=400, height=50)
        self.banner.grid(row=1, column=2, pady=10)

        self.banner_text = Label(text="Jan! Ken! Pon!", fg='black')
        self.banner_text.grid(row=1, column=2, pady=1)

        self.you_win_banner = PhotoImage(file=r'sprites\Victory text.png')
        self.you_lose_banner = PhotoImage(file=r'sprites\Defeat text.png')
        
        ## Result lists:
        self.rock_results = [self.rock_win, self.rock_lose, self.rock_draw]
        self.paper_results = [self.paper_win, self.paper_lose, self.paper_draw]
        self.scissors_results = [self.scissors_win, self.scissors_lose, self.scissors_draw]
# double index possible?

        self.window.mainloop()

    def cpu_choice(self):
        choice = random.choice(logic.gambits)
        return choice
    #
    def user_choice(choice):
        # print(choice)
        cpu_current = choice.cpu_choice()
        result = logic.find_status(choice, cpu_current)
        print(result)
        return result

# window.mainloop()
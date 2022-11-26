import tkinter as tk
from password_checker import check_password
from problems import problems, get_challenge
from random import randint


class App(tk.Tk):
    def __init__(self, test_text, group_no):
        super().__init__()

        # initialize with group number with problem and set max attempt
        self.problem = test_text
        self.group_no = group_no
        self.att = 3

        # Set title name and window size
        self.title(f"Decrypt Game")
        self.geometry("720x550")
        self.resizable(0, 0)

        # Frame 1
        self.pack_frame = tk.Frame(self)
        self.pack_frame.pack(pady=10)

        # Title
        self.label = tk.Label(
            self.pack_frame, text='เกมถอดรหัส', font=("Tahoma", 48))
        self.label.pack()

        self.problems_group = tk.Label(
            self.pack_frame, text="รหัสที่กลุ่มคุณต้องถอดคือ ? ", font=("Tahoma", 24))
        self.problems_group.pack()

        # Group Name
        self.group_name = tk.Label(
            self.pack_frame, text=test_text, font=("Tahoma", 36))
        self.group_name.pack()

        # Frame 2
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=10)

        # check password fill
        self.passtxt = tk.Label(
            self.grid_frame, text='รหัสผ่าน', font=("Tahoma", 24))
        self.passtxt.grid(row=0, column=0, padx=20)

        # Fill password textbox
        self.get_password = tk.StringVar()
        self.textbox = tk.Entry(self.grid_frame,
                                width=10,
                                font=("Tahoma", 24),
                                textvariable=self.get_password)
        self.textbox.grid(row=1, column=0, pady=20)

        # Frame 3
        self.pack_frame2 = tk.Frame(self)
        self.pack_frame2.pack()

        # check password button
        self.password_button = tk.Button(self.pack_frame2,
                                         text='check password',
                                         font=("Tahoma", 16))
        self.password_button['command'] = self.password_checker
        self.password_button.pack(pady=5)

        # Frame 5
        self.pack_frame3 = tk.Frame(self)
        self.pack_frame3.pack(pady=10)

        # Check password
        self.status = tk.StringVar()
        self.status.set("")
        self.status_check = tk.Label(
            self.pack_frame3, textvariable=self.status, font=("Tahoma", 24))
        self.status_check.pack()

        # show attempt
        self.pack_status = tk.Frame(self)
        self.pack_status.pack(side=tk.LEFT)

        self.attempt = tk.StringVar()
        self.attempt.set(f"Attempt : {self.att}")
        self.attempt_left = tk.Label(
            self.pack_status, textvariable=self.attempt, font=("Tahoma", 24))
        self.attempt_left.pack(padx=10)

    def clear_text(self):
        '''
            clear text after 5 seconds
        '''

        self.after(5000, lambda: self.status.set(""))

    def enable_button(self):
        '''
            re-enable button after 5 seconds
        '''

        self.password_button["state"] = "normal"

    def clear_screen(self):
        '''
            clear fill screen
        '''

        self.pack_frame.forget()
        self.grid_frame.forget()
        self.pack_frame.forget()
        self.pack_frame2.forget()
        self.pack_frame3.forget()
        self.pack_status.forget()

    def win(self):
        '''
            random some fun challenge from problems.py
        '''

        self.winning = tk.Frame(self)
        self.winning.pack(expand=True, fill="both")

        self.winning_text = get_challenge()

        self.win_text = tk.Label(
            self.winning, text=self.winning_text, font=("Tahoma", 36), wraplength=700, justify="center")
        self.win_text.pack(expand=True, fill="both")

    def lose(self):
        '''
            if player use all attempt
        '''

        self.losing = tk.Frame(self)
        self.losing.pack(expand=True, fill="both")

        self.lose_text = tk.Label(
            self.losing, text="แย่จังเลย\nคุณไม่สามารถถอดรหัสได้", font=("Tahoma", 36), wraplength=700, justify="center")
        self.lose_text.pack(expand=True, fill="both")

    def password_checker(self):

        # check password from user

        if(check_password(self.problem, self.textbox.get())):
            self.clear_screen()
            self.win()
        else:
            self.status.set("Wrong Password")
            self.password_button["state"] = "disable"
            self.att -= 1
            if(self.att > 0):
                self.attempt.set(f"Attempt : {self.att}")
                self.after(5000, self.enable_button)
                self.clear_text()
            else:
                self.clear_screen()
                self.lose()


if __name__ == "__main__":

    '''
        Main program goes here.
    '''
    n = randint(1, 10)
    App(problems[n-1], n).mainloop()

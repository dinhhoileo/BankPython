from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self, account,page_login):
        self.account = account
        self.page_login=page_login

    def check_login(self):
        user_name =self.page_login.input_email.get()  # Lấy giá trị từ widget entry_email
        password =self.page_login.input_password.get()  # Lấy giá trị từ widget entry_password

        if not self.account:
            messagebox.showinfo("Thông báo", "Bạn chưa đăng ký")
        elif user_name in self.account and self.account[user_name] == password:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công")

        else:
            messagebox.showinfo("Thông báo", "Đăng nhập thất bại")

class Register:
    def __init__(self, account,page_login):
        self.account = account
        self.page_login=page_login

    def add(self, user_name, password):
        if user_name in self.account:
            messagebox.showinfo("Thông báo", "Tài khoản đã tồn tại")
        else:
            self.account[user_name] = password
            messagebox.showinfo("Thông báo", "Đăng ký thành công")
            home_page=HomePage()

    def register(self):
        user_name = self.page_login.input_email.get()  # Lấy giá trị từ widget entry_email
        password = self.page_login.input_password.get()  # Lấy giá trị từ widget entry_password
        self.add(user_name, password)


class PageLogin:
    def __init__(self):
        self.app = Tk()
        self.app.title("BTC")
        self.app.iconbitmap("bitcoin.ico")
        self.app.geometry("500x350")
        self.welcome_label = Label(self.app, text="Welcome Back!", font=("Arial", 25), fg="orange",anchor="center")
        self.welcome_label.pack()

        # Email
        self.email_label = Label(self.app, text="EMAIL", font=("Arial", 10), fg="#FF6699",anchor="w")
        self.email_label.place(x=9, y=127)
        self.input_email = Entry(self.app, width=35)
        self.input_email.place(x=100, y=127)

        # Password
        self.password_label = Label(self.app, text="PASSWORD", font=("Arial", 10), fg="#FF6699",anchor="w")
        self.password_label.place(x=9, y=178)
        self.input_password = Entry(self.app, width=35)
        self.input_password.place(x=100, y=183)

        # Dữ liệu người dùng database
        self.account_data = {}
        self.register_account = Register(self.account_data,self)
        self.login_account = Login(self.account_data,self)

        # Login button
        self.login_button = Button(self.app, text="LOGIN", command=self.login_account.check_login, bg="orange", fg="red")
        self.login_button.place(x=276, y=212)

        # Register button
        self.register_button = Button(self.app, text="REGISTER", command=self.register_account.register, bg="orange", fg="red")
        self.register_button.place(x=190, y=212)
        self.app.mainloop()

class HomePage:
    def __init__(self):
        self.app =Tk()
        self.app.title("Home Page")
        self.app.iconbitmap("home page.ico")
        test_label = Label(self.app,text="Hello this is new page").pack()
        self.app.mainloop()
    def logout(self):
        self.app.destroy()
        login_page = PageLogin()
        

class App:
    def __init__(self):
        self.new_app = PageLogin()


if __name__ == "__main__":
    new_app = App()

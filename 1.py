from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class HomePage:
    def __init__(self):
        self.app = Tk()
        self.app.title("BTC")
        self.app.iconbitmap("bitcoin.ico")
        self.app.geometry("500x350")
        back_ground_image = ImageTk.PhotoImage(file="background.png")
        back_ground_label = Label(self.app, image=back_ground_image)
        back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)  # Đặt hình ảnh nền kích thước toàn bộ giao diện

        self.account_data = {}
        self.page_login = PageLogin(self.account_data)

        self.page_login.show_login()

        self.app.mainloop()

    def show_balance(self):
        # Đoạn mã để hiển thị số dư
        pass


class Login:
    def __init__(self, account, page_login):
        self.account = account
        self.page_login = page_login

    def check_login(self):
        user_name = self.page_login.input_email.get()  # Lấy giá trị từ widget entry_email
        password = self.page_login.input_password.get()  # Lấy giá trị từ widget entry_password

        if not self.account:
            messagebox.showinfo("Thông báo", "Bạn chưa đăng ký")
        elif user_name in self.account and self.account[user_name] == password:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công")
            self.page_login.app.destroy()
            home_page = HomePage()
            home_page.show_balance()  # Hiển thị số dư
        else:
            messagebox.showinfo("Thông báo", "Đăng nhập thất bại")


class Register:
    def __init__(self, account, page_login):
        self.account = account
        self.page_login = page_login

    def add(self, user_name, password):
        if user_name in self.account:
            messagebox.showinfo("Thông báo", "Tài khoản đã tồn tại")
        else:
            self.account[user_name] = password
            messagebox.showinfo("Thông báo", "Đăng ký thành công")
            self.page_login.app.destroy()
            home_page = HomePage()
            home_page.show_balance()  # Hiển thị số dư

    def register(self):
        user_name = self.page_login.input_email.get()  # Lấy giá trị từ widget entry_email
        password = self.page_login.input_password.get()  # Lấy giá trị từ widget entry_password
        self.add(user_name, password)


class PageLogin:
    def __init__(self, account_data):
        self.account_data = account_data

    def show_login(self):
        self.app = Tk()
        self.app.title("BTC")
        self.app.iconbitmap("bitcoin.ico")
        self.app.geometry("500x350")
        back_ground_image = ImageTk.PhotoImage(file="background.png")
        back_ground_label = Label(self.app, image=back_ground_image)
        back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)  # Đặt hình ảnh nền kích thước toàn bộ giao diện
        self.welcome_label = Label(self.app, text="WELCOME BACK!", font=("Arial", 25), fg="orange",bg="#19141A", anchor="center")
        self.welcome_label.pack()

        # Email
        self.email_label = Label(self.app, text="EMAIL", font=("Arial", 10), fg="white",bg="#613A29", anchor="w")
        self.email_label.place(x=9, y=127)
        self.input_email = Entry(self.app, width=35)
        self.input_email.place(x=100, y=127)

        # Password
        self.password_label = Label(self.app, text="PASSWORD", font=("Arial", 10), fg="white",bg="#A36953", anchor="w")
        self.password_label.place(x=9, y=178)
        self.input_password = Entry(self.app, width=35, show="*")
        self.input_password.place(x=100, y=183)

        self.register_account = Register(self.account_data, self)
        self.login_account = Login(self.account_data, self)

        # Login button
        self.login_button = Button(self.app, text="LOGIN", command=self.login_account.check_login, bg="#9400D3",fg="white")
        self.login_button.place(x=276, y=212)

        # Register button
        self.register_button = Button(self.app, text="REGISTER", command=self.register_account.register, bg="#9400D3",fg="white")
        self.register_button.place(x=190, y=212)
        self.app.mainloop()


# Sử dụng class HomePage để bắt đầu chạy ứng dụng
home_page = HomePage()
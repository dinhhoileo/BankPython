from tkinter import *
from PIL import ImageTk
from tkinter import messagebox  

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
    def __init__(self):
        self.app = Tk()
        self.app.title("BTC")
        self.app.iconbitmap("bitcoin.ico")
        self.app.geometry("500x350")
        back_ground_image = ImageTk.PhotoImage(file="background.png")
        back_ground_label = Label(self.app, image=back_ground_image)
        back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)  # Đặt hình ảnh nền kích thước toàn bộ giao diện
        self.welcome_label = Label(self.app, text="WELCOME BACK!", font=("Arial", 25), fg="orange",bg="#19141A", anchor="center")
        self.welcome_label.pack()
        # Dữ liệu người dùng database
        self.account_data = {}
        self.register_account = Register(self.account_data, self)
        self.login_account = Login(self.account_data, self)

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

        # Login button
        self.login_button = Button(self.app, text="LOGIN", command=self.login_account.check_login, bg="#9400D3",fg="white")
        self.login_button.place(x=276, y=212)

        # Register button
        self.register_button = Button(self.app, text="REGISTER", command=self.register_account.register, bg="#9400D3",fg="white")
        self.register_button.place(x=190, y=212)
        self.app.mainloop()
class HomePage:
    def __init__(self):
        self.app = Tk()
        self.app.geometry("900x400")
        self.app.title("Home Page")
        self.app.iconbitmap("home page.ico")
        
        balance_value = 0  # Số dư cụ thể để hiển thị
        self.balance_entry = Entry(self.app, width=10, justify="center",font=("Arial",24))
        self.balance_entry.insert(0, balance_value)  # Chèn giá trị số dư vào ô vuông
        self.balance_entry.place(x=400, y=63)
        
        deposit_button = Button(self.app, text="Deposit", font=("Arial", 13), fg="Blue", width=8)
        deposit_button.place(x=250, y=123)
        
        withdraw_button = Button(self.app, text="Withdraw", font=("Arial", 13), fg="Blue", width=8)
        withdraw_button.place(x=423, y=124)
        
        transfer_button = Button(self.app, text="Transfer", font=("Arial", 13), fg="Blue", width=8)
        transfer_button.place(x=584, y=123)
        
        back_button = Button(self.app, text="BACK", command=self.back, font=("Arial", 12), width=12, fg="White", bg="orange")
        back_button.place(x=20, y=20)
        
        price_label= Label(self.app,text="PRICE",font=("Garamond",15),fg="#6A5ACD",width=20)
        price_label.place(x=180,y=199)
        
        amount_label=Label(self.app,text="AMOUNT",font=("Garamond",15),fg="#6A5ACD",width=20)
        amount_label.place(x=403,y=199)
        
        bitcoin_label = Label(self.app, text="BTC", font=("Arial", 10))
        bitcoin_label.place(x=114, y=231)
        price_btc=Entry(self.app,width=13,font=("Arial",13),justify="center")
        price_btc.place(x=239,y=235)
        
        ethereum_label = Label(self.app, text="ETH", font=("Arial", 10),justify="center")
        ethereum_label.place(x=114, y=271)
        price_eth=Entry(self.app,width=13,font=("Arial",13),justify="center")
        price_eth.place(x=239,y=269)
        
        binance_label = Label(self.app, text="BNB", font=("Arial", 10),justify="center")
        binance_label.place(x=114, y=305)
        price_bnb=Entry(self.app,width=13,font=("Arial",13),justify="center")
        price_bnb.place(x=239,y=303)
        
        price_usdt_0= 1
        usdt_label = Label(self.app, text="USDT", font=("Arial", 10),justify="center")
        usdt_label.place(x=114, y=342)
        price_usdt=Entry(self.app,width=13,font=("Arial",13),justify="center")
        price_usdt.insert(0,price_usdt_0)
        price_usdt.place(x=239,y=339)
        
        self.app.mainloop()

    def back(self):
        self.app.destroy()
        login_page = PageLogin()

class App:
    def __init__(self):
        self.new_app = PageLogin()

if __name__ == "__main__":
    new_app = App()
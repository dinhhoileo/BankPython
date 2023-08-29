from PIL import ImageTk
from tkinter import *
from tkinter import messagebox

# ------------------------BACK END-------------------------------------
class Login:
    def __init__(self, account):
        self.account = account
    
    def check_login(self):
        user_name = entry_email.get()  # Lấy giá trị từ widget entry_email
        password = entry_password.get()  # Lấy giá trị từ widget entry_password
        
        if not self.account:
            messagebox.showinfo("Thông báo", "Bạn chưa đăng ký")
        elif user_name in self.account and self.account[user_name] == password:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công")
        else:
            messagebox.showinfo("Thông báo", "Đăng nhập thất bại")

class Register:
    def __init__(self, account):
        self.account = account
    
    def add(self, user_name, password):
        if user_name in self.account:
            messagebox.showinfo("Thông báo", "Tài khoản đã tồn tại")
        else:
            self.account[user_name] = password
            messagebox.showinfo("Thông báo", "Đăng ký thành công")
    
    def register(self):
        user_name = entry_email.get()  # Lấy giá trị từ widget entry_email
        password = entry_password.get()  # Lấy giá trị từ widget entry_password
        self.add(user_name, password)

# ---------------------------FONT END----------------------------------
desktop = Tk()
desktop.title("Bitcoin")
desktop.geometry("350x250")
desktop.iconbitmap("bitcoin.ico")

load = ImageTk.PhotoImage(file='background.png')
curent = load
img = Label(desktop, image=curent)

# Label(desktop, text="Sàn giao dịch bitcoin", fg='red', font=("time new roman", 18), width=25).grid(row=0, column=0, columnspan=2, sticky='e')

# Email
Label(desktop, text="Email", fg='blue').grid(row=1, column=0, sticky='ne')
entry_email = Entry(desktop, width=30)  # Tạo widget Entry và gán vào biến entry_email
entry_email.grid(row=1, column=1)  # Định vị widget entry_email trên giao diện

# Password
Label(desktop, text='Password', fg='red').grid(row=2, column=0, sticky='ne')
entry_password = Entry(desktop, width=30)  # Tạo widget Entry và gán vào biến entry_password
entry_password.grid(row=2, column=1)  # Định vị widget entry_password trên giao diện

account_data = {}
register_account = Register(account_data)
login_account = Login(account_data)

# Login
login_button = Button(desktop, text="Login", command=login_account.check_login)
login_button.grid(row=3, column=0, padx=5, pady=5)

# Register
register_button = Button(desktop, text="Register", command=register_account.register)
register_button.grid(row=3, column=1, padx=5, pady=5)

# -----------------MAIN------------------------
desktop.mainloop()
# pip install selenium

import json
import time
from datetime import datetime  # Thêm import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import tkinter as tk  # Thêm import tkinter
from tkinter import messagebox, filedialog  # Thêm import cho messagebox và filedialog
import threading  # Thêm import threading

# Định nghĩa driver là biến toàn cục
driver = None

url = 'https://api.telegram.org/bot5737041469:AAG5XdXVwATvldvDpXmnlQT0dmh2-sZ70gE/sendMessage?chat_id=-4153385107&text='
def di_dau_truong():
    print('di dau truong')
    
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[contains(@onclick, 'startProvinciarumFight(this, 3')]").click()
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - {result}")  
    print(reward)
    ketqua = f"{current_time} - {result} \n {reward}"
    requests.get(url+ketqua)

def check_dautruong():
    global driver  # Thêm dòng này để sử dụng biến driver toàn cục
    driver.save_screenshot('checkdautruong.png')
    try:
        text_element = driver.find_element(By.XPATH, "//div[text()='To Circus Turma']")
        link_element = text_element.find_element(By.XPATH, "following-sibling::a")
        link_element.click()
        di_dau_truong()
        
    except Exception as e:
        pass

def check_farm():
    try:
        text_element = driver.find_element(By.XPATH, "//div[text()='Go to expedition']")
        link_element = text_element.find_element(By.XPATH, "following-sibling::a")
        link_element.click()
        di_farm() 
    except Exception as e:
        pass

def di_farm():
    print('farm')
    
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(@class, 'expedition_button') and contains(@class, 'awesome-button')]").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Thorough Search')]").click()
        print("Thorough Search")
    except:
        print("khong co drop them")
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - {result}") 
    print(reward)
    ketqua = f"{current_time} - {result} \n {reward}"
    requests.get(url + ketqua)

def di_dungeon():
    print('di_dungeon')
    
    time.sleep(4)
    try:
        driver.find_element(By.XPATH, "//input[@class='button1' and @type='submit' and @value='Normal']").click()
    except:
        pass

    driver.find_element(By.XPATH, "//img[contains(@onclick, 'startFight')]").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Thorough Search')]").click()
        print("Thorough Search")
    except:
        print("khong co drop them")
    
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - {result}") 
    print(reward)
    ketqua = f"{current_time} - {result} \n {reward}"
    requests.get(url + ketqua)

def check_dungeon():
    try:
        text_element = driver.find_element(By.XPATH, "//div[text()='Go to dungeon']")
        link_element = text_element.find_element(By.XPATH, "following-sibling::a")
        link_element.click()
        di_dungeon()
    except Exception as e:
        pass

def check_event():
    try:
        text_element = driver.find_element(By.ID, "banner_event_link")
        
        text_element.click()
        try:
            driver.find_element(By.XPATH, "//button[contains(@class, 'expedition_button') and contains(@class, 'awesome-button')]").click()
            time.sleep(4)
            # Tìm element có id là reportHeader và lưu nội dung vào biến result
            result = driver.find_element(By.ID, "reportHeader").text

            # Tìm element có class="report_reward" và lưu nội dung vào biến reward
            reward = driver.find_element(By.CLASS_NAME, "report_reward").text
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time} - {result}") 
            print(reward)
            ketqua = f"{current_time} - {result} \n {reward}"
            requests.get(url + ketqua)
        except:
            pass
    except:
        pass



# Hàm để hiển thị giao diện
def create_interface():
    global log_text
    global update_log
    global root  # Thêm dòng này để sử dụng biến root toàn cục
    root = tk.Tk()
    root.title("Gladiatus Bot")
    root.geometry("300x550")  # Đặt kích thước giao diện thành 300x800px
    root.eval('tk::PlaceWindow . center')  # Đặt giao diện ở giữa màn hình
    root.update_idletasks()  # Cập nhật giao diện
    x = root.winfo_screenwidth() - root.winfo_width()  # Tính toán vị trí x để đặt bên phải
    root.geometry(f"+{x}+300")  # Đặt giao diện ở bên phải màn hình

    # Khung đăng nhập
    login_frame = tk.Frame(root)
    login_frame.pack(pady=10)

    tk.Button(login_frame, text="Login", command=login).grid(row=0, column=0)

    

    # Khung chọn file cookie
    cookie_frame = tk.Frame(root)
    cookie_frame.pack(pady=10)

    

    # Khung hiển thị thông số
    stats_frame = tk.Frame(root)
    stats_frame.pack(pady=10)

    tk.Label(stats_frame, text="HP:").grid(row=0, column=0)
    hp_label = tk.Label(stats_frame, text="0")
    hp_label.grid(row=0, column=1)

    tk.Label(stats_frame, text="EXP:").grid(row=1, column=0)
    exp_label = tk.Label(stats_frame, text="0")
    exp_label.grid(row=1, column=1)

    tk.Label(stats_frame, text="Thời gian chờ:").grid(row=2, column=0)
    wait_time_label = tk.Label(stats_frame, text="0")
    wait_time_label.grid(row=2, column=1)

    # Khung log
    log_frame = tk.Frame(root)
    log_frame.pack(pady=10)
    
    log_text = tk.Text(log_frame, height=10, width=50)
    log_text.pack()

    

    # Ví dụ cập nhật log
    update_log("Ứng dụng đã khởi động.")

    root.mainloop()
# Hàm để cập nhật log
def update_log(message):
    global log_text
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)  # Cuộn xuống cuối log

def start_auto():
    global update_log
    
    while True:
        
        check_dungeon()
        check_dautruong()
        check_farm()
        time.sleep(5)  # Thay đổi thời gian chờ giữa các lần kiểm tra nếu cần

def login():
    global update_log
    global root

    def perform_login():
        global driver  # Thêm dòng này để sử dụng biến driver toàn cục
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1000,1000")
        opt.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

        # Hiện thông báo cho người dùng lựa chọn hiển thị trình duyệt
        user_input = messagebox.askquestion("Hiển thị trình duyệt", "Bạn có muốn hiển thị trình duyệt không? (y/n)")  # Sử dụng messagebox để hỏi người dùng
        if user_input == 'yes':
            pass
        else:
            opt.add_argument('headless')  # Thêm tùy chọn headless nếu không muốn hiển thị trình duyệt

        root.after(100, lambda: update_log("Đang đăng nhập..."))  # Cập nhật log trước khi bắt đầu
        driver = webdriver.Chrome(options=opt)  # Gán driver cho biến toàn cục
        root.after(100, lambda: update_log("Trình duyệt đã khởi động."))  # Cập nhật log sau khi khởi động trình duyệt
        driver.get('https://lobby.gladiatus.gameforge.com/en_GB/hub')  # Thay đổi URL thành trang web bạn muốn
        original_window = driver.current_window_handle
        # Tải cookie từ file JSON
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)

        # Thêm cookie vào trình duyệt
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(3)
        # Tải lại trang để áp dụng cookie
        driver.find_element(By.XPATH, '//*[@id="joinGame"]/button').click()
        
        driver.switch_to.window(driver.window_handles[-1]) 
        time.sleep(6)

        # Chụp ảnh trình duyệt và lưu vào file check.png
        driver.save_screenshot('check.png')
        update_log("Đã chụp ảnh trình duyệt và lưu vào check.png.")

        start_auto()

    # Tạo thread cho perform_login
    login_thread = threading.Thread(target=perform_login)  # Tạo thread mới cho perform_login
    login_thread.start()  # Bắt đầu thread

# Gọi hàm để tạo giao diện
create_interface()

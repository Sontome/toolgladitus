# pip install selenium

import json
import time
from datetime import datetime  # Thêm import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import tkinter as tk  # Thêm import tkinter
from tkinter import messagebox, filedialog, ttk  # Thêm import cho messagebox và filedialog
import threading  # Thêm import threading
from PIL import Image, ImageTk  # Thêm import cho Pillow

# Định nghĩa driver là biến toàn cục
driver = None

url = 'https://api.telegram.org/bot5737041469:AAG5XdXVwATvldvDpXmnlQT0dmh2-sZ70gE/sendMessage?chat_id=-4153385107&text='
def checkHp():
    try:
        global exp_label
        global gold_label
        global hp_label
        global hp_progress
        global wait_time_farm_label
        global wait_time_label_dungeon
        global wait_time_label_cistus
        global wait_time_vodai_label
        global update_log

        hp_bar_element = driver.find_element(By.ID, "header_values_hp_bar")

        # Lấy giá trị của data-max-value và data-value
        max_heart = hp_bar_element.get_attribute("data-max-value")
        heart = hp_bar_element.get_attribute("data-value")
        hp=f"{heart} / {max_heart}"
        

        # Cập nhật hiển thị lên phần HP trong giao diện
        hp_label.config(text=hp)  # Cập nhật nhãn hiển thị HP
        xp_bar_element = driver.find_element(By.ID, "header_values_xp_bar")

        # Lấy giá trị tooltip
        tooltip = xp_bar_element.get_attribute("data-tooltip")
        
        # Phân tích tooltip để lấy giá trị exp
        exp_value = tooltip.split('"')[3] 
         # Lấy giá trị "Experience: 118 / 295"
        exp_value = exp_value.replace(" / ", " ")
        exp_percentage = xp_bar_element.find_element(By.ID, "header_values_xp_bar_fill").get_attribute("style").split(":")[1].strip()  # Lấy phần trăm từ style
        exp_percentage = exp_percentage.replace(";", "")
        # Kết hợp giá trị exp và phần trăm
        exp = f"{exp_value} ({exp_percentage})"
        exp_label.config(text=exp)

        # Cập nhật thanh tiến trình
        hp_percentage = (int(heart) / int(max_heart)) * 100
        hp_progress['value'] = hp_percentage  # Cập nhật giá trị thanh tiến trình

        # Cập nhật màu sắc của thanh tiến trình
        if hp_percentage == 100:
            hp_progress.config(style='green.Horizontal.TProgressbar')
        elif hp_percentage >= 50:
            hp_progress.config(style='yellow.Horizontal.TProgressbar')
        else:
            hp_progress.config(style='red.Horizontal.TProgressbar')
        gold_text_element = driver.find_element(By.ID, "sstat_gold_val")
        gold_text = gold_text_element.text
        gold_label.config(text=gold_text)

        arena_text_element = driver.find_element(By.ID, "cooldown_bar_text_arena")
        arena_text = arena_text_element.text
        wait_time_vodai_label.config(text=arena_text)
        
        cistus_text_element = driver.find_element(By.ID, "cooldown_bar_text_ct")
        cistus_text = cistus_text_element.text
        wait_time_label_cistus.config(text=cistus_text)

        farm_text_element = driver.find_element(By.ID, "cooldown_bar_text_expedition")
        farm_text = farm_text_element.text
        wait_time_farm_label.config(text=farm_text)

        dungeon_text_element = driver.find_element(By.ID, "cooldown_bar_text_dungeon")
        dungeon_text = dungeon_text_element.text
        wait_time_label_dungeon.config(text=dungeon_text)
    except:
        pass
def di_dau_truong():
    global update_log
    update_log('di_dau_truong')
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[contains(@onclick, 'startProvinciarumFight(this, 3')]").click()
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ketqua = f"{current_time} - {result} \n {reward}"
    update_log(ketqua)
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
    global update_log
    update_log('di_farm')
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(@class, 'expedition_button') and contains(@class, 'awesome-button')]").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Thorough Search')]").click()
        update_log('Thorough Search')
    except:
        update_log('khong co drop them')
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ketqua = f"{current_time} - {result} \n {reward}"
    update_log(ketqua)
    requests.get(url + ketqua)

def di_dungeon():
    global update_log
    update_log('di_dungeon')
    time.sleep(4)
    try:
        driver.find_element(By.XPATH, "//input[@class='button1' and @type='submit' and @value='Normal']").click()
    except:
        pass

    driver.find_element(By.XPATH, "//img[contains(@onclick, 'startFight')]").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Thorough Search')]").click()
        
        update_log('Thorough Search')
    except:
        
        update_log('khong co drop them')
    
    time.sleep(4)
    # Tìm element có id là reportHeader và lưu nội dung vào biến result
    result = driver.find_element(By.ID, "reportHeader").text

    # Tìm element có class="report_reward" và lưu nội dung vào biến reward
    reward = driver.find_element(By.CLASS_NAME, "report_reward").text
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ketqua = f"{current_time} - {result} \n {reward}"
    update_log(ketqua)
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
    global hp_label
    global exp_label
    global hp_progress
    global gold_label
    global wait_time_farm_label
    global wait_time_label_dungeon
    global wait_time_label_cistus
    global wait_time_vodai_label
    global update_log
    global image_label
    global root  # Thêm dòng này để sử dụng biến root toàn cục
    root = tk.Tk()
    root.title("Gladiatus Bot")
    root.geometry("300x750")  # Đặt kích thước giao diện thành 300x800px
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

    # Thêm thanh tiến trình cho HP
    hp_progress = ttk.Progressbar(stats_frame, length=200, mode='determinate')
    hp_progress.grid(row=1, column=0, columnspan=2)

    tk.Label(stats_frame, text="EXP:").grid(row=2, column=0)
    exp_label = tk.Label(stats_frame, text="0")
    exp_label.grid(row=2, column=1)
    tk.Label(stats_frame, text="Vàng:").grid(row=3, column=0)
    gold_label = tk.Label(stats_frame, text="0")
    gold_label.grid(row=3, column=1)

    tk.Label(stats_frame, text="Thời gian chờ farm:").grid(row=4, column=0)
    wait_time_farm_label = tk.Label(stats_frame, text="0")
    wait_time_farm_label.grid(row=3, column=1)
    tk.Label(stats_frame, text="Thời gian chờ võ đài:").grid(row=5, column=0)
    wait_time_vodai_label = tk.Label(stats_frame, text="0")
    wait_time_vodai_label.grid(row=4, column=1)
    tk.Label(stats_frame, text="Thời gian chờ dungeon:").grid(row=6, column=0)
    wait_time_label_dungeon = tk.Label(stats_frame, text="0")
    wait_time_label_dungeon.grid(row=5, column=1)
    tk.Label(stats_frame, text="Thời gian chờ Cistus:").grid(row=7, column=0)
    wait_time_label_cistus = tk.Label(stats_frame, text="0")
    wait_time_label_cistus.grid(row=6, column=1)

    # Khung log
    log_frame = tk.Frame(root)
    log_frame.pack(pady=10)
    
    log_text = tk.Text(log_frame, height=10, width=50)
    log_text.pack()
    image_frame = tk.Frame(root)
    image_frame.pack(pady=10)

    # Tải ảnh check.png
    img = Image.open('check.png')  # Mở ảnh
    img = img.resize((300, 250), Image.LANCZOS)  # Thay đổi kích thước ảnh
    check_image = ImageTk.PhotoImage(img)  # Chuyển đổi ảnh thành PhotoImage
    image_label = tk.Label(image_frame, image=check_image)
    image_label.image = check_image  # Giữ tham chiếu đến ảnh
    image_label.pack()
    

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
    global image_label
    while True:
        try:
            driver.find_element(By.XPATH, "//input[@type='submit' and @value='OK']").click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, "//input[@type='submit' and @value='Confirm']").click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, "//input[@type='submit' and @value='Close']").click()
        except:
            pass
        checkHp()
        check_dungeon()
        check_dautruong()
        check_farm()
        
        # Chụp ảnh trình duyệt và lưu vào file check.png
        driver.save_screenshot('check.png')
        
        # Resize ảnh và cập nhật hiển thị trong giao diện
        img = Image.open('check.png')  # Mở ảnh
        img = img.resize((300, 250), Image.LANCZOS)  # Thay đổi kích thước ảnh
        check_image = ImageTk.PhotoImage(img)  # Chuyển đổi ảnh thành PhotoImage
        
        image_label.config(image=check_image)  # Cập nhật ảnh trong label
        image_label.image = check_image  # Giữ tham chiếu đến ảnh mới

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
        time.sleep(8)

        # Chụp ảnh trình duyệt và lưu vào file check.png
        driver.save_screenshot('check.png')
        update_log("Đã chụp ảnh trình duyệt và lưu vào check.png.")

        start_auto()

    # Tạo thread cho perform_login
    login_thread = threading.Thread(target=perform_login)  # Tạo thread mới cho perform_login
    login_thread.start()  # Bắt đầu thread

# Gọi hàm để tạo giao diện
create_interface()

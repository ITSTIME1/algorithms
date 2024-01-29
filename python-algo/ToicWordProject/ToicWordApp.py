import sys
import requests
import time
from PyQt5.QtWidgets import ( QStackedWidget, QWidget, QApplication, QMainWindow, 
    QVBoxLayout, QLabel, QGridLayout, QPushButton, 
    QSizePolicy
)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class InternetChecker(QThread):
    internet_status_signal = pyqtSignal(bool)
    def run(self):
        while True:
            try:
                response = requests.get("https://www.google.com", timeout=5)
                internet_status = response.status_code == 200
            except requests.ConnectionError:
                internet_status = False
            self.internet_status_signal.emit(internet_status)
            time.sleep(60)
        
# 단어장 선택               
class SecondPageLayout(QWidget):
    def __init__(self):
        super().__init__() # Qwidget에 있는것들을 사용하기 위해서.

    def initUI(self):
        pass
        
class FirstPageLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.is_internet_connect = False
        self.connect_count = 0
        self.selected_word_book = None
        self.stackedWidget = None  # Define stackedWidget attribute
        self.initUI() # call initUI Method

    def initUI(self):
        self.stackedWidget = QStackedWidget()
        self.firstPage_layout()
        self.secondPage_layout()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stackedWidget)

        self.setGeometry(300, 300, 800, 700)
        self.setLayout(main_layout)
        
        
    def clickButton(self):
        btn_text = self.sender().text()
        if btn_text == "계속듣기":
            print(self.stackedWidget)
            self.stackedWidget.setCurrentIndex(1)
        elif btn_text == "미국 발음":
            pass
        elif btn_text == "영국 발음":
            pass
        elif btn_text == "호주 발음":
            pass
        elif btn_text == "이어서 듣기":
            pass
        elif btn_text == "듣기":
            pass
        elif btn_text == "계속듣기":
            pass       
   

    # 단어장 선택 페이지
    def secondPage_layout(self):
        secondPageWidget = QWidget()
        word_text = QLabel("this is second page.")
        layout_page_2 = QVBoxLayout(secondPageWidget)
        layout_page_2.addWidget(word_text)
        self.stackedWidget.addWidget(secondPageWidget)
        
    def firstPage_layout(self):  
        firstPageWidget = QWidget()
        word_text = QLabel("Testing")
        word_text.setStyleSheet("margin: 20px")
        word_text.setAlignment(Qt.AlignCenter)
        word_text.setFont(QFont("Arial",25))
        layout_page_1 = QVBoxLayout(firstPageWidget)
        
        grid_layout = QGridLayout()
        
        self.names = ["미국식 발음", "영국식 발음", "호주 발음", "이어서 듣기", "듣기", "계속듣기"]
        
        coords = [(i, j) for i in range(2) for j in range(3)]
        
        for name, coord in zip(self.names, coords):
            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(self.clickButton)
            grid_layout.addWidget(button, *coord)
            
        layout_page_1.addWidget(word_text)
        layout_page_1.addLayout(grid_layout)
        self.stackedWidget.addWidget(firstPageWidget)
    
    


class ToicWordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Connecting...")
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Central Widget')
        self.show()
        self.firstLayout = FirstPageLayout()
        self.setCentralWidget(self.firstLayout)
        
        self.internet_checker = InternetChecker(self)
        self.internet_checker.internet_status_signal.connect(self.handleInternetStatus)
        self.internet_checker.start()  
        
    def handleInternetStatus(self, status):
        self.is_internet_connect = status
        if status:
            print("인터넷 연결 상태가 정상입니다.")
            self.statusBar.showMessage("Successful Internet Connectiong.")
            self.connect_count = 0
        else:
            print(f"1분뒤 자동으로 인터넷 연결을 시도 하겠습니다. ( 시도횟수 {self.connect_count} )")
            self.statusBar.showMessage("Failed Internet Connectiong.")
            self.connect_count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToicWordApp()
    ex.show()
    sys.exit(app.exec_())

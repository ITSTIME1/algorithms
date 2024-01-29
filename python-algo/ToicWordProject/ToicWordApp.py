import sys
import requests
import time
import os
from glob import glob
from PyQt5.QtWidgets import (
    QStackedWidget, QWidget, QApplication, QMainWindow,
    QVBoxLayout, QLabel, QGridLayout, QPushButton,
    QSizePolicy, QAction, qApp
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

    def __init__(self, stackedWidget) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.initUI()

    def initUI(self) -> None:
        self.createGridLayout()
        
    def createGridLayout(self):
        self.getWordBook()
        
        
    # Get wordBook at current directory.
    def getWordBook(self):
        root_path = f"/Users/itstime/algorithms/python-algo/ToicWordProject"
        
        txt_files = glob(os.path.join(root_path, '*.txt'))
        word_book_name = [file.split("/")[-1] for file in txt_files]
        layout_page_2 = QVBoxLayout(self)
        # 파일이 하나라도 존재한다면
        if len(word_book_name) != 0:    
            grid_layout_2 = QGridLayout()
            word_text = QLabel("Choose from your .txt")
            word_text.setStyleSheet("margin: 25px")
            word_text.setAlignment(Qt.AlignCenter)
            word_text.setFont(QFont("Arial", 25))    
            
            # @TODO 버튼 클릭 구현
            for i, name in enumerate(word_book_name):
                word_book_btn = QPushButton(name)
                word_book_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                # word_book_btn.clicked.connect()
                grid_layout_2.addWidget(word_book_btn, i // 3, i % 3)  # Use integer division and modulo

            layout_page_2.addWidget(word_text)
            layout_page_2.addLayout(grid_layout_2)
            
        else:
            warning_message = QLabel("There is noting.")
            layout_page_2.addWidget(warning_message)
            
            


class FirstPageLayout(QWidget):

    def __init__(self, stackedWidget) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.selected_word_book = None
        self.initUI()  # call initUI Method

    def clickButton(self):
        btn_text = self.sender().text()
        if btn_text == "계속듣기":
            pass
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

    def initUI(self) -> None:
        word_text = QLabel("This is a test page.")
        word_text.setStyleSheet("margin: 25px")
        word_text.setAlignment(Qt.AlignCenter)
        word_text.setFont(QFont("Arial", 25))
        layout_page_1 = QVBoxLayout(self)

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


class ToicWordApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.show()

        self.internet_checker = InternetChecker(self)
        self.internet_checker.internet_status_signal.connect(self.handleInternetStatus)
        self.internet_checker.start()

    def initUI(self):
        self.stackedWidget = QStackedWidget()
        self.is_internet_connect = False
        self.connect_count = 0
        self.statusBar = self.statusBar()

        self.stackedWidget.addWidget(FirstPageLayout(self.stackedWidget))
        self.stackedWidget.addWidget(SecondPageLayout(self.stackedWidget))

        self.setCentralWidget(self.stackedWidget)

        self.createMenubar()
        self.statusBar.showMessage("Connecting...")
        self.setWindowTitle('Central Widget')
        self.setGeometry(300, 300, 800, 700)

    def createMenubar(self) -> None:
        exitAction = QAction('종료', self)
        addWordBookAction = QAction('단어장추가', self)
        addWordBookAction.setStatusTip('단어장 추가')
        addWordBookAction.triggered.connect(self.move_to_secondPage)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        settingMenu = menubar.addMenu('&설정')
        settingMenu.addAction(exitAction)

        programMenu = menubar.addMenu('&프로그램')
        programMenu.addAction(addWordBookAction)

    def move_to_secondPage(self) -> None:
        self.stackedWidget.setCurrentIndex(1)

    def handleInternetStatus(self, status) -> None:
        self.is_internet_connect = status
        if status:
            print("인터넷 연결 상태가 정상입니다.")
            self.statusBar.showMessage("Successful Internet Connection.")
            self.connect_count = 0
        else:
            print(f"1분뒤 자동으로 인터넷 연결을 시도 하겠습니다. ( 시도횟수 {self.connect_count} )")
            self.statusBar.showMessage("Failed Internet Connection.")
            self.connect_count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToicWordApp()
    sys.exit(app.exec_())

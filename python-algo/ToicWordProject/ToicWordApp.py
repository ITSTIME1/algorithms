import sys
import requests
import random
import time
import os
import playsound
from gtts import gTTS
from glob import glob
from PyQt5.QtWidgets import (
    QStackedWidget, QWidget, QApplication, QMainWindow,
    QVBoxLayout, QLabel, QGridLayout, QPushButton,
    QSizePolicy, QAction, qApp
)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer


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

    def __init__(self, stackedWidget, firstPageLayout) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.firstPageLayout = firstPageLayout
        self.prev_clicked_button = None
        
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
            self.word_text = QLabel("Choose from your .txt file.")
            self.word_text.setStyleSheet("margin: 25px")
            self.word_text.setAlignment(Qt.AlignCenter)
            self.word_text.setFont(QFont("Arial", 25))    
            
            for i, name in enumerate(word_book_name):
                word_book_btn = QPushButton(name)
                word_book_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                word_book_btn.clicked.connect(self.getWordBookName)
                grid_layout_2.addWidget(word_book_btn, i // 3, i % 3)  # Use integer division and modulo

            layout_page_2.addWidget(self.word_text)
            layout_page_2.addLayout(grid_layout_2)
            
        else:
            warning_message = QLabel("There is noting.")
            layout_page_2.addWidget(warning_message)
            
    def getWordBookName(self):
        file_name = self.sender().text()
        
        if self.prev_clicked_button == None:
            self.sender().setStyleSheet("background-color: orange")
            self.word_text.setText(file_name)
            self.prev_clicked_button = self.sender()
        else:
            if self.sender() != self.prev_clicked_button:
                self.sender().setStyleSheet("background-color: orange")
                self.word_text.setText(file_name)
                self.prev_clicked_button.setStyleSheet("background-color: none")
                self.prev_clicked_button = self.sender()
            else:
                self.word_text.setText("Choose from your .txt file.")
                self.prev_clicked_button.setStyleSheet("background-color: none")
                self.prev_clicked_button = None

        self.firstPageLayout.setSelectedWordBookName(file_name)
        # print(self.firstPageLayout.getSelectedWordBookName())
        
        # 임시로 페이지이동
        self.parent_stackedWidget.setCurrentIndex(0)

class FirstPageLayout(QWidget):
    # Class Variable
    selected_word_book = None
    word_book_dic = {}
    checked_word_list = []
    keys_list = None
    secure_random = random.SystemRandom()
    end_string = "There are no more words to choose from."  
    prpronunciation = None # 발음
    tld = "com"
    prev_prpronunciation = None
    
    
    def __init__(self, stackedWidget) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.initUI()  # call initUI Method
        

    # @TODO 단어장 기능구현
    def clickButton(self):
        btn_text = self.sender().text()
        if self.selected_word_book is not None:
            if btn_text == "계속듣기":
                pass
            
            
            elif btn_text == "미국식 발음" or btn_text == "호주식 발음" or btn_text == "영국식 발음":
                self.select_prpronunciation(btn_text)   
                
                
            elif btn_text == "이어서 듣기":
                
                # @TODO 한번 듣고 나서, 다시 듣기 위해서, start, end를 구분하고 있어야 겠네

                if not hasattr(self, 'timer'):  # 타이머가 없을 경우에만 타이머를 설정
                    self.sender().setStyleSheet("background-color: orange")
                    self.timer = QTimer(self)
                    self.timer.timeout.connect(self.playSound)
                    self.timer.start(2000)  # 여기서 2초에 한 번씩 실행할 테니까
                    self.sender().setStyleSheet("background-color: none")
            elif btn_text == "듣기": 
                # 그럼 기존거는 한번 들려주어야 겠네
                self.listen_once()
                
    # 음원재생
    def playSound(self):
        check_word = self.word_text.text()
        if check_word != self.end_string and self.prpronunciation is not None and self.tld is not None:
            object_gTTs = gTTS(text=check_word, lang="en", tld=self.tld)
            fileName = 'LC_File.mp4'
            object_gTTs.save(fileName)
            playsound.playsound(fileName)

            # 그리고 다른 단어를 선택하게끔
            self.checked_word_list.append(check_word)
            # 새로운 단어를 뽑아옴
            check_word = self.check_available_word()
            self.word_text.setText(check_word)
            
            if check_word == self.end_string:
                self.timer.stop()
                del self.timer  # 타이머 객체 제거
        
                
                                
    def check_available_word(self) -> str:
        available_words = set(self.keys_list) - set(self.checked_word_list)
        if available_words:
            selected_word = self.secure_random.choice(list(available_words))
            self.word_text.setText(selected_word)
            return selected_word
        else:
            self.word_text.setText(self.end_string)
            return self.end_string
            
    
    def select_prpronunciation(self, btn_text):
        # 이전에 선택한 버튼이 없을 때
        if self.prev_prpronunciation is None:
            self.sender().setStyleSheet('color: orange')
            self.prev_prpronunciation = self.sender()
            self.set_pronunciation_and_tld(btn_text)   
        else:
            # 이전에 선택한 버튼이 있을 때
            if self.prev_prpronunciation == self.sender():
                # 같은 버튼을 다시 클릭했을 때 토글
                current_style = self.sender().styleSheet()
                if 'color: orange' in current_style:
                    self.sender().setStyleSheet('color: white')
                elif 'color: white' in current_style:
                    self.sender().setStyleSheet('color: orange')
                
                # 같은 버튼을 다시 클릭했으므로, 발음과 tld 초기화
                self.prpronunciation = None
                self.tld = None
            else:
                # 다른 버튼을 클릭했을 때
                self.sender().setStyleSheet('color: orange')
                self.prev_prpronunciation.setStyleSheet('color: white')
                self.prev_prpronunciation = self.sender()
                # 발음 설정
                self.set_pronunciation_and_tld(btn_text)    
                
    # 발음 설정                                
    def set_pronunciation_and_tld(self, btn_text):
        if btn_text == "미국식 발음":
            self.prpronunciation = "en"
            self.tld = "com"
        elif btn_text == "영국식 발음":
            self.prpronunciation = "en"
            self.tld = "co.uk"
        else:
            self.prpronunciation = "en"
            self.tld = "com.au"        
            
            
    def listen_once(self):
        check_word = self.word_text.text()
        
        if check_word != self.end_string and self.prpronunciation is not None and self.tld is not None:
            object_gTTs = gTTS(text=check_word, lang="en", tld = self.tld)
            fileName = 'LC_File.mp4'
            object_gTTs.save(fileName)
            
            playsound.playsound(fileName)
            
        
        # 여기서 둘다 None인 경우는 제외하자
        if self.prpronunciation is not None and self.tld is not None and check_word not in self.checked_word_list :
            self.checked_word_list.append(check_word)
            self.check_available_word()
    
                        
    def initUI(self) -> None:
        self.word_text = QLabel("This is a test page.")
        self.word_text.setStyleSheet("margin: 25px")
        self.word_text.setAlignment(Qt.AlignCenter)
        self.word_text.setFont(QFont("Arial", 25))
        layout_page_1 = QVBoxLayout(self)

        grid_layout = QGridLayout()

        self.names = ["미국식 발음", "영국식 발음", "호주식 발음", "이어서 듣기", "듣기", "계속듣기"]

        coords = [(i, j) for i in range(2) for j in range(3)]

        for name, coord in zip(self.names, coords):
            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if name == "미국식 발음" or name == "영국식 발음" or name =="호주 발음":
                button.clicked.connect(self.clickButton)
            else:
                button.released.connect(self.clickButton)
            grid_layout.addWidget(button, *coord)

        layout_page_1.addWidget(self.word_text)
        layout_page_1.addLayout(grid_layout)
        
        
    def getSelectedWordBookName(self):
        return self.selected_word_book
    
    def setSelectedWordBookName(self, book_name):
        # 만약 선택한 단어장, 이전에 선택했던 단어장이랑 같지 않다면
        if book_name is not None and self.selected_word_book != book_name:
            # 이전에 선택한 단어장 초기화
            self.word_book_dic = {}

            try:
                with open(book_name) as file:
                    words = file.readlines()
                    for word in words:
                        result = word.split(",")
                        # 단어: 뜻
                        self.word_book_dic[result[0]] = result[1]

                self.selected_word_book = book_name
                self.keys_list = list(self.word_book_dic.keys())
                self.word_text.setText(self.secure_random.choice(self.keys_list))
            except Exception as e:
                print(f"{e} 발생.")
        elif book_name is not None:
            # 만약 선택한 단어장이 이전에 선택했던 단어장이랑 같다면
            # 결국 단어들만 새로 뽑으면됨.
            self.word_text.setText(self.secure_random.choice(self.keys_list))

        

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
        self.firstLayout = FirstPageLayout(self.stackedWidget)
        self.stackedWidget.addWidget(self.firstLayout)
        self.stackedWidget.addWidget(SecondPageLayout(self.stackedWidget, self.firstLayout))

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

        programMenu = menubar.addMenu('&단어장 선택')
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

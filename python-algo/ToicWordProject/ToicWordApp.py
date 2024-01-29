import sys
import requests
import time
import glob
from PyQt5.QtWidgets import ( QStackedWidget, QWidget, QApplication, QMainWindow, 
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
        super().__init__() # Qwidget에 있는것들을 사용하기 위해서.
        self.parent_stackedWidget = stackedWidget
        self.initUI()

    def initUI(self) -> QWidget:
        secondPageWidget = QWidget()
        word_text = QLabel("this is second page.")
        layout_page_2 = QVBoxLayout(secondPageWidget)
        layout_page_2.addWidget(word_text)
        
        self.parent_stackedWidget.addWidget(secondPageWidget)
        
        return secondPageWidget
        
        # 단어장 종류
        # secondPage 오면, 미리 저장해뒀던, 단어장 전부다 가지고 와서 보여주어야 겠네
        self.wordBook = ["LC파트1단어.txt", "LC파트2단어.txt"] 
        fileCounter = len(glob.glob1("/Users/itstime/algorithms/python-algo/ToicWordProject","*.txt"))
        print(fileCounter)
        # coords = [(i, j) for i in range(2) for j in range(3)]
        
        # for name, coord in zip(self.names, coords):
        #     button = QPushButton(name)
        #     button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #     button.clicked.connect(self.clickButton)
        #     grid_layout.addWidget(button, *coord)
            
        # layout_page_1.addWidget(word_text)
        # layout_page_1.addLayout(grid_layout)
        # self.stackedWidget.addWidget(firstPageWidget)
        
class FirstPageLayout(QWidget):
    def __init__(self, stackedWidget) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.is_internet_connect = False
        self.connect_count = 0
        self.selected_word_book = None
        self.initUI() # call initUI Method
        
        
    def clickButton(self):
        btn_text = self.sender().text()
        if btn_text == "계속듣기":
            self.parent_stackedWidget.setCurrentIndex(1)
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
        firstPageWidget = QWidget()
        word_text = QLabel("This is a test page.")
        word_text.setStyleSheet("margin: 25px")
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
        
        self.parent_stackedWidget.addWidget(firstPageWidget)
        
    
    

# mainView에서, stacked를 관리해야 할거 같은데
# 그래서 생성되면 stacked에다가 넣어주는 형식으로
# 그럼 설계를 좀 다시 해보자면, ToicWordApp에서 stackedWidget을 관리하고, 여기에서, 생성되게끔 만들면 되겠다.
# 그럼 여기다가 추가하고, firstLAyout, secondLAyout모두 참조로 넘기면, 여기다가 추가가 되니까, 그런다음에, 
# stackedwidget에다가, 레이아웃들만 추가해주면되는거지. 오케이

class ToicWordApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.stackedWidget = QStackedWidget()
        self.statusBar = self.statusBar()
        self.initUI()
        
        '''
            1. stackWidget을 만들어준다.
            2. FirstPage, SecondPage를 만들어주고
            3. 첫번째 페이지를 firstPage로 잡아준다.
            4. 화면을 생성한다.
            5. 인터넷 환경을 체크한다.
        '''
    

        # 페이지를 생성해서 widget에 넣어주고
        self.stackedWidget.addWidget(FirstPageLayout(self.stackedWidget))
        self.stackedWidget.addWidget(SecondPageLayout(self.stackedWidget))
        # 0번째를 가장 처음으로 중앙을 잡음.
        self.stackedWidget.setCurrentIndex(0)
        self.setCentralWidget(self.stackedWidget)
        
        self.show()
        
        self.internet_checker = InternetChecker(self)
        self.internet_checker.internet_status_signal.connect(self.handleInternetStatus)
        self.internet_checker.start()  
        
     
        
    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stackedWidget)
    
        self.createMenubar()
        self.statusBar.showMessage("Connecting...")
        self.setWindowTitle('Central Widget')

        self.setGeometry(300, 300, 800, 700)
        self.setLayout(main_layout)    
        
    def createMenubar(self) -> None:
        exitAction = QAction('종료', self)
        addWordBookAction = QAction('단어장추가', self)
        addWordBookAction.setStatusTip('단어장 추가')
        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)
        

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        # setting menu
        settingMenu = menubar.addMenu('&설정')
        settingMenu.addAction(exitAction)
        
        # view
        programMenu = menubar.addMenu('&프로그램')
        programMenu.addAction(addWordBookAction)

    def handleInternetStatus(self, status) -> None:
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

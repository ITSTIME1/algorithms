import sys, requests, random, time, os, playsound, pygame
from functools import partial
from gtts import gTTS
from glob import glob
from PyQt5.QtWidgets import (
    QStackedWidget, QWidget, QApplication, QMainWindow,
    QVBoxLayout, QLabel, QGridLayout, QPushButton,
    QSizePolicy, QAction, qApp, QHBoxLayout
)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QMimeData, QEvent, QPoint

'''
    @Class Internet Check.
'''


# @TODO 한단어에 대해서, 세가지 발음을 한번에 듣는것을 만들자

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

class DragButton(QPushButton):
    
    def mouseMoveEvent(self, e):
        # whene i clicked left button.
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            # get button text when i clicked button but noting?
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)
            
        
'''
    @Class drag & drop.
'''
class ThirdPageLayout(QWidget):
    def __init__(self, stackedWidget, firstPageLayout) -> None:
        # QWidget initialize.
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.firstPageLayout = firstPageLayout
        self.setAcceptDrops(True)
        self.init_layout()
    
    
    def init_layout(self) -> None:
        self.test_drag_layout = QHBoxLayout(self)
        # 여기다가 레이블로 만들 수 있구나
        self.drag_and_drop_viewer = QLabel("Drop .txt file.")
        self.drag_and_drop_viewer.setStyleSheet("border : 4px dashed #aaa")
        self.drag_and_drop_viewer.setFont(QFont("Arial", 25))    
        self.drag_and_drop_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_drag_layout.addWidget(self.drag_and_drop_viewer)
    
    def dragEnterEvent(self, e) -> None:
        e.accept()
        
    def dropEvent(self, e) -> None:
        # 텍스트를 가진 파일일 때만 . Mime Type / text/plain
        if e.mimeData().hasText():
            file = e.mimeData().urls()[0].toLocalFile().split("/")[-1]
            result = file.split(".")
            file_name, file_extension = result[0], result[1]
            
            if file_extension == 'txt':
                e.setDropAction(Qt.CopyAction)
                e.accept()
                self.drag_and_drop_viewer.setText(f"{file_name + '.' + file_extension}\nSuccessful load.")
                self.drag_and_drop_viewer.setStyleSheet("border : 4px dashed orange")
                current_index = self.parent_stackedWidget.currentIndex()
                current_widget = self.parent_stackedWidget.widget(current_index-1)
                # 현재 표시된 페이지의 위젯이 SecondPageLayout 클래스의 인스턴스인지 확인
                if isinstance(current_widget, SecondPageLayout):
                    # 위젯을 지우고, 해당 자리에 SecondPageLayout을 다시 생성.
                    self.parent_stackedWidget.removeWidget(current_widget)
                    self.parent_stackedWidget.insertWidget(current_index - 1, SecondPageLayout(self.parent_stackedWidget, self.firstPageLayout))
                    self.parent_stackedWidget.setCurrentIndex(1)
                    
                
            else:
                e.ignore()
                self.drag_and_drop_viewer.setText(f"{file_name + '.' + file_extension}\nFailed load.")
                self.drag_and_drop_viewer.setStyleSheet("border : 4px dashed #aaa")
        else:
            e.ignore()
            self.drag_and_drop_viewr.setText(f"Not Text File.")
            
            


        
        
        
        
'''
    @Class select word on grid layout.
'''
class SecondPageLayout(QWidget):

    def __init__(self, stackedWidget, firstPageLayout) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.firstPageLayout = firstPageLayout
        self.prev_clicked_button = None
        self.init_layout()

    def init_layout(self) -> None:
        self.create_grid_layout()
        
    def create_grid_layout(self) -> None:
        self.get_wordbook()
        
        
    # Get wordBook at current directory.
    def get_wordbook(self) -> None:
        print("get_wordBook 호출")
        root_path = f"{sys.path[0]}"
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
                word_book_btn.clicked.connect(self.get_wordbookName)
                grid_layout_2.addWidget(word_book_btn, i // 3, i % 3)  # Use integer division and modulo

            layout_page_2.addWidget(self.word_text)
            layout_page_2.addLayout(grid_layout_2)
            
        else:
            warning_message = QLabel("There is noting.")
            warning_message.setAlignment(Qt.AlignCenter)
            # Qt.AlignCenter
            layout_page_2.addWidget(warning_message)
            
            
    # @TODO 이거를 생각해보니까, 단어장이 일단 그 파일에 있어야 한다는거니까
    # 단어장을 추가하지를 못하는데 어떻게 해야하냐
    # 1. 프로그램 내장디비를 sqlite같은걸 사용한다.
    # 2. 복사해서 사용하는 동안에만 딕셔너리에 모두 저장해둔다. 너무 비효율적인거 같은데
    
    # 단어 저장할 파일 path를 사전에 정의하고, 그 사전에 정의된 파일 path를 내장으로 가지고 있자.
    # 그래서 만약에 환경변수에 해당 파일 path가 저장되어 있다면, 해당 단어 저장 디렉토리를 가지고 오고
    # 만약 해당 환경변수가 없다면, 단어 환경변수를 설정한다.
    # 이렇게 하면, 이미 installer로 만들어진 것에, 추가하지 못하는 문제를 해결할 수 있다.
    # 뿐만 아니라, 드래그 앤 드롭 기능을 이용할 때, 어떤 폴더에서든 .txt파일을 드래그앤 드롭하고 난 뒤에
    # 환경변수로 해당 파일을 옮기거나, 해당 파일에다가 추가한다. copy본을 .
    # 그럼 한번 추가 등록한 것은 삭제하지 않는 이상, 환경 변수에 의해 단어장을 계속 불러올 것이다.
    # 그럼 환경변수를 어떻게 설정할지가 문제네 이건 나중에하자.
    # 지금 쓰는데 큰 문제가 없으니까. 
    def get_wordbookName(self) -> None:
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

        self.firstPageLayout.set_selected_book_name(file_name)
        # print(self.firstPageLayout.get_selected_book_name())
        
        # 임시로 페이지이동
        self.parent_stackedWidget.setCurrentIndex(0)

'''
    @Class main layout for listening.
'''
class FirstPageLayout(QWidget):
    # Class Variable
    selected_word_book = None
    word_book_dic = {}
    checked_word_list = []
    keys_list = None
    secure_random = random.SystemRandom()
    end_string = "There are no more words to choose from."  
    pron = None # 발음
    tld = "com"
    prev_pron = None
    isPlayer = False
    timer = None
    
    
    
    def __init__(self, stackedWidget) -> None:
        super().__init__()
        self.parent_stackedWidget = stackedWidget
        self.init_layout()  # call init_layout Method
           
        
           
    def click_book_btn(self) -> None:
        self.global_obj = self.sender()
        btn_text = self.sender().text()
        if self.selected_word_book is not None:
            if btn_text in ("미국식 발음",  "호주식 발음", "영국식 발음"):
                self.select_prpron(btn_text)   
                
            elif btn_text in ("이어서 듣기", "듣기", "한 단어 계속듣기"):
                # sender()는 해당 버튼의 객체인데
                # 해당 버튼의 객체를 가지고, 작업을 하기 위해서 sender()를 넘기면 될거 같음
                self.play_wordbook(btn_text)
                self.global_obj.setStyleSheet("color : orange")
            elif btn_text == "다음 단어":
                current_word = self.word_text.text()
                if current_word != self.end_string:
                    self.checked_word_list.append(current_word)
                    self.word_text.setText(self.check_available_word())
        
            
    # TODO listening button 감지하는거 하나 더 만들어야 할 것 같고, 
    def play_wordbook(self, btn_text):
        # play_wordBook을 실행할때 중요한건, isPlayer is False냐가 중요한거니까
        if self.isPlayer is False:
            if btn_text == "듣기":
                self.listen_once()
                
            elif btn_text == "이어서 듣기":
                self.continue_listening()
                
            elif btn_text == "한 단어 계속듣기":
                self.continue_listening_for_a_word() 
                
        else:
            if self.isPlayer and btn_text == "한 단어 계속듣기":
                self.timer.stop()
                self.isPlayer = False
                
                # self.global_obj.setStyleSheet("color: white")
            
            print(f"{self.isPlayer} 이미 player가 동작중..")
                    
    def continue_listening_for_a_word(self):
        # 한단어 리스닝은, 현재 단어를 기반으로 계속 듣는것,
        # 다음 단어를 넘기지 않음, 다음 단어 넘기는 것도 생각은 해봐야 겠다.
        self.isPlayer = True
        self.continue_listening(True)
    # Initialize timer
    def continue_listening(self, has_a_word=False) -> None:
        self.isPlayer = True
        self.timer = QTimer(self)
        # self.global_obj.setStyleSheet("color: orange")
        self.timer.timeout.connect(partial(self.play_sound, has_a_word))
        self.timer.start(1500)
                
    # 음원재생
    # pygame 을 사용해서 실행하는거. non-blocking 방식임.
    def play_mp4(self, check_word) -> bool:
        if check_word != self.end_string or check_word != "Please choose pronunciation.":
            if self.pron != None and self.tld != None:
                object_gTTs = gTTS(text=check_word, lang="en", tld=self.tld)
                fileName = 'LC_File.mp4'
                object_gTTs.save(fileName)
                
                pygame.mixer.music.load(fileName)
                pygame.mixer.music.play()
                
                

                return True
        return False
    # play_sound         
    def play_sound(self, has_a_word) -> None:
        # 단어가 존재한다면, 또는 단어가 존재하지 않는다면
        if has_a_word:
            # 체크할 단어를 가지고 옴
            # 이제 그 단어를 play_mp4로 보낼거임
            check_word = self.word_text.text()
            if check_word != self.end_string:
                self.word_text.setText(check_word)
                self.play_mp4(check_word)
        else:
            check_word = self.word_text.text()
            
            if check_word != self.end_string:
                # 해당 단어를 가지고 온다음에, 소리를 재생시키고
                self.play_mp4(check_word)
            
                # 억지로 딜레이를 걸긴 했는데, 이게 효과가 있을지 모르겠네
                time.sleep(1.5)
                self.checked_word_list.append(check_word)
                new_word = self.check_available_word()
                

                if new_word == self.end_string or new_word == "Please choose pronunciation.":
                    self.timer.stop()
                    self.isPlayer = False
                    self.checked_word_list.clear()
                else:
                    self.word_text.setText(new_word)
            # else:
            #     # 생각해보니까 이것도 checked_list를 기반으로 하는거지
            #     # 그럼 어쩔수가 없네 다른 방식을 고안해야겠음.
            #     self.word_text.setText(self.check_available_word())
    
        
        
    # 선택 가능한 단어를 확인.                   
    def check_available_word(self) -> str:
        if self.keys_list is not None and len(self.checked_word_list) != 0:
            available_words = set(self.keys_list) - set(self.checked_word_list)
            if available_words:
                selected_word = self.secure_random.choice(list(available_words))
                return selected_word
            else:
                return self.end_string
        else:
            self.word_text.setText(self.end_string)
            print("단어 존재하지 않음.")
            
            
    def select_prpron(self, btn_text) -> None:
        
        # There isn't pre_pron
        if self.prev_pron is None:
            self.sender().setStyleSheet('color: orange')
            self.prev_pron = self.sender()
            self.set_pronun_and_tld(btn_text)   
        else:
            # 이전에 선택한 버튼이 있을 때
            if self.prev_pron == self.sender():
                # 같은 버튼을 다시 클릭했을 때 토글
                current_style = self.sender().styleSheet()
                if 'color: orange' in current_style:
                    self.sender().setStyleSheet('color: white')
                elif 'color: white' in current_style:
                    self.sender().setStyleSheet('color: orange')
                
                # 같은 버튼을 다시 클릭했으므로, 발음과 tld 초기화
                self.pron = None
                self.tld = None
            else:
                # 다른 버튼을 클릭했을 때
                self.sender().setStyleSheet('color: orange')
                self.prev_pron.setStyleSheet('color: white')
                self.prev_pron = self.sender()
                # 발음 설정
                self.set_pronun_and_tld(btn_text)    
                
    # 발음 설정                                
    def set_pronun_and_tld(self, btn_text):
        if btn_text == "미국식 발음":
            self.pron = "en"
            self.tld = "com"
        elif btn_text == "영국식 발음":
            self.pron = "en"
            self.tld = "co.uk"
        else:
            self.pron = "en"
            self.tld = "com.au"        
            
            
    def listen_once(self):
        self.isPlayer = True
        check_word = self.word_text.text()
        
        if check_word != self.end_string or check_word != "Please choose pronunciation.":
            if self.pron != None and self.tld != None:
                self.play_sound(check_word)
                # self.global_obj.setStyleSheet("color: white")
            # else:
            #     # 만약 둘 중에 하나라도 선택이 되지 않았다면, 발음을 먼저 선택하라고 한다.
            #     self.word_text.setText("Please choose pronunciation.")
                
        else:
            self.word_text.setText(self.end_string)
            
        self.isPlayer= False
        
        # 이후에 만약 다시 듣기를 하고 싶다면 체크표시를 만들면됨.
                        
    def init_layout(self) -> None:
        self.isMouseEnter = False
        self.isListeningWidget = None
        self.setFocusPolicy(Qt.StrongFocus) # keyPressEvent 받기 위해서, 최초에 한번 받아주어야함.
        # self.setMouseTracking(True) # mouse button을 누르지 않아도, 트랙킹이 가능하도록 True 를 넘겨줌.
        # self.three_listening_buttons_coords = []
        
        self.current_mouse_x_pos = None
        self.current_mouse_y_pos = None
        
        
        self.word_text = QLabel("Select .txt file.")
        self.word_text.setStyleSheet("margin: 25px")
        self.word_text.setAlignment(Qt.AlignCenter)
        self.word_text.setFont(QFont("Arial", 25))
        
        
        layout_page_1 = QVBoxLayout(self)

        grid_layout = QGridLayout()

        self.names = ["미국식 발음", "영국식 발음", "호주식 발음", "이어서 듣기", "듣기", "한 단어 계속듣기", "다음 단어"]

        coords = [(i, j) for i in range(3) for j in range(3)]

        for name, coord in zip(self.names, coords):
            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
            if name in ("미국식 발음", "영국식 발음", "호주식 발음"):
                button.clicked.connect(self.click_book_btn)
            else:
                button.released.connect(self.click_book_btn)
                button.installEventFilter(self)
                
            grid_layout.addWidget(button, *coord)

        layout_page_1.addWidget(self.word_text)
        layout_page_1.addLayout(grid_layout)
        
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            text = obj.text()
            if text in ["듣기", "이어서 듣기", "한 단어 계속듣기"]:
               self.isMouseEnter = True 
               self.isListeningWidget = text
        return super().eventFilter(obj, event)

        
        
        
    def keyPressEvent(self, event):
        # 스페이스를 눌렀고, 그때 마우스가 리스닝 위젯에 들어와 있다면
        if event.key() == Qt.Key_Space:
        
            if self.isPlayer is False and self.isMouseEnter:
                if self.isListeningWidget == "듣기":
                    self.listen_once()
                elif self.isListeningWidget == "이어서 듣기":
                    self.continue_listening()
                elif self.isListeningWidget == "한 단어 계속듣기":  
                    self.continue_listening_for_a_word()
                    
            else:
                if self.isPlayer and self.isListeningWidget == "한 단어 계속듣기":
                    self.timer.stop()
                    self.isPlayer = False
                elif self.isPlayer is True:
                    print(f"{self.isPlayer} 이미 player가 동작중..")
                    
        
    def get_selected_book_name(self):
        return self.selected_word_book
    
    def set_selected_book_name(self, book_name):
        # 만약 선택한 단어장, 이전에 선택했던 단어장이랑 같지 않다면
        print(book_name, self.selected_word_book)
        # 음 if문 안으로 들어오는건 확실한데
        if book_name is not None:
            # 이전에 선택한 단어장 초기화
            self.word_book_dic = {}

            try:
                with open(book_name, "r") as file:
                    words = file.readlines()
                    for word in words:
                        # 콤마를 기준으로 분리한다.
                        # 콤마를 기준으로 분리 한다음에, result가 두개 이상인것
                        result = word.rstrip().split(",")
                        if len(result) >= 2:
                            # 단어: 뜻
                            self.word_book_dic[result[0]] = result[1]
                self.selected_word_book = book_name
                self.keys_list = list(self.word_book_dic.keys())
                print(self.keys_list)
                self.word_text.setText(self.secure_random.choice(self.keys_list))
            except Exception as e:
                print(f"{e.with_traceback}  + 발생.")
                
                
        elif book_name is not None:
            # 만약 선택한 단어장이 이전에 선택했던 단어장이랑 같다면
            # 결국 단어들만 새로 뽑으면됨.
            self.word_text.setText(self.secure_random.choice(self.keys_list))

        
'''
    @Class root layout for all page.
'''
class ToicWordApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_layout()
        self.show()
        pygame.mixer.init()
        self.internet_checker = InternetChecker(self)
        self.internet_checker.internet_status_signal.connect(self.handle_internet_status)
        self.internet_checker.start()
    


    
          
    def init_layout(self):
        self.stackedWidget = QStackedWidget()
        self.is_internet_connect = False
        self.connect_count = 0
        self.statusBar = self.statusBar()
        self.firstLayout = FirstPageLayout(self.stackedWidget)
        self.stackedWidget.addWidget(self.firstLayout)
        self.stackedWidget.addWidget(SecondPageLayout(self.stackedWidget, self.firstLayout))
        self.stackedWidget.addWidget(ThirdPageLayout(self.stackedWidget, self.firstLayout))

        self.setCentralWidget(self.stackedWidget)

        self.create_menubar()
        self.statusBar.showMessage("Connecting...")
        self.setWindowTitle('Central Widget')
        self.setGeometry(300, 300, 800, 700)


    def create_menubar(self) -> None:
        exitAction = QAction('종료', self)
        choiceWordBook = QAction('단어장 선택', self)
        addWordBook = QAction('단어장 추가', self)
        
        
        choiceWordBook.setStatusTip('단어장 선택')
        choiceWordBook.triggered.connect(self.move_to_secondPage)
        
        addWordBook.setStatusTip("단어장 추가")
        addWordBook.triggered.connect(self.move_to_thirdPage)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        settingMenu = menubar.addMenu('&설정')
        settingMenu.addAction(exitAction)

        programMenu = menubar.addMenu('&단어장')
        programMenu.addAction(choiceWordBook)
        programMenu.addAction(addWordBook)
        
        
    def move_to_thirdPage(self) -> None:
        self.stackedWidget.setCurrentIndex(2)

    def move_to_secondPage(self) -> None:
        self.stackedWidget.setCurrentIndex(1)

    def handle_internet_status(self, status) -> None:
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
    print(sys.path[0])
    app = QApplication(sys.argv)
    ex = ToicWordApp()
    sys.exit(app.exec_())

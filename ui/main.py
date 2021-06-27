import sys
import platform
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtCore import (QCoreApplication,QPropertyAnimation,QDate,QTime,QMetaObject,QObject,QPoint,QRect,QSize,QTime,QUrl,Qt,QEvent,QObject)
from PySide2.QtGui import (QBrush,QColor,QConicalGradient,QCursor,QFont,QFontDatabase,QIcon,QKeySequence,QLinearGradient,QPalette,QPainter,QPixmap,QRadialGradient)
from PySide2.QtWidgets import *
import time
# ====> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

# ====> LOGIN WINDOW
from ui_login import Ui_LoginWindow,sing

# ====> School Main Window
from ui_school_main import Ui_MainWindow

## ===> GLOBALS
counter = 0
## School MainWindow
WINDOW_SIZE = 0


class MainSchoolWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                ## UI ==> INTERFACE CODES
        #######################################
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
        ## DROP SHADOW EFFECT
        #self.shadow = QGraphicsDropShadowEffect(self)
        #self.shadow.setBlurRadius(20)
        #self.shadow.setXOffset(0)
        #self.shadow.setYOffset(0)
        #self.shadow.setColor(QColor(0,92,157,150))
        #self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        ## minimizeButton Window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # RestoreButton Window
        self.ui.maximizeButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # CloseButton Window
        self.ui.close_button.clicked.connect(lambda: self.close())

            # STACKED PAGES (DEFAULT/CURRENT PAGE)///////////////////////
    # SET THE PAGE THAT WILL BE VISIBLE BY DEFAULT WHEN THE APP IS OPENED
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashbord_page)
        ############################################################
        # /////////////////////////////////////////////////////////

        ################### stacked pages navigations ////////////////////
        # USING side menu buttons
        #navigate home pages
        self.ui.dashbord_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.dashbord_page))
        
        # Navigate to Meassage Page
        self.ui.messages_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.messages_page))

        # Navigate Students Page 
        self.ui.students_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.students_page))

        # Navigate Teachers Page
        self.ui.teachers_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.teachers_page))

        # Navigate Laser Page
        self.ui.laser_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.laser_page))

        # Navigate ClassRoomS 
        self.ui.classrooms_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.classrooms_page))

        # Navigate ADD USERPAGE
        self.ui.adduser_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.adduser_page))
        
        # Navigate Attendance Page
        self.ui.attendance_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.attendance_page))
        
        # Navigate Result Page
        self.ui.results_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.results_page))

        # Navigate backup Page
        self.ui.backup_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.backup_page))

        # Navigate Setting Page
        self.ui.settings_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page))
        
        # Start Menu Button Style ////////////////////
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
        # MOVE wINDOW ON MOUSE DRAG EVENT ON THE TITLE BAR
        ################################################################
        def moveWindow(e):
            # Detect if the window is normal size
            ###############################################################
            ##################
            if self.isMaximized() == False:
                #################################
                #Move window only when window is Normal size
                #############################################
                # If left mouse button is clicked
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos()+e.globalPos()-self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            ####################################################################     
    # Add click Event to the top header to move the window###############
        self.ui.main_header.mouseMoveEvent = moveWindow
    ###########################################################
    # SlideBar Left Menu################################################
    ####################################
        self.ui.left_menu_toggle_buttons.clicked.connect(lambda:self.slideLeftMenu())
        QSizeGrip(self.ui.size_grip)
    ##########################################################################
    # Add mouse events to the window
    ############################################################################
    def mousePressEvent(self, event):
        #######################################################################
        # Get the current Position of the mouse #############################
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        #####################################################################

    # restore_or_maximize_window
    def restore_or_maximize_window(self):
        # Global Window State
        global WINDOW_SIZE # default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1 # Update the value that window has been maximized
            self.showMaximized() 
            self.ui.maximizeButton.setIcon(QtGui.QIcon(u"icons/restore-window-24.png"))
            
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0# Update the value that window has been minimized
            self.showNormal()    #normal size/minimized size(850,700)   

            #Update Button icon When Window is minimized
            self.ui.maximizeButton.setIcon(QtGui.QIcon(u"icons/maximize-window-24.png"))
    
        
        ###########################################################
        ######################
        # End Menu buttons Styling 
        ######################################################################
        ##################

        # Start Menu Buttons Styling
        ################################################
    def applyButtonStyle(self):
        #Reset Style for other Button
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                defaultStyle = w.styleSheet().replace("border-left:2px solid rgb(0,136,255);border-bottom:2px solid rgb(0,136,255);"," ")
                # Create default Style
                w.setStyleSheet(defaultStyle)
        # Apply new style
        # sender = clicked button
        # Get the clicked button style and add new one
        newStyle = self.sender().styleSheet() + ("border-left:2px solid rgb(0,136,255);border-bottom:2px solid rgb(0,136,255);")
        self.sender().setStyleSheet(newStyle)
        #
        return
    
    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()
        if width == 40:
            # Expand Menu
            newwidth = 145
        else:
            # Restore Menu
            newwidth = 40
    #Animation he transition
        self.animation = QPropertyAnimation(self.ui.left_side_menu,b"minimumWidth")
        # Animate minimumWidth
        self.animation.setDuration(250)
        self.animation.setStartValue(width) # Stating value is the current menu width
        self.animation.setEndValue(newwidth) #  ending value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    ##################################################################################
    
##=====> LOGIN WINDOW
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
                ## UI ==> INTERFACE CODES
        #######################################
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def button_CloseClicked(self):
            print("Close Button Clicked")
            login_window.close()
        #a = Ui_LoginWindow.button_click
        def get_login_details():
            details = sing.loginsignal()
            print(details[0][-1])
            if details[0][-1] == 'admin' and details[1][-1] == '1234':
                self.ui.label_5.setText(QCoreApplication.translate("LoginWindow", u"", None))
                main_school_window.show()
                login_window.close()
            else:
                self.ui.label_5.setText(QCoreApplication.translate("LoginWindow", u"Incorrect Username and Password ", None))

        self.ui.button_close.clicked.connect(button_CloseClicked)
        self.ui.pushButton.clicked.connect(get_login_details)
    





##============> SPLASH SCREEN 
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        #######################################
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTimer ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECOND
        self.timer.start(35)


        ## SHOW ==> Splash WINDOW
        ###########################################
        self.show()
        ## ===> END ##

    ## ==> App FUNCTIONS
    ######################################################
    def progress(self):
        global counter
        #SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
        # Close SPLASH SCREEN AND OPEN APP
        if counter >100:
            #STOP TImer
            self.timer.stop()
            # SHOW Login SCREEN
            login_window.show()
            # CLOSE SPLASH SCREEN
            self.close()
            

        # INCREASE COUNTER
        counter +=1


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    #window.close()
    login_window = LoginWindow()
    main_school_window = MainSchoolWindow()
    
    #login_window.close()
    #login_window.close()
    sys.exit(app.exec_())
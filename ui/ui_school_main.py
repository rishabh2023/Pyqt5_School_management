# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'school_maingENoio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(842, 724)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(25,25,25);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"\n"
"QFrame{\n"
"border-bottom:1px solid #000;\n"
"background-color:#000;\n"
"}")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.main_header.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setCursor(QCursor(Qt.ArrowCursor))
        self.title_bar_container.setStyleSheet(u"")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.title_bar_container.setLineWidth(1)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.left_menu_toggle.setLineWidth(1)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_buttons = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_buttons.setObjectName(u"left_menu_toggle_buttons")
        self.left_menu_toggle_buttons.setMinimumSize(QSize(0, 50))
        self.left_menu_toggle_buttons.setMaximumSize(QSize(16777215, 50))
        self.left_menu_toggle_buttons.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:5px 10px;\n"
"border:none;\n"
"border-radius:5px;\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 85, 255);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/icons8-menu-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_buttons.setIcon(icon)
        self.left_menu_toggle_buttons.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_menu_toggle_buttons)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setCursor(QCursor(Qt.CrossCursor))
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.title_bar.setLineWidth(1)

        self.horizontalLayout_5.addWidget(self.title_bar)


        self.horizontalLayout_2.addWidget(self.title_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"")
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.top_right_btns.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(0, 235, 0);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/minimize-window-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.top_right_btns)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(170, 0, 127)\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/maximize-window-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon2)
        self.maximizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.maximizeButton)

        self.close_button = QPushButton(self.top_right_btns)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icons/close-window-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_button)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMaximumSize(QSize(16777215, 16777215))
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.main_body.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(0, 0))
        self.left_side_menu.setMaximumSize(QSize(40, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"padding:20px 10px;\n"
"border:none;\n"
"border-left:2px solid transparent;\n"
"border-bottom:2px solid transparent;\n"
"border-radius:10px;\n"
"background-color:#000;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 85, 255);\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.left_side_menu.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setMinimumSize(QSize(120, 0))
        self.left_menu_top_buttons.setStyleSheet(u"")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.dashbord_btn = QPushButton(self.left_menu_top_buttons)
        self.dashbord_btn.setObjectName(u"dashbord_btn")
        self.dashbord_btn.setMinimumSize(QSize(100, 0))
        self.dashbord_btn.setStyleSheet(u"padding-left:10px;\n"
"background-position:center left;")
        icon4 = QIcon()
        icon4.addFile(u"icons/icons8-home-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashbord_btn.setIcon(icon4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dashbord_btn)

        self.messages_btn = QPushButton(self.left_menu_top_buttons)
        self.messages_btn.setObjectName(u"messages_btn")
        self.messages_btn.setMinimumSize(QSize(100, 0))
        self.messages_btn.setStyleSheet(u"padding-left:10px;")
        icon5 = QIcon()
        icon5.addFile(u"icons/icons8-edit-message-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.messages_btn.setIcon(icon5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.messages_btn)

        self.students_btn = QPushButton(self.left_menu_top_buttons)
        self.students_btn.setObjectName(u"students_btn")
        self.students_btn.setMinimumSize(QSize(100, 0))
        self.students_btn.setStyleSheet(u"padding-left:10px;")
        icon6 = QIcon()
        icon6.addFile(u"icons/icons8-accompany-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.students_btn.setIcon(icon6)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.students_btn)

        self.teachers_btn = QPushButton(self.left_menu_top_buttons)
        self.teachers_btn.setObjectName(u"teachers_btn")
        self.teachers_btn.setMinimumSize(QSize(100, 0))
        self.teachers_btn.setStyleSheet(u"padding-left:10px;")
        icon7 = QIcon()
        icon7.addFile(u"icons/teacher-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.teachers_btn.setIcon(icon7)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.teachers_btn)

        self.laser_btn = QPushButton(self.left_menu_top_buttons)
        self.laser_btn.setObjectName(u"laser_btn")
        self.laser_btn.setMinimumSize(QSize(100, 0))
        self.laser_btn.setSizeIncrement(QSize(0, 0))
        self.laser_btn.setStyleSheet(u"padding-left:10px;")
        icon8 = QIcon()
        icon8.addFile(u"icons/banknotes-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.laser_btn.setIcon(icon8)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.laser_btn)

        self.classrooms_btn = QPushButton(self.left_menu_top_buttons)
        self.classrooms_btn.setObjectName(u"classrooms_btn")
        self.classrooms_btn.setMinimumSize(QSize(100, 0))
        self.classrooms_btn.setStyleSheet(u"padding-left:10px;")
        icon9 = QIcon()
        icon9.addFile(u"icons/classroom-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classrooms_btn.setIcon(icon9)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.classrooms_btn)

        self.adduser_btn = QPushButton(self.left_menu_top_buttons)
        self.adduser_btn.setObjectName(u"adduser_btn")
        self.adduser_btn.setMinimumSize(QSize(100, 0))
        self.adduser_btn.setStyleSheet(u"padding-left:10px;")
        icon10 = QIcon()
        icon10.addFile(u"icons/add-user-2-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adduser_btn.setIcon(icon10)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.adduser_btn)

        self.attendance_btn = QPushButton(self.left_menu_top_buttons)
        self.attendance_btn.setObjectName(u"attendance_btn")
        self.attendance_btn.setMinimumSize(QSize(100, 0))
        self.attendance_btn.setSizeIncrement(QSize(0, 0))
        self.attendance_btn.setStyleSheet(u"padding-left:10px;")
        icon11 = QIcon()
        icon11.addFile(u"icons/address-book-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance_btn.setIcon(icon11)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.attendance_btn)

        self.results_btn = QPushButton(self.left_menu_top_buttons)
        self.results_btn.setObjectName(u"results_btn")
        self.results_btn.setMinimumSize(QSize(100, 0))
        self.results_btn.setStyleSheet(u"padding-left:10px;")
        icon12 = QIcon()
        icon12.addFile(u"icons/paper-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.results_btn.setIcon(icon12)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.results_btn)

        self.backup_btn = QPushButton(self.left_menu_top_buttons)
        self.backup_btn.setObjectName(u"backup_btn")
        self.backup_btn.setMinimumSize(QSize(100, 0))
        self.backup_btn.setStyleSheet(u"padding-left:10px;")
        icon13 = QIcon()
        icon13.addFile(u"icons/data-backup-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backup_btn.setIcon(icon13)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.backup_btn)


        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)

        self.settings_btn = QPushButton(self.left_side_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(100, 0))
        icon14 = QIcon()
        icon14.addFile(u"icons/settings-4-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon14)

        self.verticalLayout_2.addWidget(self.settings_btn)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_item = QFrame(self.main_body)
        self.center_main_item.setObjectName(u"center_main_item")
        self.center_main_item.setMaximumSize(QSize(16777215, 16777215))
        self.center_main_item.setStyleSheet(u"")
        self.center_main_item.setFrameShape(QFrame.StyledPanel)
        self.center_main_item.setFrameShadow(QFrame.Raised)
        self.center_main_item.setLineWidth(1)
        self.verticalLayout_14 = QVBoxLayout(self.center_main_item)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget = QStackedWidget(self.center_main_item)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.dashbord_page = QWidget()
        self.dashbord_page.setObjectName(u"dashbord_page")
        self.dashbord_page.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.dashbord_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.dashbord_page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.dashbord_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.messages_page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.messages_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.messages_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.messages_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.students_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.students_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.students_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.students_page)
        self.teachers_page = QWidget()
        self.teachers_page.setObjectName(u"teachers_page")
        self.verticalLayout_6 = QVBoxLayout(self.teachers_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.teachers_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.teachers_page)
        self.laser_page = QWidget()
        self.laser_page.setObjectName(u"laser_page")
        self.laser_page.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.laser_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.laser_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.laser_page)
        self.classrooms_page = QWidget()
        self.classrooms_page.setObjectName(u"classrooms_page")
        self.classrooms_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.classrooms_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.classrooms_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.classrooms_page)
        self.adduser_page = QWidget()
        self.adduser_page.setObjectName(u"adduser_page")
        self.adduser_page.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.adduser_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.adduser_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.adduser_page)
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName(u"attendance_page")
        self.attendance_page.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.attendance_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.attendance_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.attendance_page)
        self.results_page = QWidget()
        self.results_page.setObjectName(u"results_page")
        self.results_page.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.results_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.results_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.results_page)
        self.backup_page = QWidget()
        self.backup_page.setObjectName(u"backup_page")
        self.backup_page.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.backup_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.backup_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.backup_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.setting_page.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.setting_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.setting_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_14.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_item)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 0);\n"
"border-top-color: solid 1px #000;\n"
"}")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.main_footer.setLineWidth(1)
        self.horizontalLayout_6 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.main_footer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.size_grip = QFrame(self.main_footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_buttons.setText("")
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.close_button.setText("")
        self.dashbord_btn.setText(QCoreApplication.translate("MainWindow", u"  DASHBOARD  ", None))
        self.messages_btn.setText(QCoreApplication.translate("MainWindow", u"  MESSAGES   ", None))
        self.students_btn.setText(QCoreApplication.translate("MainWindow", u"  STUDENTS  ", None))
        self.teachers_btn.setText(QCoreApplication.translate("MainWindow", u"  TEACHERS  ", None))
        self.laser_btn.setText(QCoreApplication.translate("MainWindow", u"  LASER         ", None))
        self.classrooms_btn.setText(QCoreApplication.translate("MainWindow", u"  CLASSROOMS", None))
        self.adduser_btn.setText(QCoreApplication.translate("MainWindow", u"  ADD USER  ", None))
        self.attendance_btn.setText(QCoreApplication.translate("MainWindow", u"  ATTENDANCE", None))
        self.results_btn.setText(QCoreApplication.translate("MainWindow", u"  RESULT        ", None))
        self.backup_btn.setText(QCoreApplication.translate("MainWindow", u"  BACKUP     ", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"    SETTINGS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DASHBORDS PAGE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MESSAGES PAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"STUDENTS PAGE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TEACHERS PAGE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LASER PAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CLASSROOMS PAGE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ADD NEW USER PAGE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE PAGE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"RESULT PAGE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"BACKUP PAGE", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"SETTINGS PAGE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"v 2.0.0", None))
    # retranslateUi


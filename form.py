# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)
import res
import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1325, 822)
        MainWindow.setMinimumSize(QSize(1250, 820))
        MainWindow.setMaximumSize(QSize(2120, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:none;\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(960, 50))
        self.frame_3.setMaximumSize(QSize(1920, 100))
        self.frame_3.setStyleSheet(u"background-color:rgb(36, 36, 36);\n"
"border:none;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(215, 680))
        self.frame.setMaximumSize(QSize(215, 980))
        self.frame.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"border:none;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(180, 120))
        self.frame_12.setMaximumSize(QSize(190, 125))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_70 = QPushButton(self.frame_12)
        self.pushButton_70.setObjectName(u"pushButton_70")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_for_right_half.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_70.setIcon(icon)
        self.pushButton_70.setIconSize(QSize(170, 120))

        self.verticalLayout_11.addWidget(self.pushButton_70)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.left_widget = QTabWidget(self.frame)
        self.left_widget.setObjectName(u"left_widget")
        self.left_widget.setMinimumSize(QSize(202, 300))
        self.left_widget.setMaximumSize(QSize(202, 450))
        self.left_widget.setStyleSheet(u"")
        self.first_tab_left = QWidget()
        self.first_tab_left.setObjectName(u"first_tab_left")
        self.first_tab_left.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.first_tab_left)
        self.verticalLayout_15.setSpacing(50)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 18, 0, 18)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_73 = QPushButton(self.first_tab_left)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setMinimumSize(QSize(40, 40))
        self.pushButton_73.setMaximumSize(QSize(45, 45))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/google-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_73.setIcon(icon1)
        self.pushButton_73.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.pushButton_73)

        self.label_20 = QLabel(self.first_tab_left)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font-size:14px;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"padding:1px;")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_20)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_76 = QPushButton(self.first_tab_left)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setMinimumSize(QSize(40, 40))
        self.pushButton_76.setMaximumSize(QSize(45, 45))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/galaxy-store.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_76.setIcon(icon2)
        self.pushButton_76.setIconSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.pushButton_76)

        self.label_21 = QLabel(self.first_tab_left)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-size:14px;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"padding:1px;")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_21)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_77 = QPushButton(self.first_tab_left)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setMinimumSize(QSize(30, 30))
        self.pushButton_77.setMaximumSize(QSize(45, 45))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/Huawei_AppGallery.svg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_77.setIcon(icon3)
        self.pushButton_77.setIconSize(QSize(40, 40))

        self.horizontalLayout_15.addWidget(self.pushButton_77)

        self.label_22 = QLabel(self.first_tab_left)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font-size:14px;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"padding:1px;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_22)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_78 = QPushButton(self.first_tab_left)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setMinimumSize(QSize(40, 40))
        self.pushButton_78.setMaximumSize(QSize(45, 45))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/appstore.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_78.setIcon(icon4)
        self.pushButton_78.setIconSize(QSize(40, 40))

        self.horizontalLayout_16.addWidget(self.pushButton_78)

        self.label_23 = QLabel(self.first_tab_left)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font-size:14px;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"padding:1px;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_23)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.left_widget.addTab(self.first_tab_left, "")
        self.second_tab_left = QWidget()
        self.second_tab_left.setObjectName(u"second_tab_left")
        self.verticalLayout_9 = QVBoxLayout(self.second_tab_left)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.toolBox = QToolBox(self.second_tab_left)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(190, 180))
        self.toolBox.setMaximumSize(QSize(190, 210))
        self.toolBox.setStyleSheet(u"font-size:18px;\n"
"background-color:rgb(19, 30, 20);\n"
"color:rgb(245, 245, 245);\n"
"border-radius:6px;\n"
"padding:5px;\n"
"border:none;\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 90, 20))
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 158, 87))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color:rgb(66, 143, 131);\n"
"border-radius:6px;\n"
"")

        self.verticalLayout_6.addWidget(self.comboBox)

        self.pushButton_65 = QPushButton(self.layoutWidget)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_65.setStyleSheet(u"background-color:rgb(64, 170, 64);\n"
"border-radius:6px;\n"
"border:none;\n"
"text-align:left;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_65.setIcon(icon5)

        self.verticalLayout_6.addWidget(self.pushButton_65)

        self.toolBox.addItem(self.page, u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0431\u043e\u0442\u043e\u043c")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 170, 114))
        self.layoutWidget_2 = QWidget(self.page_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 10, 166, 103))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 10, 6, 10)
        self.checkBox = QCheckBox(self.layoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background-color:rgb(66, 143, 131);\n"
"border-radius:6px;")

        self.verticalLayout_7.addWidget(self.checkBox)

        self.start_game_2_players = QPushButton(self.layoutWidget_2)
        self.start_game_2_players.setObjectName(u"start_game_2_players")
        self.start_game_2_players.setStyleSheet(u"background-color:rgb(64, 170, 64);\n"
"border-radius:6px;\n"
"border:none;\n"
"text-align:left;")
        self.start_game_2_players.setIcon(icon5)

        self.verticalLayout_7.addWidget(self.start_game_2_players)

        self.toolBox.addItem(self.page_2, u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0434\u0440\u0443\u0433\u043e\u043c")

        self.verticalLayout_9.addWidget(self.toolBox)

        self.frame_11 = QFrame(self.second_tab_left)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(130, 20))
        self.frame_11.setMaximumSize(QSize(160, 30))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.stop_game = QPushButton(self.frame_11)
        self.stop_game.setObjectName(u"stop_game")
        self.stop_game.setMinimumSize(QSize(130, 20))
        self.stop_game.setMaximumSize(QSize(160, 30))
        self.stop_game.setStyleSheet(u"font-size:16px;\n"
"color:rgb(245, 245, 245);\n"
"background-color:rgb(182, 69, 69);\n"
"border-radius:6px;\n"
"padding:5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_game.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.stop_game)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.frame_15 = QFrame(self.second_tab_left)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(135, 25))
        self.frame_15.setMaximumSize(QSize(170, 50))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.settings = QPushButton(self.frame_15)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(130, 20))
        self.settings.setMaximumSize(QSize(160, 30))
        self.settings.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:6px;\n"
"padding:5px;\n"
"font-size:16px;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings.setIcon(icon7)

        self.horizontalLayout_17.addWidget(self.settings)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.left_widget.addTab(self.second_tab_left, "")

        self.verticalLayout_5.addWidget(self.left_widget)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(130, 20))
        self.frame_9.setMaximumSize(QSize(160, 30))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.rules_of_play = QPushButton(self.frame_9)
        self.rules_of_play.setObjectName(u"rules_of_play")
        self.rules_of_play.setMinimumSize(QSize(130, 20))
        self.rules_of_play.setMaximumSize(QSize(160, 30))
        self.rules_of_play.setStyleSheet(u"font-size:16px;\n"
"color:rgb(245, 245, 245);\n"
"background-color:rgb(66, 143, 131);\n"
"border-radius:6px;\n"
"padding:2px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rules_of_play.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.rules_of_play)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(130, 20))
        self.frame_17.setMaximumSize(QSize(160, 30))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(130, 20))
        self.frame_16.setMaximumSize(QSize(160, 30))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(700, 700))
        self.frame_2.setMaximumSize(QSize(980, 980))
        self.frame_2.setStyleSheet(u"border:none;\n"
"background-color:rgb(24, 24, 24);\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.central_widget = QTabWidget(self.frame_2)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setMinimumSize(QSize(670, 680))
        self.central_widget.setMaximumSize(QSize(980, 982))
        self.central_widget.setStyleSheet(u"border:none;\n"
"font-size:12px;")
        self.first_cenral_widget = QWidget()
        self.first_cenral_widget.setObjectName(u"first_cenral_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.first_cenral_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.first_cenral_widget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(670, 680))
        self.frame_10.setMaximumSize(QSize(980, 982))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u"images/backg.jpeg"))

        self.horizontalLayout_20.addWidget(self.label_18)


        self.verticalLayout_8.addWidget(self.frame_26)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color:rgb(24, 24, 24);\n"
"")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(150, 15, 150, -1)
        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.leave_the_game = QPushButton(self.frame_14)
        self.leave_the_game.setObjectName(u"leave_the_game")
        self.leave_the_game.setStyleSheet(u"font-size:14px;\n"
"color:rgb(255, 255, 255);\n"
"padding:5px;\n"
"background-color:rgb(255, 95, 80);\n"
"border:none;\n"
"border-radius:6px;")

        self.horizontalLayout_7.addWidget(self.leave_the_game)

        self.start_the_game = QPushButton(self.frame_14)
        self.start_the_game.setObjectName(u"start_the_game")
        self.start_the_game.setStyleSheet(u"font-size:14px;\n"
"color:rgb(255, 255, 255);\n"
"padding:5px;\n"
"background-color:rgb(75, 134, 35);\n"
"border:none;\n"
"border-radius:6px;")

        self.horizontalLayout_7.addWidget(self.start_the_game)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.central_widget.addTab(self.first_cenral_widget, "")
        self.second_central_widget = QWidget()
        self.second_central_widget.setObjectName(u"second_central_widget")
        self.second_central_widget.setStyleSheet(u"border:none;\n"
"background-color:rgb(24, 24, 24)\n"
";")
        self.verticalLayout_3 = QVBoxLayout(self.second_central_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_28 = QFrame(self.second_central_widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(665, 10))
        self.frame_28.setMaximumSize(QSize(970, 15))
        self.frame_28.setSizeIncrement(QSize(0, 0))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, 0, 5, 4)
        self.label_47 = QLabel(self.frame_28)
        self.label_47.setObjectName(u"label_47")
        font = QFont()
        font.setBold(True)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_28)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_48)

        self.label_49 = QLabel(self.frame_28)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_49)

        self.label_50 = QLabel(self.frame_28)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_50)

        self.label_51 = QLabel(self.frame_28)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_51)

        self.label_52 = QLabel(self.frame_28)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)
        self.label_52.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_52)

        self.label_54 = QLabel(self.frame_28)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(1, 10))
        self.label_54.setSizeIncrement(QSize(970, 12))
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_54)

        self.label_53 = QLabel(self.frame_28)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)
        self.label_53.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_53)


        self.verticalLayout_3.addWidget(self.frame_28)

        self.frame_5 = QFrame(self.second_central_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(30, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"border:none;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_40 = QPushButton(self.frame_5)
        self.button_40.setObjectName(u"button_40")
        self.button_40.setMinimumSize(QSize(83, 83))
        self.button_40.setMaximumSize(QSize(123, 123))
        self.button_40.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_40.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_40, 3, 1, 1, 1)

        self.button_35 = QPushButton(self.frame_5)
        self.button_35.setObjectName(u"button_35")
        self.button_35.setMinimumSize(QSize(83, 83))
        self.button_35.setMaximumSize(QSize(123, 123))
        self.button_35.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_35.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_35, 4, 6, 1, 1)

        self.button_52 = QPushButton(self.frame_5)
        self.button_52.setObjectName(u"button_52")
        self.button_52.setMinimumSize(QSize(83, 83))
        self.button_52.setMaximumSize(QSize(123, 123))
        self.button_52.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_52.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_52, 2, 3, 1, 1)

        self.button_37 = QPushButton(self.frame_5)
        self.button_37.setObjectName(u"button_37")
        self.button_37.setMinimumSize(QSize(83, 83))
        self.button_37.setMaximumSize(QSize(123, 123))
        self.button_37.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_37.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_37, 4, 8, 1, 1)

        self.button_64 = QPushButton(self.frame_5)
        self.button_64.setObjectName(u"button_64")
        self.button_64.setMinimumSize(QSize(83, 83))
        self.button_64.setMaximumSize(QSize(123, 123))
        self.button_64.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/black_figure_default.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_64.setIcon(icon9)
        self.button_64.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_64, 1, 5, 1, 1)

        self.button_55 = QPushButton(self.frame_5)
        self.button_55.setObjectName(u"button_55")
        self.button_55.setMinimumSize(QSize(83, 83))
        self.button_55.setMaximumSize(QSize(123, 123))
        self.button_55.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_55.setIcon(icon9)
        self.button_55.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_55, 2, 6, 1, 1)

        self.frame_27 = QFrame(self.frame_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(10, 670))
        self.frame_27.setMaximumSize(QSize(14, 970))
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_27)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 0, 0, 0)
        self.label_39 = QLabel(self.frame_27)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)
        self.label_39.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_27)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_27)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_27)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_27)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_27)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_27)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_27)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_46)


        self.gridLayout.addWidget(self.frame_27, 0, 9, 8, 1)

        self.button_65 = QPushButton(self.frame_5)
        self.button_65.setObjectName(u"button_65")
        self.button_65.setMinimumSize(QSize(83, 83))
        self.button_65.setMaximumSize(QSize(123, 123))
        self.button_65.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_65.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_65, 1, 6, 1, 1)

        self.button_11 = QPushButton(self.frame_5)
        self.button_11.setObjectName(u"button_11")
        self.button_11.setMinimumSize(QSize(83, 83))
        self.button_11.setMaximumSize(QSize(123, 123))
        self.button_11.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/white_figure_default.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_11.setIcon(icon10)
        self.button_11.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_11, 6, 2, 1, 1)

        self.button_74 = QPushButton(self.frame_5)
        self.button_74.setObjectName(u"button_74")
        self.button_74.setMinimumSize(QSize(83, 83))
        self.button_74.setMaximumSize(QSize(123, 123))
        self.button_74.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_74.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_74, 0, 5, 1, 1)

        self.button_46 = QPushButton(self.frame_5)
        self.button_46.setObjectName(u"button_46")
        self.button_46.setMinimumSize(QSize(83, 83))
        self.button_46.setMaximumSize(QSize(123, 123))
        self.button_46.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_46.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_46, 3, 7, 1, 1)

        self.button_25 = QPushButton(self.frame_5)
        self.button_25.setObjectName(u"button_25")
        self.button_25.setMinimumSize(QSize(83, 83))
        self.button_25.setMaximumSize(QSize(123, 123))
        self.button_25.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_25.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_25, 5, 6, 1, 1)

        self.button_66 = QPushButton(self.frame_5)
        self.button_66.setObjectName(u"button_66")
        self.button_66.setMinimumSize(QSize(83, 83))
        self.button_66.setMaximumSize(QSize(123, 123))
        self.button_66.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_66.setIcon(icon9)
        self.button_66.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_66, 1, 7, 1, 1)

        self.button_42 = QPushButton(self.frame_5)
        self.button_42.setObjectName(u"button_42")
        self.button_42.setMinimumSize(QSize(83, 83))
        self.button_42.setMaximumSize(QSize(123, 123))
        self.button_42.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_42.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_42, 3, 3, 1, 1)

        self.button_72 = QPushButton(self.frame_5)
        self.button_72.setObjectName(u"button_72")
        self.button_72.setMinimumSize(QSize(83, 83))
        self.button_72.setMaximumSize(QSize(123, 123))
        self.button_72.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_72.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_72, 0, 3, 1, 1)

        self.button_32 = QPushButton(self.frame_5)
        self.button_32.setObjectName(u"button_32")
        self.button_32.setMinimumSize(QSize(83, 83))
        self.button_32.setMaximumSize(QSize(123, 123))
        self.button_32.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_32.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_32, 4, 3, 1, 1)

        self.button_21 = QPushButton(self.frame_5)
        self.button_21.setObjectName(u"button_21")
        self.button_21.setMinimumSize(QSize(83, 83))
        self.button_21.setMaximumSize(QSize(123, 123))
        self.button_21.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_21.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_21, 5, 2, 1, 1)

        self.button_16 = QPushButton(self.frame_5)
        self.button_16.setObjectName(u"button_16")
        self.button_16.setMinimumSize(QSize(83, 83))
        self.button_16.setMaximumSize(QSize(123, 123))
        self.button_16.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_16.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_16, 6, 7, 1, 1)

        self.button_61 = QPushButton(self.frame_5)
        self.button_61.setObjectName(u"button_61")
        self.button_61.setMinimumSize(QSize(83, 83))
        self.button_61.setMaximumSize(QSize(123, 123))
        self.button_61.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_61.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_61, 1, 2, 1, 1)

        self.button_60 = QPushButton(self.frame_5)
        self.button_60.setObjectName(u"button_60")
        self.button_60.setMinimumSize(QSize(83, 83))
        self.button_60.setMaximumSize(QSize(123, 123))
        self.button_60.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_60.setIcon(icon9)
        self.button_60.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_60, 1, 1, 1, 1)

        self.button_22 = QPushButton(self.frame_5)
        self.button_22.setObjectName(u"button_22")
        self.button_22.setMinimumSize(QSize(83, 83))
        self.button_22.setMaximumSize(QSize(123, 123))
        self.button_22.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_22.setIcon(icon10)
        self.button_22.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_22, 5, 3, 1, 1)

        self.button_04 = QPushButton(self.frame_5)
        self.button_04.setObjectName(u"button_04")
        self.button_04.setMinimumSize(QSize(83, 83))
        self.button_04.setMaximumSize(QSize(123, 123))
        self.button_04.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_04.setIcon(icon10)
        self.button_04.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_04, 7, 5, 1, 1)

        self.button_13 = QPushButton(self.frame_5)
        self.button_13.setObjectName(u"button_13")
        self.button_13.setMinimumSize(QSize(83, 83))
        self.button_13.setMaximumSize(QSize(123, 123))
        self.button_13.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_13.setIcon(icon10)
        self.button_13.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_13, 6, 4, 1, 1)

        self.button_43 = QPushButton(self.frame_5)
        self.button_43.setObjectName(u"button_43")
        self.button_43.setMinimumSize(QSize(83, 83))
        self.button_43.setMaximumSize(QSize(123, 123))
        self.button_43.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_43.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_43, 3, 4, 1, 1)

        self.button_56 = QPushButton(self.frame_5)
        self.button_56.setObjectName(u"button_56")
        self.button_56.setMinimumSize(QSize(83, 83))
        self.button_56.setMaximumSize(QSize(123, 123))
        self.button_56.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_56.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_56, 2, 7, 1, 1)

        self.button_45 = QPushButton(self.frame_5)
        self.button_45.setObjectName(u"button_45")
        self.button_45.setMinimumSize(QSize(83, 83))
        self.button_45.setMaximumSize(QSize(123, 123))
        self.button_45.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_45.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_45, 3, 6, 1, 1)

        self.button_62 = QPushButton(self.frame_5)
        self.button_62.setObjectName(u"button_62")
        self.button_62.setMinimumSize(QSize(83, 83))
        self.button_62.setMaximumSize(QSize(123, 123))
        self.button_62.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_62.setIcon(icon9)
        self.button_62.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_62, 1, 3, 1, 1)

        self.button_34 = QPushButton(self.frame_5)
        self.button_34.setObjectName(u"button_34")
        self.button_34.setMinimumSize(QSize(83, 83))
        self.button_34.setMaximumSize(QSize(122, 122))
        self.button_34.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_34.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_34, 4, 5, 1, 1)

        self.button_33 = QPushButton(self.frame_5)
        self.button_33.setObjectName(u"button_33")
        self.button_33.setMinimumSize(QSize(83, 83))
        self.button_33.setMaximumSize(QSize(123, 123))
        self.button_33.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_33.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_33, 4, 4, 1, 1)

        self.button_27 = QPushButton(self.frame_5)
        self.button_27.setObjectName(u"button_27")
        self.button_27.setMinimumSize(QSize(83, 83))
        self.button_27.setMaximumSize(QSize(123, 123))
        self.button_27.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_27.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_27, 5, 8, 1, 1)

        self.button_41 = QPushButton(self.frame_5)
        self.button_41.setObjectName(u"button_41")
        self.button_41.setMinimumSize(QSize(83, 83))
        self.button_41.setMaximumSize(QSize(123, 123))
        self.button_41.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_41.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_41, 3, 2, 1, 1)

        self.button_26 = QPushButton(self.frame_5)
        self.button_26.setObjectName(u"button_26")
        self.button_26.setMinimumSize(QSize(83, 83))
        self.button_26.setMaximumSize(QSize(123, 123))
        self.button_26.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_26.setIcon(icon10)
        self.button_26.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_26, 5, 7, 1, 1)

        self.button_47 = QPushButton(self.frame_5)
        self.button_47.setObjectName(u"button_47")
        self.button_47.setMinimumSize(QSize(83, 83))
        self.button_47.setMaximumSize(QSize(123, 123))
        self.button_47.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_47.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_47, 3, 8, 1, 1)

        self.button_24 = QPushButton(self.frame_5)
        self.button_24.setObjectName(u"button_24")
        self.button_24.setMinimumSize(QSize(83, 83))
        self.button_24.setMaximumSize(QSize(123, 123))
        self.button_24.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_24.setIcon(icon10)
        self.button_24.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_24, 5, 5, 1, 1)

        self.button_10 = QPushButton(self.frame_5)
        self.button_10.setObjectName(u"button_10")
        self.button_10.setMinimumSize(QSize(83, 83))
        self.button_10.setMaximumSize(QSize(123, 123))
        self.button_10.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_10.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_10, 6, 1, 1, 1)

        self.button_30 = QPushButton(self.frame_5)
        self.button_30.setObjectName(u"button_30")
        self.button_30.setMinimumSize(QSize(83, 83))
        self.button_30.setMaximumSize(QSize(123, 123))
        self.button_30.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_30.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_30, 4, 1, 1, 1)

        self.button_57 = QPushButton(self.frame_5)
        self.button_57.setObjectName(u"button_57")
        self.button_57.setMinimumSize(QSize(83, 83))
        self.button_57.setMaximumSize(QSize(123, 123))
        self.button_57.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_57.setIcon(icon9)
        self.button_57.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_57, 2, 8, 1, 1)

        self.button_71 = QPushButton(self.frame_5)
        self.button_71.setObjectName(u"button_71")
        self.button_71.setMinimumSize(QSize(83, 83))
        self.button_71.setMaximumSize(QSize(123, 123))
        self.button_71.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_71.setIcon(icon9)
        self.button_71.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_71, 0, 2, 1, 1)

        self.button_54 = QPushButton(self.frame_5)
        self.button_54.setObjectName(u"button_54")
        self.button_54.setMinimumSize(QSize(83, 83))
        self.button_54.setMaximumSize(QSize(123, 123))
        self.button_54.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_54.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_54, 2, 5, 1, 1)

        self.button_15 = QPushButton(self.frame_5)
        self.button_15.setObjectName(u"button_15")
        self.button_15.setMinimumSize(QSize(83, 83))
        self.button_15.setMaximumSize(QSize(123, 123))
        self.button_15.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_15.setIcon(icon10)
        self.button_15.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_15, 6, 6, 1, 1)

        self.button_23 = QPushButton(self.frame_5)
        self.button_23.setObjectName(u"button_23")
        self.button_23.setMinimumSize(QSize(83, 83))
        self.button_23.setMaximumSize(QSize(123, 123))
        self.button_23.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_23.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_23, 5, 4, 1, 1)

        self.button_50 = QPushButton(self.frame_5)
        self.button_50.setObjectName(u"button_50")
        self.button_50.setMinimumSize(QSize(83, 83))
        self.button_50.setMaximumSize(QSize(123, 123))
        self.button_50.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_50.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_50, 2, 1, 1, 1)

        self.button_51 = QPushButton(self.frame_5)
        self.button_51.setObjectName(u"button_51")
        self.button_51.setMinimumSize(QSize(83, 83))
        self.button_51.setMaximumSize(QSize(123, 123))
        self.button_51.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_51.setIcon(icon9)
        self.button_51.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_51, 2, 2, 1, 1)

        self.button_44 = QPushButton(self.frame_5)
        self.button_44.setObjectName(u"button_44")
        self.button_44.setMinimumSize(QSize(83, 83))
        self.button_44.setMaximumSize(QSize(123, 123))
        self.button_44.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_44.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_44, 3, 5, 1, 1)

        self.button_17 = QPushButton(self.frame_5)
        self.button_17.setObjectName(u"button_17")
        self.button_17.setMinimumSize(QSize(83, 83))
        self.button_17.setMaximumSize(QSize(123, 123))
        self.button_17.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_17.setIcon(icon10)
        self.button_17.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_17, 6, 8, 1, 1)

        self.button_20 = QPushButton(self.frame_5)
        self.button_20.setObjectName(u"button_20")
        self.button_20.setMinimumSize(QSize(83, 83))
        self.button_20.setMaximumSize(QSize(123, 123))
        self.button_20.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_20.setIcon(icon10)
        self.button_20.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_20, 5, 1, 1, 1)

        self.button_14 = QPushButton(self.frame_5)
        self.button_14.setObjectName(u"button_14")
        self.button_14.setMinimumSize(QSize(83, 83))
        self.button_14.setMaximumSize(QSize(123, 123))
        self.button_14.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_14.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_14, 6, 5, 1, 1)

        self.button_03 = QPushButton(self.frame_5)
        self.button_03.setObjectName(u"button_03")
        self.button_03.setMinimumSize(QSize(83, 83))
        self.button_03.setMaximumSize(QSize(123, 123))
        self.button_03.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_03.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_03, 7, 4, 1, 1)

        self.button_00 = QPushButton(self.frame_5)
        self.button_00.setObjectName(u"button_00")
        self.button_00.setMinimumSize(QSize(83, 83))
        self.button_00.setMaximumSize(QSize(123, 123))
        self.button_00.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_00.setIcon(icon10)
        self.button_00.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_00, 7, 1, 1, 1)

        self.button_67 = QPushButton(self.frame_5)
        self.button_67.setObjectName(u"button_67")
        self.button_67.setMinimumSize(QSize(83, 83))
        self.button_67.setMaximumSize(QSize(123, 123))
        self.button_67.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_67.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_67, 1, 8, 1, 1)

        self.button_07 = QPushButton(self.frame_5)
        self.button_07.setObjectName(u"button_07")
        self.button_07.setMinimumSize(QSize(83, 83))
        self.button_07.setMaximumSize(QSize(123, 123))
        self.button_07.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_07.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_07, 7, 8, 1, 1)

        self.button_75 = QPushButton(self.frame_5)
        self.button_75.setObjectName(u"button_75")
        self.button_75.setMinimumSize(QSize(83, 83))
        self.button_75.setMaximumSize(QSize(123, 123))
        self.button_75.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_75.setIcon(icon9)
        self.button_75.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_75, 0, 6, 1, 1)

        self.button_73 = QPushButton(self.frame_5)
        self.button_73.setObjectName(u"button_73")
        self.button_73.setMinimumSize(QSize(83, 83))
        self.button_73.setMaximumSize(QSize(123, 123))
        self.button_73.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_73.setIcon(icon9)
        self.button_73.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_73, 0, 4, 1, 1)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(13, 670))
        self.frame_4.setMaximumSize(QSize(15, 970))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 3, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"color:rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 8, 1)

        self.button_06 = QPushButton(self.frame_5)
        self.button_06.setObjectName(u"button_06")
        self.button_06.setMinimumSize(QSize(83, 83))
        self.button_06.setMaximumSize(QSize(123, 123))
        self.button_06.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_06.setIcon(icon10)
        self.button_06.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_06, 7, 7, 1, 1)

        self.button_12 = QPushButton(self.frame_5)
        self.button_12.setObjectName(u"button_12")
        self.button_12.setMinimumSize(QSize(83, 83))
        self.button_12.setMaximumSize(QSize(123, 123))
        self.button_12.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_12.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_12, 6, 3, 1, 1)

        self.button_36 = QPushButton(self.frame_5)
        self.button_36.setObjectName(u"button_36")
        self.button_36.setMinimumSize(QSize(83, 83))
        self.button_36.setMaximumSize(QSize(123, 123))
        self.button_36.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_36.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_36, 4, 7, 1, 1)

        self.button_53 = QPushButton(self.frame_5)
        self.button_53.setObjectName(u"button_53")
        self.button_53.setMinimumSize(QSize(83, 83))
        self.button_53.setMaximumSize(QSize(123, 123))
        self.button_53.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_53.setIcon(icon9)
        self.button_53.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_53, 2, 4, 1, 1)

        self.button_31 = QPushButton(self.frame_5)
        self.button_31.setObjectName(u"button_31")
        self.button_31.setMinimumSize(QSize(83, 83))
        self.button_31.setMaximumSize(QSize(123, 123))
        self.button_31.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_31.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_31, 4, 2, 1, 1)

        self.button_02 = QPushButton(self.frame_5)
        self.button_02.setObjectName(u"button_02")
        self.button_02.setMinimumSize(QSize(83, 83))
        self.button_02.setMaximumSize(QSize(123, 123))
        self.button_02.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_02.setIcon(icon10)
        self.button_02.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_02, 7, 3, 1, 1)

        self.button_76 = QPushButton(self.frame_5)
        self.button_76.setObjectName(u"button_76")
        self.button_76.setMinimumSize(QSize(83, 83))
        self.button_76.setMaximumSize(QSize(123, 123))
        self.button_76.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_76.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_76, 0, 7, 1, 1)

        self.button_63 = QPushButton(self.frame_5)
        self.button_63.setObjectName(u"button_63")
        self.button_63.setMinimumSize(QSize(50, 50))
        self.button_63.setMaximumSize(QSize(123, 123))
        self.button_63.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_63.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_63, 1, 4, 1, 1)

        self.button_77 = QPushButton(self.frame_5)
        self.button_77.setObjectName(u"button_77")
        self.button_77.setMinimumSize(QSize(83, 83))
        self.button_77.setMaximumSize(QSize(123, 123))
        self.button_77.setStyleSheet(u"background-color:rgb(86, 100, 117);\n"
"border:none;")
        self.button_77.setIcon(icon9)
        self.button_77.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_77, 0, 8, 1, 1)

        self.button_01 = QPushButton(self.frame_5)
        self.button_01.setObjectName(u"button_01")
        self.button_01.setMinimumSize(QSize(83, 83))
        self.button_01.setMaximumSize(QSize(123, 123))
        self.button_01.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_01.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_01, 7, 2, 1, 1)

        self.button_70 = QPushButton(self.frame_5)
        self.button_70.setObjectName(u"button_70")
        self.button_70.setMinimumSize(QSize(83, 83))
        self.button_70.setMaximumSize(QSize(123, 123))
        self.button_70.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        icon11 = QIcon()
        icon11.addFile(u":/figures/white_checker.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_70.setIcon(icon11)
        self.button_70.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_70, 0, 1, 1, 1)

        self.button_05 = QPushButton(self.frame_5)
        self.button_05.setObjectName(u"button_05")
        self.button_05.setMinimumSize(QSize(83, 83))
        self.button_05.setMaximumSize(QSize(122, 122))
        self.button_05.setStyleSheet(u"background-color:rgb(239, 239, 239);\n"
"border:none;")
        self.button_05.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.button_05, 7, 6, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.second_central_widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(665, 10))
        self.frame_7.setMaximumSize(QSize(970, 15))
        self.frame_7.setStyleSheet(u"border:none;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 3, 5, 0)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"border:none;\n"
"font-size:12px;\n"
"color:rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_16)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.central_widget.addTab(self.second_central_widget, "")
        self.third_central_widget = QWidget()
        self.third_central_widget.setObjectName(u"third_central_widget")
        self.verticalLayout_12 = QVBoxLayout(self.third_central_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_13 = QFrame(self.third_central_widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setBold(False)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"font-size:24px;\n"
"color:rgb(252, 252, 252);\n"
"")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_19)

        self.verticalSpacer_8 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_8)

        self.textEdit_3 = QTextEdit(self.frame_13)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"color:rgb(221, 221, 221);")
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.textEdit_3)

        self.back_to_game = QPushButton(self.frame_13)
        self.back_to_game.setObjectName(u"back_to_game")
        self.back_to_game.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255,255,255);\n"
"font-size:16px;\n"
"padding:5px;\n"
"border-radius:6px;")

        self.verticalLayout_13.addWidget(self.back_to_game)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.central_widget.addTab(self.third_central_widget, "")

        self.verticalLayout_2.addWidget(self.central_widget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"border:none;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.right_widget = QTabWidget(self.frame_6)
        self.right_widget.setObjectName(u"right_widget")
        self.right_widget.setMinimumSize(QSize(240, 680))
        self.right_widget.setMaximumSize(QSize(550, 980))
        self.right_widget.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"border:none;")
        self.first_widget_right = QWidget()
        self.first_widget_right.setObjectName(u"first_widget_right")
        self.first_widget_right.setStyleSheet(u"background-color:rgb(40, 40, 40);")
        self.right_widget.addTab(self.first_widget_right, "")
        self.second_widget_right = QWidget()
        self.second_widget_right.setObjectName(u"second_widget_right")
        self.second_widget_right.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.second_widget_right)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.second_widget_right)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(240, 680))
        self.frame_8.setMaximumSize(QSize(550, 980))
        self.frame_8.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"border:none;\n"
"padding:3px;\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, -1, 10, -1)
        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"border-radius:7px;\n"
"")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"\n"
"color:rgb(234, 234, 234);\n"
"font-weight:300px;\n"
"font-size:16px;\n"
"\n"
"")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_16.addWidget(self.label_25)


        self.verticalLayout_19.addWidget(self.frame_20)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.frame_23 = QFrame(self.frame_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(150, 50))
        self.frame_23.setMaximumSize(QSize(545, 80))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_time = QLabel(self.frame_23)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(150, 40))
        self.label_time.setMaximumSize(QSize(190, 60))
        self.label_time.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"border:none;\n"
"padding:5px;\n"
"")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_time)


        self.verticalLayout_19.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(215, 400))
        self.frame_24.setMaximumSize(QSize(545, 470))
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.white_in_statistics_label = QLabel(self.frame_24)
        self.white_in_statistics_label.setObjectName(u"white_in_statistics_label")
        self.white_in_statistics_label.setStyleSheet(u"color:rgb(147, 147, 147);\n"
"font-weight:350px;\n"
"font-size:18px;")
        self.white_in_statistics_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.white_in_statistics_label)

        self.textEdit_4 = QTextEdit(self.frame_24)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(7,7,7);\n"
"font-size:12px;\n"
"border:none;\n"
"border-right:1px solid rgb(147,147,147);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 0;\n"
"border-bottom-right-radius: 0;")
        self.textEdit_4.setReadOnly(True)

        self.verticalLayout_23.addWidget(self.textEdit_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.black_in_statistics_label = QLabel(self.frame_24)
        self.black_in_statistics_label.setObjectName(u"black_in_statistics_label")
        self.black_in_statistics_label.setStyleSheet(u"color:rgb(147, 147, 147);\n"
"font-weight:350px;\n"
"font-size:18px;")
        self.black_in_statistics_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.black_in_statistics_label)

        self.textEdit_5 = QTextEdit(self.frame_24)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"font-size:12px;\n"
"border: none;\n"
"border-top-left-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"")
        self.textEdit_5.setReadOnly(True)

        self.verticalLayout_24.addWidget(self.textEdit_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_24)


        self.verticalLayout_19.addWidget(self.frame_24)

        self.frame_18 = QFrame(self.frame_8)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_8 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

        self.statistics = QPushButton(self.frame_18)
        self.statistics.setObjectName(u"statistics")
        self.statistics.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"padding:5px;\n"
"border:none;\n"
"border-radius:6px;")

        self.horizontalLayout_18.addWidget(self.statistics)

        self.horizontalSpacer_9 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)


        self.verticalLayout_19.addWidget(self.frame_18)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.right_widget.addTab(self.second_widget_right, "")
        self.third_widget_right = QWidget()
        self.third_widget_right.setObjectName(u"third_widget_right")
        self.third_widget_right.setStyleSheet(u"background-color:rgb(40, 40, 40);")
        self.horizontalLayout_13 = QHBoxLayout(self.third_widget_right)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.third_widget_right)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color:rgb(40, 40, 40);")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setSpacing(25)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(7, 10, 7, 10)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_9)

        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font-size:16px;\n"
"")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_17)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_2)

        self.textEdit_2 = QTextEdit(self.frame_25)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"background-color: rgb(7,7,7);\n"
"font-size:4px;\n"
"\n"
"border-radius:10px;\n"
"")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.textEdit_2)

        self.frame_19 = QFrame(self.frame_25)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.back_to_report = QPushButton(self.frame_19)
        self.back_to_report.setObjectName(u"back_to_report")
        self.back_to_report.setStyleSheet(u"background-color:rgb(20, 20, 20);\n"
"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"border-radius:6px;\n"
"border:none;\n"
"padding:5px;")

        self.horizontalLayout_19.addWidget(self.back_to_report)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_5)


        self.verticalLayout_25.addWidget(self.frame_19)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_3)


        self.horizontalLayout_13.addWidget(self.frame_25)

        self.right_widget.addTab(self.third_widget_right, "")

        self.verticalLayout_18.addWidget(self.right_widget)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.left_widget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        self.central_widget.setCurrentIndex(1)
        self.right_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_70.setText("")
        self.pushButton_73.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Play Market", None))
        self.pushButton_76.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u" Samsung Galaxy Store", None))
        self.pushButton_77.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Huawei AppGallery", None))
        self.pushButton_78.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Appstore", None))
        self.left_widget.setTabText(self.left_widget.indexOf(self.first_tab_left), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u043a\u0438\u0439", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b", None))

        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0431\u043e\u0442\u043e\u043c", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442 \u0434\u043e\u0441\u043a\u0438", None))
        self.start_game_2_players.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0434\u0440\u0443\u0433\u043e\u043c", None))
        self.stop_game.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.left_widget.setTabText(self.left_widget.indexOf(self.second_tab_left), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.rules_of_play.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.label_18.setText("")
        self.leave_the_game.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434 \u0438\u0437 \u0438\u0433\u0440\u044b", None))
        self.start_the_game.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.central_widget.setTabText(self.central_widget.indexOf(self.first_cenral_widget), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.button_40.setText("")
        self.button_35.setText("")
        self.button_52.setText("")
        self.button_37.setText("")
        self.button_64.setText("")
        self.button_55.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_65.setText("")
        self.button_11.setText("")
        self.button_74.setText("")
        self.button_46.setText("")
        self.button_25.setText("")
        self.button_66.setText("")
        self.button_42.setText("")
        self.button_72.setText("")
        self.button_32.setText("")
        self.button_21.setText("")
        self.button_16.setText("")
        self.button_61.setText("")
        self.button_60.setText("")
        self.button_22.setText("")
        self.button_04.setText("")
        self.button_13.setText("")
        self.button_43.setText("")
        self.button_56.setText("")
        self.button_45.setText("")
        self.button_62.setText("")
        self.button_34.setText("")
        self.button_33.setText("")
        self.button_27.setText("")
        self.button_41.setText("")
        self.button_26.setText("")
        self.button_47.setText("")
        self.button_24.setText("")
        self.button_10.setText("")
        self.button_30.setText("")
        self.button_57.setText("")
        self.button_71.setText("")
        self.button_54.setText("")
        self.button_15.setText("")
        self.button_23.setText("")
        self.button_50.setText("")
        self.button_51.setText("")
        self.button_44.setText("")
        self.button_17.setText("")
        self.button_20.setText("")
        self.button_14.setText("")
        self.button_03.setText("")
        self.button_00.setText("")
        self.button_67.setText("")
        self.button_07.setText("")
        self.button_75.setText("")
        self.button_73.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_06.setText("")
        self.button_12.setText("")
        self.button_36.setText("")
        self.button_53.setText("")
        self.button_31.setText("")
        self.button_02.setText("")
        self.button_76.setText("")
        self.button_63.setText("")
        self.button_77.setText("")
        self.button_01.setText("")
        self.button_70.setText("")
        self.button_05.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.central_widget.setTabText(self.central_widget.indexOf(self.second_central_widget), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b \"\u0428\u0430\u0448\u043a\u0438\"", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0441\u0441\u0442\u0430"
                        "\u043d\u043e\u0432\u043a\u0430:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u0433\u0440\u0430 \u0432\u0435\u0434\u0435\u0442\u0441\u044f \u043d\u0430 \u0434\u043e\u0441\u043a\u0435 8\u00d78 \u043a\u043b\u0435\u0442\u043e\u043a</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0423 \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0438\u0433\u0440\u043e\u043a\u0430 \u043f\u043e 12 \u0448\u0430\u0448\u0435\u043a</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0428\u0430\u0448\u043a\u0438 \u0440\u0430\u0441\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u043d\u0430 \u0447\u0435\u0440\u043d\u044b\u0445 \u043a\u043b\u0435\u0442"
                        "\u043a\u0430\u0445 \u0432 \u043f\u0435\u0440\u0432\u044b\u0445 \u0442\u0440\u0435\u0445 \u0440\u044f\u0434\u0430\u0445 \u0441 \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u043e\u0440\u043e\u043d\u044b</li></ul>\n"
"<ol start=\"2\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0425\u043e\u0434 \u0448\u0430\u0448\u043a\u0438:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0441\u0442\u044b\u0435 \u0448\u0430\u0448\u043a\u0438 \u0445\u043e\u0434\u044f\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u043f\u0435\u0440\u0435\u0434 \u043f\u043e \u0434\u0438\u0430\u0433"
                        "\u043e\u043d\u0430\u043b\u0438 \u043d\u0430 \u043e\u0434\u043d\u0443 \u043a\u043b\u0435\u0442\u043a\u0443</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0425\u043e\u0434\u0438\u0442\u044c \u043d\u0430\u0437\u0430\u0434 \u043f\u0440\u043e\u0441\u0442\u044b\u043c\u0438 \u0448\u0430\u0448\u043a\u0430\u043c\u0438 \u043d\u0435\u043b\u044c\u0437\u044f</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0415\u0441\u043b\u0438 \u0448\u0430\u0448\u043a\u0430 \u0434\u043e\u0441\u0442\u0438\u0433\u0430\u0435\u0442 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u0438 (\u0434\u0430\u043c\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u044f), \u043e\u043d\u0430 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0434\u0430\u043c\u043a\u043e\u0439</li></ul>\n"
"<ol start=\""
                        "3\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0412\u0437\u044f\u0442\u0438\u0435 (\u0431\u043e\u0439):</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0415\u0441\u043b\u0438 \u043f\u0435\u0440\u0435\u0434 \u0448\u0430\u0448\u043a\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0448\u0430\u0448\u043a\u0430 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430, \u0430 \u0437\u0430 \u043d\u0435\u0439 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0435 \u043f\u043e\u043b\u0435, \u0442\u043e \u0448\u0430\u0448\u043a\u0443 \u043f\u0440\u043e\u0442\u0438\u0432"
                        "\u043d\u0438\u043a\u0430 \u043d\u0443\u0436\u043d\u043e \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0432\u0437\u044f\u0442\u044c, \u043f\u0435\u0440\u0435\u043f\u0440\u044b\u0433\u043d\u0443\u0432 \u0447\u0435\u0440\u0435\u0437 \u043d\u0435\u0451</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0437\u044f\u0442\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442\u044c \u043a\u0430\u043a \u0432\u043f\u0435\u0440\u0435\u0434, \u0442\u0430\u043a \u0438 \u043d\u0430\u0437\u0430\u0434</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0430 \u043e\u0434\u0438\u043d \u0445\u043e\u0434 \u043c\u043e\u0436\u043d\u043e \u0432\u0437\u044f\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0448\u0430\u0448\u0435\u043a \u043f\u0440\u043e\u0442\u0438\u0432\u043d"
                        "\u0438\u043a\u0430</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0437\u044f\u0442\u0438\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e - \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0432\u0437\u044f\u0442\u044c \u0448\u0430\u0448\u043a\u0443 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430, \u0438\u0433\u0440\u043e\u043a \u043e\u0431\u044f\u0437\u0430\u043d \u044d\u0442\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c</li></ul>\n"
"<ol start=\"4\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0414\u0430\u043c\u043a\u0430:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px"
                        "; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043c\u043a\u0430 \u043c\u043e\u0436\u0435\u0442 \u0445\u043e\u0434\u0438\u0442\u044c \u043d\u0430 \u043b\u044e\u0431\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u0435\u0439 \u043f\u043e \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438 \u0432\u043f\u0435\u0440\u0435\u0434 \u0438 \u043d\u0430\u0437\u0430\u0434</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438 \u0432\u0437\u044f\u0442\u0438\u0438 \u0434\u0430\u043c\u043a\u0430 \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u044b\u0433\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0448\u0430\u0448\u043a\u0438 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430 \u043d\u0430 \u043b\u044e\u0431\u043e\u0435"
                        " \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u043f\u043e \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438 \u0437\u0430 \u043d\u0438\u043c\u0438</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043c\u043a\u0430 \u0442\u0430\u043a\u0436\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u0430 \u0431\u0440\u0430\u0442\u044c \u0448\u0430\u0448\u043a\u0438 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430 \u043f\u0440\u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438</li></ul>\n"
"<ol start=\"5\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u043f\u043e\u0431\u0435\u0434\u044b:</span></li></o"
                        "l>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0438\u0433\u0440\u044b\u0432\u0430\u0435\u0442 \u0442\u043e\u0442, \u043a\u0442\u043e \u043f\u0435\u0440\u0432\u044b\u043c \u0443\u043d\u0438\u0447\u0442\u043e\u0436\u0438\u0442 \u0432\u0441\u0435 \u0448\u0430\u0448\u043a\u0438 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0430\u043a\u0436\u0435 \u043f\u043e\u0431\u0435\u0434\u0430 \u043f\u0440\u0438\u0441\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f, \u0435\u0441\u043b\u0438 \u0443 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u0438\u043a\u0430 \u043d\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0441\u0434\u0435\u043b\u0430"
                        "\u0442\u044c \u0445\u043e\u0434</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0438\u0447\u044c\u044f \u043e\u0431\u044a\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u043e \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044e \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0438\u043b\u0438 \u0435\u0441\u043b\u0438 \u0442\u0440\u0438 \u0440\u0430\u0437\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0430 \u0438 \u0442\u0430 \u0436\u0435 \u043f\u043e\u0437\u0438\u0446\u0438\u044f</li></ul>\n"
"<ol start=\"6\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u0430\u0432"
                        "\u0438\u043b\u0430:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0415\u0441\u043b\u0438 \u0435\u0441\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u0432\u0437\u044f\u0442\u0438\u044f, \u0438\u0433\u0440\u043e\u043a \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043b\u044e\u0431\u043e\u0439 \u0438\u0437 \u043d\u0438\u0445</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438 \u0432\u0437\u044f\u0442\u0438\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0448\u0430\u0448\u0435\u043a \u0437\u0430 \u043e\u0434\u0438\u043d \u0445\u043e\u0434 \u043d\u0435\u043b\u044c\u0437\u044f \u043f\u0440"
                        "\u043e\u0445\u043e\u0434\u0438\u0442\u044c \u0434\u0432\u0430\u0436\u0434\u044b \u0447\u0435\u0440\u0435\u0437 \u043e\u0434\u043d\u043e \u0438 \u0442\u043e \u0436\u0435 \u043f\u043e\u043b\u0435</li></ul></body></html>", None))
        self.back_to_game.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u0438\u0433\u0440\u0435", None))
        self.central_widget.setTabText(self.central_widget.indexOf(self.third_central_widget), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.right_widget.setTabText(self.right_widget.indexOf(self.first_widget_right), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"60c", None))
        self.white_in_statistics_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0435", None))
        self.black_in_statistics_label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u044b\u0435", None))
        self.statistics.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0448\u043b\u044b\u0435 \u043f\u0430\u0440\u0442\u0438\u0438", None))
        self.right_widget.setTabText(self.right_widget.indexOf(self.second_widget_right), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u0438\u0439", None))
        self.back_to_report.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u043f\u0430\u0440\u0442\u0438\u0438", None))
        self.right_widget.setTabText(self.right_widget.indexOf(self.third_widget_right), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi


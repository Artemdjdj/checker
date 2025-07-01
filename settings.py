# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 240)
        Dialog.setStyleSheet(u"background-color:rgb(40, 40, 40);\n"
"border:none;\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 180))
        self.tabWidget.setMaximumSize(QSize(300, 180))
        self.tabWidget.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 221, 31))
        self.label.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 60, 231, 31))
        self.comboBox.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"padding:5px;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.comboBox_2 = QComboBox(self.tab_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 60, 231, 31))
        self.comboBox_2.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"padding:5px;")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 221, 31))
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font-size:14px;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 60))
        self.frame.setMaximumSize(QSize(300, 60))
        self.frame.setStyleSheet(u"background-color:rgb(7,7,7);\n"
"border-top:1px solid rgb(102, 255, 99);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:0.5px solid rgb(178, 255, 106);\n"
"color:rgb(255, 255, 255);\n"
"padding:2px;\n"
"border-radius:5px;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border:0.5px solid rgb(178, 255, 106);\n"
"color:rgb(255, 255, 255);\n"
"padding:2px;\n"
"border-radius:5px;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"border:0.5px solid rgb(178, 255, 106);\n"
"color:rgb(255, 255, 255);\n"
"padding:2px;\n"
"border-radius:5px;\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0437\u0432\u0443\u043a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0411\u0435\u0437 \u043c\u0443\u0437\u044b\u043a\u0438", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u043a\u043e\u0439\u043d\u0430\u044f", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u0430\u044f", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u0417\u0432\u0443\u043a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u044f\u044f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u0430\u044f", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


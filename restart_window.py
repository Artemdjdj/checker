# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restart_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QWidget)
import res

class Ui_Dialog_restart(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 600)
        Dialog.setMinimumSize(QSize(650, 600))
        Dialog.setMaximumSize(QSize(650, 600))
        Dialog.setStyleSheet(u"background-color:rgb(47,47,47);")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 480, 501, 102))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 50))
        self.pushButton_2.setMaximumSize(QSize(200, 50))
        self.pushButton_2.setStyleSheet(u"background:rgb(94, 78, 19);\n"
"font-size:20px;\n"
"color:rgb(235, 235, 235);\n"
"border-radius:10px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 50))
        self.pushButton.setMaximumSize(QSize(200, 50))
        self.pushButton.setStyleSheet(u"background:rgb(13, 84, 10);\n"
"font-size:20px;\n"
"color:rgb(235, 235, 235);\n"
"border-radius:10px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 360, 361, 91))
        self.pushButton_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_3.setStyleSheet(u"border:none;\n"
"background-color:none;\n"
"color:rgb(165, 165, 165);\n"
"font-size:36px;\n"
"font-weight:800px;\n"
"text-align:center;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/white_figure_default.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(90, 90))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 650, 340))
        self.pushButton_4.setMinimumSize(QSize(650, 340))
        self.pushButton_4.setMaximumSize(QSize(650, 340))
        self.pushButton_4.setStyleSheet(u"background-color:rgb(47,47,47);\n"
"border:none;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"images/default.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(650, 330))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u043d\u044e", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0438\u0433\u0440\u0430\u043b\u0438 ", None))
        self.pushButton_4.setText("")
    # retranslateUi


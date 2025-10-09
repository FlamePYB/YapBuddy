# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
)
from PySide6.QtGui import (
    QFont,
    QIcon,
)
from PySide6.QtWidgets import (
    QLineEdit,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setWeight(QFont.Thin)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(
            ":/image/files/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.center = QWidget(MainWindow)
        self.center.setObjectName("center")
        self.verticalLayout = QVBoxLayout(self.center)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 50)
        self.MessageArea = QScrollArea(self.center)
        self.MessageArea.setObjectName("MessageArea")
        self.MessageArea.setStyleSheet("")
        self.MessageArea.setWidgetResizable(True)
        self.Messages = QWidget()
        self.Messages.setObjectName("Messages")
        self.Messages.setEnabled(True)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Messages.sizePolicy().hasHeightForWidth())
        self.Messages.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.Messages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 9)
        self.MessageArea.setWidget(self.Messages)

        self.verticalLayout.addWidget(self.MessageArea)

        self.MessageInput = QLineEdit(self.center)
        self.MessageInput.setObjectName("MessageInput")
        self.MessageInput.setMaximumSize(QSize(5000, 70))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setWeight(QFont.Thin)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.MessageInput.setFont(font1)

        self.verticalLayout.addWidget(self.MessageInput)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.center)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("YapBuddy", "YapBuddy", None)
        )
        self.MessageInput.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Start typing over here", None)
        )
        self.MessageInput.setProperty(
            "html",
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:100; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;"><br /></p></body></html>',
                None,
            ),
        )

    # retranslateUi

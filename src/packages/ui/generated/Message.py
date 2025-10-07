# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Message.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QMargins,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Rectangle(object):
    def setupUi(self, Rectangle):
        if not Rectangle.objectName():
            Rectangle.setObjectName(u"Rectangle")
        Rectangle.resize(504, 46)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Rectangle.sizePolicy().hasHeightForWidth())
        Rectangle.setSizePolicy(sizePolicy)
        Rectangle.setMinimumSize(QSize(0, 0))
        Rectangle.setMaximumSize(QSize(16777215, 16777215))
        Rectangle.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Rectangle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(QMargins(4, 4, 9, 4))
        self.MessageContent = QLabel(Rectangle)
        self.MessageContent.setObjectName(u"MessageContent")
        self.MessageContent.setWordWrap(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MessageContent.sizePolicy().hasHeightForWidth())
        self.MessageContent.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.MessageContent.setFont(font)
        self.MessageContent.setLayoutDirection(Qt.LeftToRight)
        self.MessageContent.setStyleSheet(u"background: transparent; border: none;")
        self.MessageContent.setContentsMargins(QMargins(0, 0, 0, 0))

        self.verticalLayout.addWidget(self.MessageContent)


        self.retranslateUi(Rectangle)

        QMetaObject.connectSlotsByName(Rectangle)
    # setupUi

    def retranslateUi(self, Rectangle):
        self.MessageContent.setText("")
        pass
    # retranslateUi


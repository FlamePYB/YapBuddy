# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Message.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Rectangle(object):
    def setupUi(self, Rectangle):
        if not Rectangle.objectName():
            Rectangle.setObjectName(u"Rectangle")
        Rectangle.resize(504, 46)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Rectangle.sizePolicy().hasHeightForWidth())
        Rectangle.setSizePolicy(sizePolicy)
        Rectangle.setMinimumSize(QSize(0, 46))
        Rectangle.setMaximumSize(QSize(504, 16777215))
        Rectangle.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Rectangle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 0, 0, 0)
        self.MessageContent = QLabel(Rectangle)
        self.MessageContent.setObjectName(u"MessageContent")
        self.MessageContent.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.verticalLayout.addWidget(self.MessageContent, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(Rectangle)

        QMetaObject.connectSlotsByName(Rectangle)
    # setupUi

    def retranslateUi(self, Rectangle):
        Rectangle.setWindowTitle(QCoreApplication.translate("Rectangle", u"Form", None))
        self.MessageContent.setText(QCoreApplication.translate("Rectangle", u"text", None))
    # retranslateUi


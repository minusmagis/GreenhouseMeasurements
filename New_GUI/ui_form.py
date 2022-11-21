# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1351, 760)
        MainWindow.setMinimumSize(QSize(0, 5))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(75, 81, 72);")
        self.actionSomtheng = QAction(MainWindow)
        self.actionSomtheng.setObjectName(u"actionSomtheng")
        self.actionSomething_else = QAction(MainWindow)
        self.actionSomething_else.setObjectName(u"actionSomething_else")
        self.actionSomething_Dumb = QAction(MainWindow)
        self.actionSomething_Dumb.setObjectName(u"actionSomething_Dumb")
        self.actionSomething_clever = QAction(MainWindow)
        self.actionSomething_clever.setObjectName(u"actionSomething_clever")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(0, 0, 100, 760))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QSize(100, 0))
        self.verticalFrame.setStyleSheet(u"background-color: rgb(48, 52, 46);")
        self.verticalFrame.setLineWidth(0)
        self.MenuButtonLayout = QVBoxLayout(self.verticalFrame)
        self.MenuButtonLayout.setSpacing(0)
        self.MenuButtonLayout.setObjectName(u"MenuButtonLayout")
        self.MenuButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.LogoFrame = QFrame(self.verticalFrame)
        self.LogoFrame.setObjectName(u"LogoFrame")
        self.LogoFrame.setMinimumSize(QSize(50, 50))
        self.LogoFrame.setFrameShape(QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QFrame.Raised)

        self.MenuButtonLayout.addWidget(self.LogoFrame)

        self.DashboardButton = QPushButton(self.verticalFrame)
        self.DashboardButton.setObjectName(u"DashboardButton")
        self.DashboardButton.setMinimumSize(QSize(100, 100))
        self.DashboardButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/greenohouse_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.DashboardButton.setIcon(icon)
        self.DashboardButton.setIconSize(QSize(65, 65))

        self.MenuButtonLayout.addWidget(self.DashboardButton)

        self.JVCurvesButton = QPushButton(self.verticalFrame)
        self.JVCurvesButton.setObjectName(u"JVCurvesButton")
        self.JVCurvesButton.setMinimumSize(QSize(100, 100))
        self.JVCurvesButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/curves_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.JVCurvesButton.setIcon(icon1)
        self.JVCurvesButton.setIconSize(QSize(60, 60))

        self.MenuButtonLayout.addWidget(self.JVCurvesButton)

        self.HistoricalDataButton = QPushButton(self.verticalFrame)
        self.HistoricalDataButton.setObjectName(u"HistoricalDataButton")
        self.HistoricalDataButton.setMinimumSize(QSize(100, 100))
        self.HistoricalDataButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/historic_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.HistoricalDataButton.setIcon(icon2)
        self.HistoricalDataButton.setIconSize(QSize(65, 65))

        self.MenuButtonLayout.addWidget(self.HistoricalDataButton)

        self.ButtonVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.MenuButtonLayout.addItem(self.ButtonVSpacer)

        self.SettingsButton = QPushButton(self.verticalFrame)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setMinimumSize(QSize(100, 100))
        self.SettingsButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")

        self.MenuButtonLayout.addWidget(self.SettingsButton)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(170, 440, 791, 311))
        self.StringPowerLayout = QGridLayout(self.gridLayoutWidget)
        self.StringPowerLayout.setSpacing(0)
        self.StringPowerLayout.setObjectName(u"StringPowerLayout")
        self.StringPowerLayout.setContentsMargins(0, 0, 0, 0)
        self.PowerBarMetersLayout = QFrame(self.gridLayoutWidget)
        self.PowerBarMetersLayout.setObjectName(u"PowerBarMetersLayout")
        self.PowerBarMetersLayout.setFrameShape(QFrame.StyledPanel)
        self.PowerBarMetersLayout.setFrameShadow(QFrame.Raised)

        self.StringPowerLayout.addWidget(self.PowerBarMetersLayout, 0, 1, 1, 1)

        self.UselessFrame1 = QFrame(self.gridLayoutWidget)
        self.UselessFrame1.setObjectName(u"UselessFrame1")
        self.UselessFrame1.setFrameShape(QFrame.StyledPanel)
        self.UselessFrame1.setFrameShadow(QFrame.Raised)

        self.StringPowerLayout.addWidget(self.UselessFrame1, 1, 0, 1, 1)

        self.StringsXaxisLayout = QHBoxLayout()
        self.StringsXaxisLayout.setSpacing(0)
        self.StringsXaxisLayout.setObjectName(u"StringsXaxisLayout")
        self.String1Label = QLabel(self.gridLayoutWidget)
        self.String1Label.setObjectName(u"String1Label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.String1Label.sizePolicy().hasHeightForWidth())
        self.String1Label.setSizePolicy(sizePolicy1)
        self.String1Label.setMinimumSize(QSize(10, 2))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.String1Label.setFont(font1)
        self.String1Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String1Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String1Label)

        self.String2Label = QLabel(self.gridLayoutWidget)
        self.String2Label.setObjectName(u"String2Label")
        sizePolicy1.setHeightForWidth(self.String2Label.sizePolicy().hasHeightForWidth())
        self.String2Label.setSizePolicy(sizePolicy1)
        self.String2Label.setMinimumSize(QSize(10, 2))
        self.String2Label.setFont(font1)
        self.String2Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String2Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String2Label)

        self.String3Label = QLabel(self.gridLayoutWidget)
        self.String3Label.setObjectName(u"String3Label")
        sizePolicy1.setHeightForWidth(self.String3Label.sizePolicy().hasHeightForWidth())
        self.String3Label.setSizePolicy(sizePolicy1)
        self.String3Label.setMinimumSize(QSize(10, 2))
        self.String3Label.setFont(font1)
        self.String3Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String3Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String3Label)

        self.String4Label = QLabel(self.gridLayoutWidget)
        self.String4Label.setObjectName(u"String4Label")
        sizePolicy1.setHeightForWidth(self.String4Label.sizePolicy().hasHeightForWidth())
        self.String4Label.setSizePolicy(sizePolicy1)
        self.String4Label.setMinimumSize(QSize(10, 2))
        self.String4Label.setFont(font1)
        self.String4Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String4Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String4Label)

        self.StringNumberLabelLayout = QVBoxLayout()
        self.StringNumberLabelLayout.setSpacing(0)
        self.StringNumberLabelLayout.setObjectName(u"StringNumberLabelLayout")
        self.StringNumberString = QLabel(self.gridLayoutWidget)
        self.StringNumberString.setObjectName(u"StringNumberString")
        sizePolicy1.setHeightForWidth(self.StringNumberString.sizePolicy().hasHeightForWidth())
        self.StringNumberString.setSizePolicy(sizePolicy1)
        self.StringNumberString.setMinimumSize(QSize(10, 2))
        self.StringNumberString.setFont(font1)
        self.StringNumberString.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.StringNumberLabelLayout.addWidget(self.StringNumberString)

        self.StringNumberNumber = QLabel(self.gridLayoutWidget)
        self.StringNumberNumber.setObjectName(u"StringNumberNumber")
        sizePolicy1.setHeightForWidth(self.StringNumberNumber.sizePolicy().hasHeightForWidth())
        self.StringNumberNumber.setSizePolicy(sizePolicy1)
        self.StringNumberNumber.setMinimumSize(QSize(10, 2))
        self.StringNumberNumber.setFont(font1)
        self.StringNumberNumber.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.StringNumberLabelLayout.addWidget(self.StringNumberNumber)


        self.StringsXaxisLayout.addLayout(self.StringNumberLabelLayout)

        self.String5Label = QLabel(self.gridLayoutWidget)
        self.String5Label.setObjectName(u"String5Label")
        sizePolicy1.setHeightForWidth(self.String5Label.sizePolicy().hasHeightForWidth())
        self.String5Label.setSizePolicy(sizePolicy1)
        self.String5Label.setMinimumSize(QSize(10, 2))
        self.String5Label.setFont(font1)
        self.String5Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String5Label.setScaledContents(False)
        self.String5Label.setAlignment(Qt.AlignCenter)
        self.String5Label.setWordWrap(True)

        self.StringsXaxisLayout.addWidget(self.String5Label)

        self.String6Label = QLabel(self.gridLayoutWidget)
        self.String6Label.setObjectName(u"String6Label")
        sizePolicy1.setHeightForWidth(self.String6Label.sizePolicy().hasHeightForWidth())
        self.String6Label.setSizePolicy(sizePolicy1)
        self.String6Label.setMinimumSize(QSize(10, 2))
        self.String6Label.setFont(font1)
        self.String6Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String6Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String6Label)

        self.String7Label = QLabel(self.gridLayoutWidget)
        self.String7Label.setObjectName(u"String7Label")
        sizePolicy1.setHeightForWidth(self.String7Label.sizePolicy().hasHeightForWidth())
        self.String7Label.setSizePolicy(sizePolicy1)
        self.String7Label.setMinimumSize(QSize(10, 2))
        self.String7Label.setFont(font1)
        self.String7Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String7Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String7Label)

        self.String8Label = QLabel(self.gridLayoutWidget)
        self.String8Label.setObjectName(u"String8Label")
        sizePolicy1.setHeightForWidth(self.String8Label.sizePolicy().hasHeightForWidth())
        self.String8Label.setSizePolicy(sizePolicy1)
        self.String8Label.setMinimumSize(QSize(10, 2))
        self.String8Label.setFont(font1)
        self.String8Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String8Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String8Label)


        self.StringPowerLayout.addLayout(self.StringsXaxisLayout, 1, 1, 1, 1)

        self.PowerMeterYaxisLayout = QVBoxLayout()
        self.PowerMeterYaxisLayout.setObjectName(u"PowerMeterYaxisLayout")
        self.MaxPowerLabel = QLabel(self.gridLayoutWidget)
        self.MaxPowerLabel.setObjectName(u"MaxPowerLabel")
        self.MaxPowerLabel.setFont(font)
        self.MaxPowerLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.MaxPowerLabel)

        self.PowerWLabel = QLabel(self.gridLayoutWidget)
        self.PowerWLabel.setObjectName(u"PowerWLabel")
        self.PowerWLabel.setFont(font)
        self.PowerWLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.PowerWLabel)

        self.MinPowerLabel = QLabel(self.gridLayoutWidget)
        self.MinPowerLabel.setObjectName(u"MinPowerLabel")
        self.MinPowerLabel.setFont(font1)
        self.MinPowerLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.MinPowerLabel)


        self.StringPowerLayout.addLayout(self.PowerMeterYaxisLayout, 0, 0, 1, 1)

        self.StringPowerLayout.setRowStretch(0, 90)
        self.StringPowerLayout.setRowStretch(1, 10)
        self.StringPowerLayout.setColumnStretch(0, 5)
        self.StringPowerLayout.setColumnStretch(1, 95)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(296, 193, 91, 51))
        self.SunPowerLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.SunPowerLayout.setSpacing(0)
        self.SunPowerLayout.setObjectName(u"SunPowerLayout")
        self.SunPowerLayout.setContentsMargins(0, 0, 0, 0)
        self.SunPowerLabel = QLabel(self.verticalLayoutWidget_3)
        self.SunPowerLabel.setObjectName(u"SunPowerLabel")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel.setSizePolicy(sizePolicy1)
        self.SunPowerLabel.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel.setFont(font)
        self.SunPowerLabel.setStyleSheet(u"  color: rgb(254, 249, 193);\n"
"background: transparent;")
        self.SunPowerLabel.setAlignment(Qt.AlignCenter)
        self.SunPowerLabel.setWordWrap(True)

        self.SunPowerLayout.addWidget(self.SunPowerLabel)

        self.SunPowerUnitsLabel = QLabel(self.verticalLayoutWidget_3)
        self.SunPowerUnitsLabel.setObjectName(u"SunPowerUnitsLabel")
        sizePolicy1.setHeightForWidth(self.SunPowerUnitsLabel.sizePolicy().hasHeightForWidth())
        self.SunPowerUnitsLabel.setSizePolicy(sizePolicy1)
        self.SunPowerUnitsLabel.setMinimumSize(QSize(10, 2))
        self.SunPowerUnitsLabel.setFont(font)
        self.SunPowerUnitsLabel.setStyleSheet(u"  color: rgb(254, 249, 193);\n"
"background: transparent;")
        self.SunPowerUnitsLabel.setWordWrap(True)

        self.SunPowerLayout.addWidget(self.SunPowerUnitsLabel)

        self.HistoricEnergyGraphFrame = QFrame(self.centralwidget)
        self.HistoricEnergyGraphFrame.setObjectName(u"HistoricEnergyGraphFrame")
        self.HistoricEnergyGraphFrame.setGeometry(QRect(970, 470, 341, 231))
        self.HistoricEnergyGraphFrame.setFrameShape(QFrame.StyledPanel)
        self.HistoricEnergyGraphFrame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(590, 80, 721, 271))
        self.EnergyDashboardLayout = QGridLayout(self.layoutWidget)
        self.EnergyDashboardLayout.setObjectName(u"EnergyDashboardLayout")
        self.EnergyDashboardLayout.setVerticalSpacing(30)
        self.EnergyDashboardLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SunPowerLabel_2 = QLabel(self.layoutWidget)
        self.SunPowerLabel_2.setObjectName(u"SunPowerLabel_2")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_2.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_2.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_2.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_2.setFont(font)
        self.SunPowerLabel_2.setStyleSheet(u"  color: rgb(255, 200, 136);")
        self.SunPowerLabel_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.SunPowerLabel_2)

        self.SunPowerLabel_3 = QLabel(self.layoutWidget)
        self.SunPowerLabel_3.setObjectName(u"SunPowerLabel_3")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_3.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_3.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_3.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_3.setFont(font)
        self.SunPowerLabel_3.setStyleSheet(u"  color: rgb(255, 152, 30);")
        self.SunPowerLabel_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.SunPowerLabel_3)


        self.EnergyDashboardLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SunPowerLabel_4 = QLabel(self.layoutWidget)
        self.SunPowerLabel_4.setObjectName(u"SunPowerLabel_4")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_4.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_4.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_4.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_4.setFont(font)
        self.SunPowerLabel_4.setStyleSheet(u"  color: rgb(231, 255, 158);")
        self.SunPowerLabel_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.SunPowerLabel_4)

        self.SunPowerLabel_5 = QLabel(self.layoutWidget)
        self.SunPowerLabel_5.setObjectName(u"SunPowerLabel_5")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_5.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_5.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_5.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_5.setFont(font)
        self.SunPowerLabel_5.setStyleSheet(u"  color: rgb(195, 255, 17);")
        self.SunPowerLabel_5.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.SunPowerLabel_5)


        self.EnergyDashboardLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SunPowerLabel_8 = QLabel(self.layoutWidget)
        self.SunPowerLabel_8.setObjectName(u"SunPowerLabel_8")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_8.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_8.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_8.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_8.setFont(font)
        self.SunPowerLabel_8.setStyleSheet(u"  color: rgb(190, 255, 236);")
        self.SunPowerLabel_8.setWordWrap(True)

        self.horizontalLayout.addWidget(self.SunPowerLabel_8)

        self.SunPowerLabel_6 = QLabel(self.layoutWidget)
        self.SunPowerLabel_6.setObjectName(u"SunPowerLabel_6")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_6.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_6.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_6.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_6.setFont(font)
        self.SunPowerLabel_6.setStyleSheet(u"  color: rgb(13, 255, 180);")
        self.SunPowerLabel_6.setWordWrap(True)

        self.horizontalLayout.addWidget(self.SunPowerLabel_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.SunPowerLabel_7 = QLabel(self.layoutWidget)
        self.SunPowerLabel_7.setObjectName(u"SunPowerLabel_7")
        sizePolicy1.setHeightForWidth(self.SunPowerLabel_7.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_7.setSizePolicy(sizePolicy1)
        self.SunPowerLabel_7.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_7.setFont(font)
        self.SunPowerLabel_7.setStyleSheet(u"  color:rgb(190, 255, 236);")
        self.SunPowerLabel_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.SunPowerLabel_7)


        self.EnergyDashboardLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 60, 311, 311))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.verticalFrame.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.HistoricEnergyGraphFrame.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSomtheng.setText(QCoreApplication.translate("MainWindow", u"Somtheng", None))
        self.actionSomething_else.setText(QCoreApplication.translate("MainWindow", u"Something else", None))
        self.actionSomething_Dumb.setText(QCoreApplication.translate("MainWindow", u"Something Dumb", None))
        self.actionSomething_clever.setText(QCoreApplication.translate("MainWindow", u"Something clever", None))
        self.DashboardButton.setText("")
        self.JVCurvesButton.setText("")
        self.HistoricalDataButton.setText("")
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.String1Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">1</span></p></body></html>", None))
        self.String2Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">2</span></p></body></html>", None))
        self.String3Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">3</span></p></body></html>", None))
        self.String4Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">4</span></p></body></html>", None))
        self.StringNumberString.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">String</span></p></body></html>", None))
        self.StringNumberNumber.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Number</span></p></body></html>", None))
        self.String5Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">5</span></p></body></html>", None))
        self.String6Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">6</span></p></body></html>", None))
        self.String7Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">7</span></p></body></html>", None))
        self.String8Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">8</span></p></body></html>", None))
        self.MaxPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.PowerWLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Power (W)</span></p></body></html>", None))
        self.MinPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">0</span></p></body></html>", None))
        self.SunPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">864</span></p></body></html>", None))
        self.SunPowerUnitsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">W m</span><span style=\" font-size:11pt; vertical-align:super;\">-2</span></p></body></html>", None))
        self.SunPowerLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Current Solar Power</span></p></body></html>", None))
        self.SunPowerLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:60pt;\">1251 W</span></p></body></html>", None))
        self.SunPowerLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Today's Solar Energy</span></p></body></html>", None))
        self.SunPowerLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:60pt;\">2547 kWh</span></p></body></html>", None))
        self.SunPowerLabel_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:25pt;\">Generated</span></p></body></html>", None))
        self.SunPowerLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:60pt;\">15%</span></p></body></html>", None))
        self.SunPowerLabel_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">of today's greenhouse energy needs</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img width=\"300\" height=\"300\" src=\":/icons/sun_full_png\"/></p></body></html>", None))
    # retranslateUi


import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import threading

Not_Sorted = []
Sorted = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.num = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 30, 1001, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.selection_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.selection_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.selection_time.setTextFormat(QtCore.Qt.AutoText)
        self.selection_time.setScaledContents(True)
        self.selection_time.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_time.setObjectName("selection_time")
        self.gridLayout_2.addWidget(self.selection_time, 3, 2, 1, 1)

        self.bingo_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bingo_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bingo_time.setTextFormat(QtCore.Qt.AutoText)
        self.bingo_time.setScaledContents(True)
        self.bingo_time.setAlignment(QtCore.Qt.AlignCenter)
        self.bingo_time.setObjectName("bingo_time")
        self.gridLayout_2.addWidget(self.bingo_time, 11, 2, 1, 1)

        self.random_numbers = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.random_numbers.sizePolicy().hasHeightForWidth())
        self.random_numbers.setSizePolicy(sizePolicy)
        self.random_numbers.setObjectName("random_numbers")
        self.gridLayout_2.addWidget(self.random_numbers, 0, 1, 1, 1)

        self.bubble_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bubble_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bubble_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.bubble_sorted.setScaledContents(True)
        self.bubble_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.bubble_sorted.setObjectName("bubble_sorted")
        self.gridLayout_2.addWidget(self.bubble_sorted, 4, 1, 1, 1)

        self.quick_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.quick_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.quick_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.quick_sorted.setScaledContents(True)
        self.quick_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.quick_sorted.setObjectName("quick_sorted")
        self.gridLayout_2.addWidget(self.quick_sorted, 7, 1, 1, 1)

        self.insertion_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.insertion_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.insertion_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.insertion_sorted.setScaledContents(True)
        self.insertion_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.insertion_sorted.setObjectName("insertion_sorted")
        self.gridLayout_2.addWidget(self.insertion_sorted, 5, 1, 1, 1)

        self.merge_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.merge_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.merge_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.merge_sorted.setScaledContents(True)
        self.merge_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.merge_sorted.setObjectName("merge_sorted")
        self.gridLayout_2.addWidget(self.merge_sorted, 6, 1, 1, 1)

        self.heap_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.heap_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.heap_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.heap_sorted.setScaledContents(True)
        self.heap_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.heap_sorted.setObjectName("heap_sorted")
        self.gridLayout_2.addWidget(self.heap_sorted, 8, 1, 1, 1)

        self.radix_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.radix_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.radix_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.radix_sorted.setScaledContents(True)
        self.radix_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.radix_sorted.setObjectName("radix_sorted")
        self.gridLayout_2.addWidget(self.radix_sorted, 10, 1, 1, 1)

        self.counting_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.counting_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.counting_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.counting_sorted.setScaledContents(True)
        self.counting_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.counting_sorted.setObjectName("counting_sorted")
        self.gridLayout_2.addWidget(self.counting_sorted, 9, 1, 1, 1)

        self.bingo_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bingo_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bingo_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.bingo_sorted.setScaledContents(True)
        self.bingo_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.bingo_sorted.setObjectName("bingo_sorted")
        self.gridLayout_2.addWidget(self.bingo_sorted, 11, 1, 1, 1)

        self.cycle_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cycle_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cycle_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.cycle_sorted.setScaledContents(True)
        self.cycle_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.cycle_sorted.setObjectName("cycle_sorted")
        self.gridLayout_2.addWidget(self.cycle_sorted, 15, 1, 1, 1)

        self.comb_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.comb_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.comb_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.comb_sorted.setScaledContents(True)
        self.comb_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.comb_sorted.setObjectName("comb_sorted")
        self.gridLayout_2.addWidget(self.comb_sorted, 13, 1, 1, 1)

        self.pigeonhole_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pigeonhole_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pigeonhole_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.pigeonhole_sorted.setScaledContents(True)
        self.pigeonhole_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.pigeonhole_sorted.setObjectName("pigeonhole_sorted")
        self.gridLayout_2.addWidget(self.pigeonhole_sorted, 14, 1, 1, 1)

        self.shell_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.shell_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.shell_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.shell_sorted.setScaledContents(True)
        self.shell_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.shell_sorted.setObjectName("shell_sorted")
        self.gridLayout_2.addWidget(self.shell_sorted, 12, 1, 1, 1)

        self.strand_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.strand_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.strand_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.strand_sorted.setScaledContents(True)
        self.strand_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.strand_sorted.setObjectName("strand_sorted")
        self.gridLayout_2.addWidget(self.strand_sorted, 16, 1, 1, 1)

        self.pancake_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pancake_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pancake_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.pancake_sorted.setScaledContents(True)
        self.pancake_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.pancake_sorted.setObjectName("pancake_sorted")
        self.gridLayout_2.addWidget(self.pancake_sorted, 17, 1, 1, 1)

        self.gnome_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gnome_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.gnome_time.setTextFormat(QtCore.Qt.AutoText)
        self.gnome_time.setScaledContents(True)
        self.gnome_time.setAlignment(QtCore.Qt.AlignCenter)
        self.gnome_time.setObjectName("gnome_time")
        self.gridLayout_2.addWidget(self.gnome_time, 18, 2, 1, 1)

        self.gnome_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gnome_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.gnome_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.gnome_sorted.setScaledContents(True)
        self.gnome_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.gnome_sorted.setObjectName("gnome_sorted")
        self.gridLayout_2.addWidget(self.gnome_sorted, 18, 1, 1, 1)

        self.pancake_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pancake_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pancake_time.setTextFormat(QtCore.Qt.AutoText)
        self.pancake_time.setScaledContents(True)
        self.pancake_time.setAlignment(QtCore.Qt.AlignCenter)
        self.pancake_time.setObjectName("pancake_time")
        self.gridLayout_2.addWidget(self.pancake_time, 17, 2, 1, 1)

        self.strand_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.strand_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.strand_time.setTextFormat(QtCore.Qt.AutoText)
        self.strand_time.setScaledContents(True)
        self.strand_time.setAlignment(QtCore.Qt.AlignCenter)
        self.strand_time.setObjectName("strand_time")
        self.gridLayout_2.addWidget(self.strand_time, 16, 2, 1, 1)

        self.pigeonhole_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pigeonhole_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pigeonhole_time.setTextFormat(QtCore.Qt.AutoText)
        self.pigeonhole_time.setScaledContents(True)
        self.pigeonhole_time.setAlignment(QtCore.Qt.AlignCenter)
        self.pigeonhole_time.setObjectName("pigeonhole_time")
        self.gridLayout_2.addWidget(self.pigeonhole_time, 14, 2, 1, 1)

        self.comb_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.comb_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.comb_time.setTextFormat(QtCore.Qt.AutoText)
        self.comb_time.setScaledContents(True)
        self.comb_time.setAlignment(QtCore.Qt.AlignCenter)
        self.comb_time.setObjectName("comb_time")
        self.gridLayout_2.addWidget(self.comb_time, 13, 2, 1, 1)

        self.cycle_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cycle_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cycle_time.setTextFormat(QtCore.Qt.AutoText)
        self.cycle_time.setScaledContents(True)
        self.cycle_time.setAlignment(QtCore.Qt.AlignCenter)
        self.cycle_time.setObjectName("cycle_time")
        self.gridLayout_2.addWidget(self.cycle_time, 15, 2, 1, 1)

        self.shell_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.shell_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.shell_time.setTextFormat(QtCore.Qt.AutoText)
        self.shell_time.setScaledContents(True)
        self.shell_time.setAlignment(QtCore.Qt.AlignCenter)
        self.shell_time.setObjectName("shell_time")
        self.gridLayout_2.addWidget(self.shell_time, 12, 2, 1, 1)

        self.user_entered_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_entered_num.sizePolicy().hasHeightForWidth())
        self.user_entered_num.setSizePolicy(sizePolicy)
        self.user_entered_num.setObjectName("user_entered_num")
        self.gridLayout_2.addWidget(self.user_entered_num, 1, 1, 1, 1)

        self.counting_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.counting_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.counting_time.setTextFormat(QtCore.Qt.AutoText)
        self.counting_time.setScaledContents(True)
        self.counting_time.setAlignment(QtCore.Qt.AlignCenter)
        self.counting_time.setObjectName("counting_time")
        self.gridLayout_2.addWidget(self.counting_time, 9, 2, 1, 1)

        self.cycle_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cycle_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cycle_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.cycle_sort_label.setScaledContents(True)
        self.cycle_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cycle_sort_label.setObjectName("cycle_sort_label")
        self.gridLayout_2.addWidget(self.cycle_sort_label, 15, 0, 1, 1)

        self.comb_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.comb_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.comb_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.comb_sort_label.setScaledContents(True)
        self.comb_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.comb_sort_label.setObjectName("comb_sort_label")
        self.gridLayout_2.addWidget(self.comb_sort_label, 13, 0, 1, 1)

        self.pigeonhole_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pigeonhole_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pigeonhole_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.pigeonhole_sort_label.setScaledContents(True)
        self.pigeonhole_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pigeonhole_sort_label.setObjectName("pigeonhole_sort_label")
        self.gridLayout_2.addWidget(self.pigeonhole_sort_label, 14, 0, 1, 1)

        self.strand_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.strand_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.strand_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.strand_sort_label.setScaledContents(True)
        self.strand_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.strand_sort_label.setObjectName("strand_sort_label")
        self.gridLayout_2.addWidget(self.strand_sort_label, 16, 0, 1, 1)

        self.pancake_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pancake_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pancake_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.pancake_sort_label.setScaledContents(True)
        self.pancake_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pancake_sort_label.setObjectName("pancake_sort_label")
        self.gridLayout_2.addWidget(self.pancake_sort_label, 17, 0, 1, 1)

        self.selection_sorted = QtWidgets.QLabel(self.gridLayoutWidget)
        self.selection_sorted.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.selection_sorted.setTextFormat(QtCore.Qt.AutoText)
        self.selection_sorted.setScaledContents(True)
        self.selection_sorted.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_sorted.setObjectName("selection_sorted")
        self.gridLayout_2.addWidget(self.selection_sorted, 3, 1, 1, 1)

        self.insertion_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.insertion_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.insertion_time.setTextFormat(QtCore.Qt.AutoText)
        self.insertion_time.setScaledContents(True)
        self.insertion_time.setAlignment(QtCore.Qt.AlignCenter)
        self.insertion_time.setObjectName("insertion_time")
        self.gridLayout_2.addWidget(self.insertion_time, 5, 2, 1, 1)

        self.heap_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.heap_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.heap_time.setTextFormat(QtCore.Qt.AutoText)
        self.heap_time.setScaledContents(True)
        self.heap_time.setAlignment(QtCore.Qt.AlignCenter)
        self.heap_time.setObjectName("heap_time")
        self.gridLayout_2.addWidget(self.heap_time, 8, 2, 1, 1)

        self.merge_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.merge_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.merge_time.setTextFormat(QtCore.Qt.AutoText)
        self.merge_time.setScaledContents(True)
        self.merge_time.setAlignment(QtCore.Qt.AlignCenter)
        self.merge_time.setObjectName("merge_time")
        self.gridLayout_2.addWidget(self.merge_time, 6, 2, 1, 1)

        self.gnome_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gnome_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.gnome_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.gnome_sort_label.setScaledContents(True)
        self.gnome_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gnome_sort_label.setObjectName("gnome_sort_label")
        self.gridLayout_2.addWidget(self.gnome_sort_label, 18, 0, 1, 1)

        self.quick_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.quick_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.quick_time.setTextFormat(QtCore.Qt.AutoText)
        self.quick_time.setScaledContents(True)
        self.quick_time.setAlignment(QtCore.Qt.AlignCenter)
        self.quick_time.setObjectName("quick_time")
        self.gridLayout_2.addWidget(self.quick_time, 7, 2, 1, 1)

        self.bubble_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bubble_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bubble_time.setTextFormat(QtCore.Qt.AutoText)
        self.bubble_time.setScaledContents(True)
        self.bubble_time.setAlignment(QtCore.Qt.AlignCenter)
        self.bubble_time.setObjectName("bubble_time")
        self.gridLayout_2.addWidget(self.bubble_time, 4, 2, 1, 1)

        self.random_numbers_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.random_numbers_button.setObjectName("random_numbers_button")
        self.gridLayout_2.addWidget(self.random_numbers_button, 0, 2, 1, 1)

        self.random_number_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.random_number_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.random_number_label.setTextFormat(QtCore.Qt.AutoText)
        self.random_number_label.setScaledContents(True)
        self.random_number_label.setAlignment(QtCore.Qt.AlignCenter)
        self.random_number_label.setObjectName("random_number_label")
        self.gridLayout_2.addWidget(self.random_number_label, 0, 0, 1, 1)

        self.user_entered_numbers_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.user_entered_numbers_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.user_entered_numbers_label.setTextFormat(QtCore.Qt.AutoText)
        self.user_entered_numbers_label.setScaledContents(True)
        self.user_entered_numbers_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_entered_numbers_label.setObjectName("user_entered_numbers_label")
        self.gridLayout_2.addWidget(self.user_entered_numbers_label, 1, 0, 1, 1)

        self.user_entered_numbers_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.user_entered_numbers_button.setObjectName("user_entered_numbers_button")
        self.gridLayout_2.addWidget(self.user_entered_numbers_button, 1, 2, 1, 1)

        self.insertion_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.insertion_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.insertion_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.insertion_sort_label.setScaledContents(True)
        self.insertion_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.insertion_sort_label.setObjectName("insertion_sort_label")
        self.gridLayout_2.addWidget(self.insertion_sort_label, 5, 0, 1, 1)

        self.merge_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.merge_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.merge_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.merge_sort_label.setScaledContents(True)
        self.merge_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.merge_sort_label.setObjectName("merge_sort_label")
        self.gridLayout_2.addWidget(self.merge_sort_label, 6, 0, 1, 1)

        self.selection_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.selection_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.selection_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.selection_sort_label.setScaledContents(True)
        self.selection_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_sort_label.setObjectName("selection_sort_label")
        self.gridLayout_2.addWidget(self.selection_sort_label, 3, 0, 1, 1)

        self.bubble_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bubble_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bubble_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.bubble_sort_label.setScaledContents(True)
        self.bubble_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bubble_sort_label.setObjectName("bubble_sort_label")
        self.gridLayout_2.addWidget(self.bubble_sort_label, 4, 0, 1, 1)

        self.quick_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.quick_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.quick_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.quick_sort_label.setScaledContents(True)
        self.quick_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.quick_sort_label.setObjectName("quick_sort_label")
        self.gridLayout_2.addWidget(self.quick_sort_label, 7, 0, 1, 1)

        self.heap_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.heap_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.heap_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.heap_sort_label.setScaledContents(True)
        self.heap_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heap_sort_label.setObjectName("heap_sort_label")
        self.gridLayout_2.addWidget(self.heap_sort_label, 8, 0, 1, 1)

        self.counting_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.counting_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.counting_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.counting_sort_label.setScaledContents(True)
        self.counting_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.counting_sort_label.setObjectName("counting_sort_label")
        self.gridLayout_2.addWidget(self.counting_sort_label, 9, 0, 1, 1)

        self.radix_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.radix_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.radix_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.radix_sort_label.setScaledContents(True)
        self.radix_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.radix_sort_label.setObjectName("radix_sort_label")
        self.gridLayout_2.addWidget(self.radix_sort_label, 10, 0, 1, 1)

        self.shell_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.shell_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.shell_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.shell_sort_label.setScaledContents(True)
        self.shell_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shell_sort_label.setObjectName("shell_sort_label")
        self.gridLayout_2.addWidget(self.shell_sort_label, 12, 0, 1, 1)

        self.bingo_sort_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bingo_sort_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bingo_sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.bingo_sort_label.setScaledContents(True)
        self.bingo_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bingo_sort_label.setObjectName("bingo_sort_label")
        self.gridLayout_2.addWidget(self.bingo_sort_label, 11, 0, 1, 1)

        self.radix_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.radix_time.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.radix_time.setTextFormat(QtCore.Qt.AutoText)
        self.radix_time.setScaledContents(True)
        self.radix_time.setAlignment(QtCore.Qt.AlignCenter)
        self.radix_time.setObjectName("radix_time")
        self.gridLayout_2.addWidget(self.radix_time, 10, 2, 1, 1)

        self.not_sorted_numbers = QtWidgets.QLabel(self.gridLayoutWidget)
        self.not_sorted_numbers.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.not_sorted_numbers.setTextFormat(QtCore.Qt.AutoText)
        self.not_sorted_numbers.setScaledContents(True)
        self.not_sorted_numbers.setAlignment(QtCore.Qt.AlignCenter)
        self.not_sorted_numbers.setObjectName("not_sorted_numbers")
        self.gridLayout_2.addWidget(self.not_sorted_numbers, 2, 1, 1, 1)

        self.not_sorted_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.not_sorted_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.not_sorted_label.setTextFormat(QtCore.Qt.AutoText)
        self.not_sorted_label.setScaledContents(True)
        self.not_sorted_label.setAlignment(QtCore.Qt.AlignCenter)
        self.not_sorted_label.setObjectName("not_sorted_label")
        self.gridLayout_2.addWidget(self.not_sorted_label, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selection_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.bingo_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.bubble_sorted.setText(_translate("MainWindow", "0"))
        self.quick_sorted.setText(_translate("MainWindow", "0"))
        self.insertion_sorted.setText(_translate("MainWindow", "0"))
        self.merge_sorted.setText(_translate("MainWindow", "0"))
        self.heap_sorted.setText(_translate("MainWindow", "0"))
        self.radix_sorted.setText(_translate("MainWindow", "0"))
        self.counting_sorted.setText(_translate("MainWindow", "0"))
        self.bingo_sorted.setText(_translate("MainWindow", "0"))
        self.cycle_sorted.setText(_translate("MainWindow", "0"))
        self.comb_sorted.setText(_translate("MainWindow", "0"))
        self.pigeonhole_sorted.setText(_translate("MainWindow", "0"))
        self.shell_sorted.setText(_translate("MainWindow", "0"))
        self.strand_sorted.setText(_translate("MainWindow", "0"))
        self.pancake_sorted.setText(_translate("MainWindow", "0"))
        self.gnome_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.gnome_sorted.setText(_translate("MainWindow", "0"))
        self.pancake_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.strand_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.pigeonhole_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.comb_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.cycle_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.shell_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.counting_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.cycle_sort_label.setText(_translate("MainWindow", "Cycle Sort"))
        self.comb_sort_label.setText(_translate("MainWindow", "Comb Sort"))
        self.pigeonhole_sort_label.setText(_translate("MainWindow", "Pigeonhole Sort"))
        self.strand_sort_label.setText(_translate("MainWindow", "Strand Sort"))
        self.pancake_sort_label.setText(_translate("MainWindow", "Pancake Sort"))
        self.selection_sorted.setText(_translate("MainWindow", "0"))
        self.insertion_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.heap_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.merge_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.gnome_sort_label.setText(_translate("MainWindow", "Gnome Sort"))
        self.quick_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.bubble_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.random_numbers_button.setText(_translate("MainWindow", "Generate"))
        self.random_number_label.setText(_translate("MainWindow", "Enter a number for how many  will be generate"))
        self.user_entered_numbers_label.setText(_translate("MainWindow", "Enter your numbers using comma "))
        self.user_entered_numbers_button.setText(_translate("MainWindow", "Run"))
        self.insertion_sort_label.setText(_translate("MainWindow", "Insertion Sort"))
        self.merge_sort_label.setText(_translate("MainWindow", "Merge Sort"))
        self.selection_sort_label.setText(_translate("MainWindow", "Selection Sort"))
        self.bubble_sort_label.setText(_translate("MainWindow", "Bubble Sort"))
        self.quick_sort_label.setText(_translate("MainWindow", "Quick Sort"))
        self.heap_sort_label.setText(_translate("MainWindow", "Heap Sort"))
        self.counting_sort_label.setText(_translate("MainWindow", "Counting Sort"))
        self.radix_sort_label.setText(_translate("MainWindow", "Radix Sort"))
        self.shell_sort_label.setText(_translate("MainWindow", "Shell Sort"))
        self.bingo_sort_label.setText(_translate("MainWindow", "Bingo Sort"))
        self.radix_time.setText(_translate("MainWindow", "Time Elapsed:"))
        self.not_sorted_numbers.setText(_translate("MainWindow", "0"))
        self.not_sorted_label.setText(_translate("MainWindow", "Not Sorted number list"))

        self.random_numbers.textChanged.connect(lambda: self.getValue())
        self.user_entered_num.textChanged.connect(lambda: self.create_list())
        self.random_numbers_button.clicked.connect(lambda: RandomButton(self.num, self.not_sorted_numbers))
        self.user_entered_numbers_button.clicked.connect(lambda: threads(self))

    def getValue(self):
       self.num = self.random_numbers.text()

    def create_list(self):
        global Not_Sorted
        global Sorted
        text = self.not_sorted_numbers.text()
        Not_Sorted = text.split(",")
        Sorted = Not_Sorted

def threads(self):
    t1 = threading.Thread(target=SelectionSort, args=(self.selection_sorted, self.selection_time))
    t2 = threading.Thread(target=BubbleSort, args=(self.bubble_sorted, self.bubble_time))
    t3 = threading.Thread(target=InsertionSort, args=(self.insertion_sorted, self.insertion_time))
    t4 = threading.Thread(target=MergeSort, args=(self.merge_sorted, self.merge_time))
    t5 = threading.Thread(target=QuickSort, args=(self.quick_sorted, self.quick_time))
    t6 = threading.Thread(target=HeapSort, args=(self.heap_sorted, self.heap_time))
    t7 = threading.Thread(target=CountingSort, args=(self.counting_sorted, self.counting_time))
    t8 = threading.Thread(target=RadixSort, args=(self.radix_sorted, self.radix_time))
    t9 = threading.Thread(target=BingoSort, args=(self.bingo_sorted, self.bingo_time))
    t10 = threading.Thread(target=ShellSort, args=(self.shell_sorted, self.shell_time))
    t11 = threading.Thread(target=CombSort, args=(self.comb_sorted, self.comb_time))
    t12 = threading.Thread(target=PigeonholeSort, args=(self.pigeonhole_sorted, self.pigeonhole_time))
    t13 = threading.Thread(target=CycleSort, args=(self.cycle_sorted, self.cycle_time))
    t14 = threading.Thread(target=StrandSort, args=(self.strand_sorted, self.strand_time))
    t15 = threading.Thread(target=PancakeSort, args=(self.pancake_sorted, self.pancake_time))
    t16 = threading.Thread(target=GnomeSort, args=(self.gnome_sorted, self.gnome_time))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

def List_To_String(text):
    txt = ""
    for i in text:
        if txt == "":
            txt = str(i)
        else:
            txt = txt + ", " + str(i)
    return txt
def SelectionSort(sorted_numbers, time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    temp = 0
    for i in range(len(Sorted)):
        smallest = 120
        for j in range(len(Not_Sorted)):
            if (i + j) < len(Not_Sorted):
                if Sorted[j + i] < smallest:
                    smallest = Sorted[j+i]
                    temp = j + i

        temp1 = Sorted[i]
        Sorted[i] = Sorted[temp]
        Sorted[temp] = temp1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def BubbleSort(sorted_numbers,time_label):
    start = time.process_time()
    counti = 0
    for i in Not_Sorted:
        countj = 0
        for j in Not_Sorted:
            if j > i and i != j:
                temp = Sorted[countj]
                Sorted[countj] = Sorted[counti]
                Sorted[counti] = temp
            countj += 1
        counti += 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def InsertionSort(sorted_numbers,time_label):
    start = time.process_time()
    for i in range(len(Not_Sorted)):
        if i < len(Not_Sorted)-1:
            j = 1
            if Not_Sorted[i] > Not_Sorted[i+1]:
                temp = Not_Sorted[i+1]
                Not_Sorted[i+1] = Not_Sorted[i]
                Not_Sorted[i] = temp
            while i-j >= 0:
                if Not_Sorted[i] < Not_Sorted[i-j]:
                    temp = Not_Sorted[i-j]
                    Not_Sorted[i-j] = Not_Sorted[i]
                    Not_Sorted[i] = temp
                    j += 1
                else:
                    break

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def MergeSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    merge_sort(Not_Sorted)

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def merge_sort(arr):
    if len(arr) > 1:
        div = len(arr)//2
        L = arr[:div]
        R = arr[div:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def partition(temp, low, high):
    pivot = temp[high]
    i = low - 1
    for j in range(low, high):
        if Sorted[j] <= pivot:
            i = i + 1
            (temp[i], temp[j]) = (temp[j], temp[i])
    (temp[i + 1], temp[high]) = (temp[high], temp[i + 1])
    return i + 1

def quickSort(temp,low, high):
    if low < high:
        pi = partition(temp, low, high)
        quickSort(temp, low, pi - 1)
        quickSort(temp, pi + 1, high)

def QuickSort(sorted_numbers,time_label):
    start = time.process_time()
    temp = Not_Sorted
    low = 0
    high = len(temp) - 1
    quickSort(temp, low, high)

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < N and arr[largest] < arr[l]:
        largest = l
    if r < N and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)
def HeapSort(sorted_numbers, time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    N = len(Not_Sorted)
    for i in range(N // 2 - 1, -1, -1):
        heapify(Not_Sorted, N, i)
    for i in range(N - 1, 0, -1):
        Not_Sorted[i], Not_Sorted[0] = Not_Sorted[0], Not_Sorted[i]  # swap
        heapify(Not_Sorted, i, 0)

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def CountingSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    Maximun = max(Not_Sorted)

    count_array = [0] * (Maximun + 1)

    # Mapping each element of input_array as an index of count_array
    for num in Not_Sorted:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, Maximun + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    Sorted = [0] * len(Not_Sorted)

    for i in range(len(Not_Sorted) - 1, -1, -1):
        Sorted[count_array[Not_Sorted[i]] - 1] = Not_Sorted[i]
        count_array[Not_Sorted[i]] -= 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def RadixSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted

    max1 = max(Not_Sorted)
    exp = 1
    while max1 / exp >= 1:
        radixCountSort(Not_Sorted, exp)
        exp *= 10

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def radixCountSort(Not_Sorted, exp1):
    n = len(Not_Sorted)
    Inv_Sorted = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = Not_Sorted[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = Not_Sorted[i] // exp1
        Inv_Sorted[count[index % 10] - 1] = Not_Sorted[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(Not_Sorted)):
        Sorted[i] = Inv_Sorted[i]

def BingoSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted

    length= len(Sorted)
    bingo = min(Sorted)
    largest = max(Sorted)
    nextBingo = largest
    nextPos = 0
    while bingo < nextBingo:
        startPos = nextPos
        for i in range(startPos, length):
            if Sorted[i] == bingo:
                Sorted[i], Sorted[nextPos] = Sorted[nextPos], Sorted[i]
                nextPos += 1
            elif Sorted[i] < nextBingo:
                nextBingo = Sorted[i]
        bingo = nextBingo
        nextBingo = largest

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def ShellSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    length = len(Sorted)
    gap = length // 2
    while gap > 0:
        j = gap
        while j < length:
            i = j - gap
            while i >= 0:
                if Sorted[i + gap] > Sorted[i]:
                    break
                else:
                    Sorted[i + gap], Sorted[i] = Sorted[i], Sorted[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap
def CombSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    length = len(Sorted)
    gap = length
    swapped = True
    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, length - gap):
            if Sorted[i] > Sorted[i + gap]:
                Sorted[i], Sorted[i + gap] = Sorted[i + gap], Sorted[i]
                swapped = True

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def PigeonholeSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted

    my_min = min(Sorted)
    my_max = max(Sorted)
    size = my_max - my_min + 1
    holes = [0] * size
    for i in Sorted:
        assert type(i) is int, "integers only please"
        holes[i - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            Sorted[i] = count + my_min
            i += 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def CycleSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    writes = 0

    for cycleStart in range(0, len(Sorted) - 1):
        item = Sorted[cycleStart]
        pos = cycleStart

        for i in range(cycleStart + 1, len(Sorted)):
            if Sorted[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while item == Sorted[pos]:
            pos += 1
        Sorted[pos], item = item, Sorted[pos]
        writes += 1

        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(Sorted)):
                if Sorted[i] < item:
                    pos += 1
            while item == Sorted[pos]:
                pos += 1
            Sorted[pos], item = item, Sorted[pos]
            writes += 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def strand_sort(temp):
    # Define a helper function to merge two sorted lists
    def merge_lists(list1, list2):
        result = []
        while list1 and list2:
            if list1[0] < list2[0]:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
        result += list1
        result += list2
        return result
    if len(temp) <= 1:
        return temp
    sublist = [temp.pop(0)]

    i = 0
    while i < len(temp):
        if temp[i] > sublist[-1]:
            sublist.append(temp.pop(i))
        else:
            i += 1
    sorted_sublist = sublist
    remaining_list = strand_sort(temp)
    return merge_lists(sorted_sublist, remaining_list)

def StrandSort(sorted_numbers,time_label):
    start = time.process_time()

    Sorted = strand_sort(Not_Sorted)

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def PancakeSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    current_size = len(Sorted)
    def findMax(Sorted, curr_size):
        mi = 0
        for i in range(0, curr_size):
            if Sorted[i] > Sorted[mi]:
                mi = i
        return mi

    def flip(Sorted, i):
        begining = 0
        while begining < i:
            temp = Sorted[begining]
            Sorted[begining] = Sorted[i]
            Sorted[i] = temp
            begining += 1
            i -= 1

    while current_size > 1:
        mi = findMax(Sorted, current_size)
        if mi != current_size - 1:
            flip(Sorted, mi)
            flip(Sorted, current_size - 1)
        current_size -= 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def GnomeSort(sorted_numbers,time_label):
    start = time.process_time()
    Sorted = Not_Sorted
    length = len(Sorted)

    index = 0
    while index < length:
        if index == 0:
            index = index + 1
        if Sorted[index] >= Sorted[index - 1]:
            index = index + 1
        else:
            Sorted[index], Sorted[index - 1] = Sorted[index - 1], Sorted[index]
            index = index - 1

    sorted_numbers.setText(List_To_String(Sorted))
    time_label.setText("Time Elapsed: " + str(start))

def RandomButton(num, not_sorted_num):
    global Sorted
    global Not_Sorted
    count = 0
    while count < int(num):
        Not_Sorted.append(random.randint(1, 100))
        count += 1
    Sorted = Not_Sorted
    txt =""
    for i in Not_Sorted:
        txt = txt + str(i) + ","
    not_sorted_num.setText(txt)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

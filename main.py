import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets

Not_Sorted = []
Sorted = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.num = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(966, 0))
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 761, 704))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.SelectionSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.SelectionSort.setObjectName("SelectionSort")
        self.verticalLayout_3.addWidget(self.SelectionSort)

        self.BubbleSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BubbleSort.setObjectName("BubbleSort")
        self.verticalLayout_3.addWidget(self.BubbleSort)

        self.InsertionSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.InsertionSort.setObjectName("InsertionSort")
        self.verticalLayout_3.addWidget(self.InsertionSort)

        self.MergeSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.MergeSort.setObjectName("MergeSort")
        self.verticalLayout_3.addWidget(self.MergeSort)

        self.QuickSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.QuickSort.setObjectName("QuickSort")
        self.verticalLayout_3.addWidget(self.QuickSort)

        self.HeapSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.HeapSort.setObjectName("HeapSort")
        self.verticalLayout_3.addWidget(self.HeapSort)

        self.CountingSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.CountingSort.setObjectName("CountingSort")
        self.verticalLayout_3.addWidget(self.CountingSort)

        self.RadixSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.RadixSort.setObjectName("RadixSort")
        self.verticalLayout_3.addWidget(self.RadixSort)

        self.BucketSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BucketSort.setObjectName("BucketSort")
        self.verticalLayout_3.addWidget(self.BucketSort)

        self.BingoSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BingoSort.setObjectName("BingoSort")
        self.verticalLayout_3.addWidget(self.BingoSort)

        self.ShellSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ShellSort.setObjectName("ShellSort")
        self.verticalLayout_3.addWidget(self.ShellSort)

        self.TimSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.TimSort.setObjectName("TimSort")
        self.verticalLayout_3.addWidget(self.TimSort)

        self.CombSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.CombSort.setObjectName("CombSort")
        self.verticalLayout_3.addWidget(self.CombSort)

        self.PigeonholeSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PigeonholeSort.setObjectName("PigeonholeSort")
        self.verticalLayout_3.addWidget(self.PigeonholeSort)

        self.CycleSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.CycleSort.setObjectName("CycleSort")
        self.verticalLayout_3.addWidget(self.CycleSort)

        self.StrandSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.StrandSort.setObjectName("StrandSort")
        self.verticalLayout_3.addWidget(self.StrandSort)

        self.PancakeSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PancakeSort.setObjectName("PancakeSort")
        self.verticalLayout_3.addWidget(self.PancakeSort)

        self.GnomeSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.GnomeSort.setObjectName("GnomeSort")
        self.verticalLayout_3.addWidget(self.GnomeSort)

        self.TreeSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.TreeSort.setObjectName("TreeSort")
        self.verticalLayout_3.addWidget(self.TreeSort)

        self.PermutationSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PermutationSort.setObjectName("PermutationSort")
        self.verticalLayout_3.addWidget(self.PermutationSort)

        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.RandomButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.RandomButton.setObjectName("RandomButton")
        self.gridLayout.addWidget(self.RandomButton, 0, 1, 1, 1)

        self.sorted_numbers = QtWidgets.QLabel(self.formLayoutWidget)
        self.sorted_numbers.setObjectName("sorted_numbers")
        self.gridLayout.addWidget(self.sorted_numbers, 2, 1, 1, 1)

        self.SizeOfNumber = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SizeOfNumber.setObjectName("how many number in the list")
        self.gridLayout.addWidget(self.SizeOfNumber, 0, 0, 1, 1)

        self.not_sorted_numbers = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.gridLayout.addWidget(self.not_sorted_numbers, 2, 0, 1, 1)

        self.not_sorted_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.not_sorted_label.setObjectName("not_sorted_label")
        self.gridLayout.addWidget(self.not_sorted_label, 1, 0, 1, 1)

        self.sorted_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.sorted_label.setObjectName("sorted_label")
        self.gridLayout.addWidget(self.sorted_label, 1, 1, 1, 1)

        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global Not_Sorted
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectionSort.setText(_translate("MainWindow", "Selection Sort"))
        self.BubbleSort.setText(_translate("MainWindow", "Bubble Sort"))
        self.InsertionSort.setText(_translate("MainWindow", "Insertion Sort"))
        self.MergeSort.setText(_translate("MainWindow", "Merge Sort"))
        self.QuickSort.setText(_translate("MainWindow", "Quick Sort"))
        self.HeapSort.setText(_translate("MainWindow", "Heap Sort"))
        self.CountingSort.setText(_translate("MainWindow", "Counting Sort"))
        self.RadixSort.setText(_translate("MainWindow", "Radix Sort"))
        self.BucketSort.setText(_translate("MainWindow", "Bucket Sort"))
        self.BingoSort.setText(_translate("MainWindow", "Bingo Sort"))
        self.ShellSort.setText(_translate("MainWindow", "Shell Sort"))
        self.TimSort.setText(_translate("MainWindow", "Tim Sort"))
        self.CombSort.setText(_translate("MainWindow", "Comb Sort"))
        self.PigeonholeSort.setText(_translate("MainWindow", "Pigeonhole Sort"))
        self.CycleSort.setText(_translate("MainWindow", "Cycle Sort"))
        self.StrandSort.setText(_translate("MainWindow", "Strand Sort"))
        self.PancakeSort.setText(_translate("MainWindow", "Pancake Sort"))
        self.GnomeSort.setText(_translate("MainWindow", "Gnome Sort"))
        self.TreeSort.setText(_translate("MainWindow", "Tree Sort"))
        self.PermutationSort.setText(_translate("MainWindow", "Permutation Sort"))

        self.SelectionSort.clicked.connect(lambda: SelectionSort(self.sorted_numbers))
        self.BubbleSort.clicked.connect(lambda: BubbleSort(self.sorted_numbers))
        self.InsertionSort.clicked.connect(lambda: InsertionSort(self.sorted_numbers))
        self.MergeSort.clicked.connect(lambda: MergeSort(self.sorted_numbers))
        self.QuickSort.clicked.connect(lambda: QuickSort(self.sorted_numbers))
        self.HeapSort.clicked.connect(lambda: HeapSort(self.sorted_numbers))
        self.CountingSort.clicked.connect(lambda: CountingSort(self.sorted_numbers))
        self.RadixSort.clicked.connect(lambda: RadixSort)
        self.BucketSort.clicked.connect(lambda: BucketSort)
        self.BingoSort.clicked.connect(lambda: BingoSort)
        self.ShellSort.clicked.connect(lambda: ShellSort)
        self.TimSort.clicked.connect(lambda: TimSort)
        self.CombSort.clicked.connect(lambda: CombSort)
        self.PigeonholeSort.clicked.connect(lambda: PancakeSort)
        self.CycleSort.clicked.connect(lambda: CycleSort)
        self.StrandSort.clicked.connect(lambda: StrandSort)
        self.PancakeSort.clicked.connect(lambda: PancakeSort)
        self.TreeSort.clicked.connect(lambda: TreeSort)
        self.GnomeSort.clicked.connect(lambda: GnomeSort)
        self.PermutationSort.clicked.connect(lambda: PermutationSort)

        self.sorted_numbers.setText(_translate("MainWindow", "TextLabel"))
        self.not_sorted_label.setText(_translate("MainWindow", "Enter your numbers using comma in between"))
        self.sorted_label.setText(_translate("MainWindow", "Numbers are ordered min to max are below"))
        self.RandomButton.setText(_translate("MainWindow", "Randomly select"))
        self.SizeOfNumber.textChanged.connect(lambda: self.getValue())
        self.not_sorted_numbers.textChanged.connect((lambda: self.create_list()))
        self.RandomButton.clicked.connect(lambda: RandomButton(self.num))

    def getValue(self):
       self.num = self.SizeOfNumber.text()

    def create_list(self):
        global Not_Sorted
        global Sorted
        text = self.not_sorted_numbers.text()
        Not_Sorted = text.split(",")
        Sorted = Not_Sorted

def List_To_String(text):
    txt = ""
    for i in text:
        if txt == "":
            txt = str(i)
        else:
            txt = txt + ", " + str(i)
    return txt
def SelectionSort(sorted_numbers):
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
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def BubbleSort(sorted_numbers):
    start = time.process_time()
    counti = 0
    print(Sorted)
    for i in Not_Sorted:
        countj = 0
        for j in Not_Sorted:
            if j > i and i != j:
                temp = Sorted[countj]
                Sorted[countj] = Sorted[counti]
                Sorted[counti] = temp
            countj += 1
        counti += 1
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def InsertionSort(sorted_numbers):
    start = time.process_time()
    for i in range(len(Not_Sorted)):
        if i < len(Not_Sorted)-1:
            j = 1
            if Not_Sorted[i] > Not_Sorted[i+1]:
                temp = Not_Sorted[i+1]
                Not_Sorted[i+1] = Not_Sorted[i]
                Not_Sorted[i] = temp
            while i-j >= 0:
                print(Not_Sorted)
                if Not_Sorted[i] < Not_Sorted[i-j]:
                    temp = Not_Sorted[i-j]
                    Not_Sorted[i-j] = Not_Sorted[i]
                    Not_Sorted[i] = temp
                    j += 1
                else:
                    break
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def MergeSort(sorted_numbers):
    start = time.process_time()
    Sorted = Not_Sorted
    merge_sort(Not_Sorted)
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

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

def QuickSort(sorted_numbers):
    start = time.process_time()
    temp = Not_Sorted
    low = 0
    high = len(temp) - 1
    quickSort(temp, low, high)
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(temp)}<br/>{clock}</html>")

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
def HeapSort(sorted_numbers):
    start = time.process_time()
    Sorted = Not_Sorted
    N = len(Not_Sorted)
    for i in range(N // 2 - 1, -1, -1):
        heapify(Not_Sorted, N, i)
    for i in range(N - 1, 0, -1):
        Not_Sorted[i], Not_Sorted[0] = Not_Sorted[0], Not_Sorted[i]  # swap
        heapify(Not_Sorted, i, 0)
    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def CountingSort(sorted_numbers):
    start = time.process_time()
    Sorted = Not_Sorted
    M = max(Not_Sorted)

    # Initializing count_array with 0
    count_array = [0] * (M + 1)

    # Mapping each element of input_array as an index of count_array
    for num in Not_Sorted:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    Sorted = [0] * len(Not_Sorted)

    for i in range(len(Not_Sorted) - 1, -1, -1):
        Sorted[count_array[Not_Sorted[i]] - 1] = Not_Sorted[i]
        count_array[Not_Sorted[i]] -= 1

    end = time.process_time()
    clock = "time passed: " + str(end - start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def RadixSort():
    print("8")

def BucketSort():
    print("9")

def BingoSort():
    print("10")

def ShellSort():
    print("11")

def TimSort():
    print("12")

def CombSort():
    print("13")

def PigeonholeSort():
    print("14")

def CycleSort():
    print("15")

def StrandSort():
    print("16")

def PancakeSort():
    print("17")

def GnomeSort():
    print("18")

def TreeSort():
    print("19")

def PermutationSort():
    print("20")


def RandomButton(num):
    global Sorted
    global Not_Sorted
    count = 0
    while count < int(num):
        Not_Sorted.append(random.randint(1, 100))
        count += 1
    Sorted = Not_Sorted

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

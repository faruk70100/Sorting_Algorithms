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

        self.BingoSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BingoSort.setObjectName("BingoSort")
        self.verticalLayout_3.addWidget(self.BingoSort)

        self.ShellSort = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ShellSort.setObjectName("ShellSort")
        self.verticalLayout_3.addWidget(self.ShellSort)

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
        self.BingoSort.setText(_translate("MainWindow", "Bingo Sort"))
        self.ShellSort.setText(_translate("MainWindow", "Shell Sort"))
        self.CombSort.setText(_translate("MainWindow", "Comb Sort"))
        self.PigeonholeSort.setText(_translate("MainWindow", "Pigeonhole Sort"))
        self.CycleSort.setText(_translate("MainWindow", "Cycle Sort"))
        self.StrandSort.setText(_translate("MainWindow", "Strand Sort"))
        self.PancakeSort.setText(_translate("MainWindow", "Pancake Sort"))
        self.GnomeSort.setText(_translate("MainWindow", "Gnome Sort"))

        self.SelectionSort.clicked.connect(lambda: SelectionSort(self.sorted_numbers))
        self.BubbleSort.clicked.connect(lambda: BubbleSort(self.sorted_numbers))
        self.InsertionSort.clicked.connect(lambda: InsertionSort(self.sorted_numbers))
        self.MergeSort.clicked.connect(lambda: MergeSort(self.sorted_numbers))
        self.QuickSort.clicked.connect(lambda: QuickSort(self.sorted_numbers))
        self.HeapSort.clicked.connect(lambda: HeapSort(self.sorted_numbers))
        self.CountingSort.clicked.connect(lambda: CountingSort(self.sorted_numbers))
        self.RadixSort.clicked.connect(lambda: RadixSort(self.sorted_numbers))
        self.BingoSort.clicked.connect(lambda: BingoSort(self.sorted_numbers))
        self.ShellSort.clicked.connect(lambda: ShellSort(self.sorted_numbers))
        self.CombSort.clicked.connect(lambda: CombSort(self.sorted_numbers))
        self.PigeonholeSort.clicked.connect(lambda: PigeonholeSort(self.sorted_numbers))
        self.CycleSort.clicked.connect(lambda: CycleSort(self.sorted_numbers))
        self.StrandSort.clicked.connect(lambda: StrandSort(self.sorted_numbers))
        self.PancakeSort.clicked.connect(lambda: PancakeSort(self.sorted_numbers))
        self.GnomeSort.clicked.connect(lambda: GnomeSort(self.sorted_numbers))

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

    clock = "time passed: " + str(start)
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

    clock = "time passed: " + str(start)
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def MergeSort(sorted_numbers):
    start = time.process_time()
    Sorted = Not_Sorted
    merge_sort(Not_Sorted)

    clock = "time passed: " + str(start)
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

    clock = "time passed: " + str(start)
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def CountingSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def RadixSort(sorted_numbers):
    start = time.process_time()
    Sorted = Not_Sorted

    max1 = max(Not_Sorted)
    exp = 1
    while max1 / exp >= 1:
        radixCountSort(Not_Sorted, exp)
        exp *= 10

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

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

def BingoSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def ShellSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap
def CombSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def PigeonholeSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def CycleSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")


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

def StrandSort(sorted_numbers):
    start = time.process_time()

    Sorted = strand_sort(Not_Sorted)

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def PancakeSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

def GnomeSort(sorted_numbers):
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

    clock = "time passed: " + str(start)
    sorted_numbers.setText(f"<html>{List_To_String(Sorted)}<br/>{clock}</html>")

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

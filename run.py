import os
import sys
from collections import defaultdict

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsPixmapItem
from PyQt5.QtCore import pyqtSignal, QStringListModel, Qt

from ui.ma import Ui_MainWindow
from cs_widgets.qci import QClickableImage
from utils.toyolo import get_xml


class MyMainWindow(QMainWindow, Ui_MainWindow):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setupUi(self)
        self.init_slot()

        self.desktop = QApplication.desktop()
        self.width = 240
        self.height = 300

        # 设置图片的预览尺寸；
        self.displayed_image_size = 80
        self.col = 0
        self.row = 0

        self.max_columns = self.get_nr_of_image_columns()  # 窗口能放的图像的列数

        self.initial_path = None

        self.label_qci = defaultdict(list)  # key 标签 value qci
        self.all_qci = defaultdict(list)  # key qci value 标签列表

        self.all_xml = set(os.listdir('./res/Annotations'))
        self.all_img = os.listdir('./res/JPEGImages')
        self.img_no_xml = [img for img in self.all_img if img.split('.')[0]+'.xml' not in self.all_xml]
        pass

    def init_slot(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.btn_choose.clicked.connect(self.slot_btn_chooseDir)
        self.btn_confirm.clicked.connect(self.item_show)
        self.btn_start.clicked.connect(self.get_img_xml)

    # Slot Func
    def get_img_xml(self):
        while self.img_no_xml:
            name = self.img_no_xml.pop()
            print(get_xml("./res/JPEGImages/" + name))

    def item_show(self):
        for qci in self.all_qci.keys():
            qci.show()

        selected_label = {i.data() for i in self.labelShow.selectionModel().selectedIndexes()}  # 选中的临时删掉

        for qci in self.all_qci.keys():
            if set(self.all_qci[qci]) & (selected_label):
                qci.hide()

    def keyPressEvent(self, event):
        """
        键盘按键事件
        :param event:
        :return:
        """
        self.helpSignal.emit("help message")
        if event.key() == Qt.Key_A:
            self.col = 1
            self.row = 0
            self.helpSignal.emit("修改col row")

    # 显示帮助消息
    def showHelpMessage(self, message):
        self.statusbar.showMessage(message)

    def slot_btn_chooseDir(self):
        file_path = QFileDialog.getExistingDirectory(self, '选择文文件夹', 'F:\Code\Python\photoAlbum')
        if file_path == None:
            QMessageBox.information(self, '提示', '文件为空，请重新操作')
        else:
            self.initial_path = file_path  # self.initial_path用来存放图片所在的文件夹
            self.showDir.setText(file_path)

        self.start_img_viewer()

    # Others
    def get_nr_of_image_columns(self):
        # 展示图片的区域，计算每排显示图片数。返回的列数-1是因为我不想频率拖动左右滚动条，影响数据筛选效率
        scroll_area_images_width = self.width
        if scroll_area_images_width > self.displayed_image_size:
            pic_of_columns = scroll_area_images_width // self.displayed_image_size  # 计算出一行几列；
        else:
            pic_of_columns = 1
        return pic_of_columns

    def next_loc(self):
        if self.col < self.max_columns - 1:
            self.col = self.col + 1
        else:
            self.col = 0
            self.row += 1

    def update_list(self):
        """
        update QListView labelShow item
        :return:
        """
        listModel = QStringListModel()
        listModel.setStringList(self.label_qci.keys())
        self.labelShow.setModel(listModel)

    def addImage(self, img_id):
        nr_of_widgets = self.gridLayout.count()  # 当前布局内的数量

        print('行数为{}'.format(self.row))
        print('列数为{}'.format(self.col))
        print('此时布局内含有的元素数为{}'.format(nr_of_widgets))

        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, self.initial_path,
                                          img_id)
        self.gridLayout.addWidget(clickable_image, self.row, self.col)

        labels = clickable_image.get_label()

        self.all_qci[clickable_image] = list(labels)

        for l in labels:
            self.label_qci[l].append(clickable_image)

        self.update_list()

        self.next_loc()

    def start_img_viewer(self):
        if not self.initial_path:
            QMessageBox.warning(self, '错误', '请设置系统根目录')
            return
        img_dir_path = os.path.join(self.initial_path, './JPEGImages', )
        annotation_path = os.path.join(self.initial_path, './Annotations')
        print('img_dir_path为{}'.format(img_dir_path))
        img_type = {'png', 'jpg'}

        img_list = list(i for i in os.listdir(img_dir_path) if i.split(".")[1] in img_type)
        annotation_list = set(list(i.split(".")[0] for i in os.listdir(annotation_path)))
        num = len(img_list)
        if num == 0:
            QMessageBox.warning(self, '错误', '图片为空')

        for i in range(num):
            img_id = str(img_list[i])
            print(img_id)
            if img_id.split(".")[0] not in annotation_list:
                continue

            self.addImage(img_id)
            QApplication.processEvents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())

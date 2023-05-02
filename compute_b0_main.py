import os

import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMessageBox, QFileDialog
)

import sys
from compute_b0 import Ui_ComputeB0
import create_jpg


class MyComputerB0(Ui_ComputeB0, QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # 使用父类 Ui_ExcelSpliter 中的 setupUi 函数
        self.show()  # 展示窗口

        self.bin_path = ""
        self.output_dir = ""
        self.det_temperature_row = 0
        self.b0_row = 0
        self.temp_start = 0
        self.temp_end = 0

        if os.path.exists('./config.xlsx'):
            df = pd.read_excel('./config.xlsx')
            self.det_temperature_row = str(df.loc[0, 'det_temperature_row'])
            self.b0_row = str(df.loc[0, 'b0_row'])
            self.temp_start = str(df.loc[0, 'temp_start'])
            self.temp_end = str(df.loc[0, 'temp_end'])

            self.lineEdit_det.setText(self.det_temperature_row)
            self.lineEdit_b0.setText(self.b0_row)
            self.lineEdit_temp_start.setText(self.temp_start)
            self.lineEdit_temp_end.setText(self.temp_end)

        self.pushButton_choose_bin.clicked.connect(
            self.do_choose_bin
        )

        self.pushButton_choose_output_dir.clicked.connect(
            self.do_choose_save_path
        )

        self.pushButton_do_deal.clicked.connect(
            self.do_deal,
            # self.do_write_excel
        )

    def do_choose_bin(self):
        self.bin_path, filetype = QFileDialog.getOpenFileName(
            self, "请选择要处理的 bin 文件 (excel)", os.getcwd(), "Excel files (*.xlsx)"
        )
        self.lineEdit_bin_path.setText(self.bin_path)

    def do_choose_save_path(self):
        self.output_dir = QFileDialog.getExistingDirectory(
            self, "请选择输出目录", os.getcwd()
        )
        self.lineEdit_output_dir.setText(self.output_dir)

    def do_deal(self):
        if not os.path.exists(self.bin_path):
            QMessageBox.warning(self, "信息提示", "请先选择要处理的 bin 文件")
            return

        self.det_temperature_row = int(self.lineEdit_det.text())
        self.b0_row = int(self.lineEdit_b0.text())
        self.temp_start = self.lineEdit_temp_start.text().upper()
        self.temp_end = self.lineEdit_temp_end.text().upper()

        if self.det_temperature_row == 0:
            QMessageBox.warning(self, "信息提示", "请先输入 det 温度行")
            return
        if self.b0_row == 0:
            QMessageBox.warning(self, "信息提示", "请先输入 b0 行")
            return
        if self.temp_start == 0:
            QMessageBox.warning(self, "信息提示", "请先输入 Temp 起始行")
            return
        if self.temp_end == 0:
            QMessageBox.warning(self, "信息提示", "请先输入 Temp 结束行")
            return

        print('output_dir', self.output_dir)

        if not os.path.exists(self.output_dir):
            QMessageBox.warning(self, "信息提示", "请先选择要存储的图片路径")
            return

        create_jpg.create_jpg(self.bin_path, self.output_dir, self.det_temperature_row, self.b0_row, self.temp_start, self.temp_end)

        # 把本次处理中用到的行列记录入 config.xlsx 文件
        data = {
            'det_temperature_row': self.det_temperature_row,
            'b0_row': self.b0_row,
            'temp_start': self.temp_start,
            'temp_end': self.temp_end
        }
        df = pd.DataFrame(data, index=[1])
        df.to_excel('./config.xlsx', index=False)

        QMessageBox.information(self, "信息提示", "处理成功！")

    # def do_write_excel(self):
    #     df = pd.read_excel('config.xlsx')
    #     df['det_temperature_row'] = self.det_temperature_row
    #     df['b0_row'] = self.b0_row
    #     df['temp_start'] = self.temp_start
    #     df['temp_end'] = self.temp_end


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 一个程序本身一定有个入口，创建 QApplication 来启动 Dialog 窗口

    myComputerB0 = MyComputerB0()

    sys.exit(app.exec())

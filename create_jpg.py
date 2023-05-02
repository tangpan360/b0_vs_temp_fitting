import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import openpyxl


def create_jpg(bin_path, output_dir, det_temperature_row, b0_row, temp_start, temp_end):
    # 从页面获取文件路径
    bin_path = bin_path
    data = pd.ExcelFile(bin_path)
    sheet_names = data.sheet_names

    # 从页面获取 B0 行和 Temp 的起始行列
    det_temperature_row = det_temperature_row
    b0_row = b0_row

    temp_letter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11}  # 建立字母：数字映射字典
    temp_start = temp_letter[f'{temp_start}']  # 温度起始处字母转换为数字
    temp_end = temp_letter[f'{temp_end}']  # 温度结束处字母转换为数字

    print('temp_end', temp_end - temp_start)

    temp_start = temp_start - 1
    temp_end = temp_end - 1

    # 从文件位置通过切分方式获取文件名，用于存储计算出来的 r2.
    file_name_part = bin_path.split('/')[-1].split('.')[0]

    # 存放3、4、5次 r2 的列表
    list_sheet_names = []
    list3 = []
    list4 = []
    list5 = []

    # 循环处理文件中的每个 sheet
    for sheet_name in sheet_names:
        df = pd.read_excel(bin_path, sheet_name=sheet_name)  # 循环读取文件中的每个sheet

        # 读取n个 det_temperature 值
        det_temperature = np.array(df.iloc[det_temperature_row - 2, temp_start: temp_end + 1], dtype=np.float32)

        # 读取n个 B0 值
        b0 = np.array(df.iloc[b0_row - 2, temp_start: temp_end + 1], dtype=np.float32)

        num_temp = len(det_temperature)

        # print(det_temperature)
        # print(b0)

        # 画图前的设置
        plt.figure(figsize=(13, 8))
        plt.rcParams['font.sans-serif'] = 'SimHei'  # 字体黑体

        # 画出5个温度点的折线图
        plt.scatter(det_temperature, b0, label=f'{num_temp}个温度点')
        plt.plot(det_temperature, b0, label=f'{num_temp}个温度点的折线')

        # 拟合3次函数，求方程和R2
        # 拟合3次函数
        coef_3 = np.polyfit(det_temperature, b0, 3)  # 利用 det_temperature 拟合3次函数
        # 求3次多项式公式
        poly_fit_3 = np.poly1d(coef_3)  # 3次多项式公式
        # 利用拟合3次函数求得 B0
        b0_coef_3 = np.polyval(coef_3, det_temperature)
        # 3次函数 R2
        R2_coef_3 = r2_score(b0, b0_coef_3)
        # 画拟合的3次函数曲线
        x3 = np.arange(det_temperature[0], det_temperature[-1])
        y_fit3 = np.polyval(coef_3, x3)
        plt.plot(x3, y_fit3, label=f'3次函数拟合 B0 曲线, \n3次多项式：\n{poly_fit_3}, \nR2：{R2_coef_3}')
        print("三阶多项式为：", poly_fit_3)
        print('coef_3', coef_3)
        print('y_fit3', y_fit3)

        ##  拟合4次函数，求方程和R2
        # 拟合4次函数
        coef_4 = np.polyfit(det_temperature, b0, 4)  # 利用 det_temperature 拟合4次函数
        # 求4次多项式公式
        poly_fit_4 = np.poly1d(coef_4)  # 4次多项式公式
        # 利用拟合4次函数求得 B0
        b0_coef_4 = np.polyval(coef_4, det_temperature)
        # 4次函数 R2
        R2_coef_4 = r2_score(b0, b0_coef_4)
        # 画拟合的4次函数曲线
        x4 = np.arange(det_temperature[0], det_temperature[-1])
        y_fit4 = np.polyval(coef_4, x4)
        plt.plot(x4, y_fit4, label=f'4次函数拟合 B0 曲线, \n4次多项式：\n{poly_fit_4}, \nR2：{R2_coef_4}')

        ##  拟合5次函数，求方程和R2
        # 拟合5次函数
        coef_5 = np.polyfit(det_temperature, b0, 5)  # 利用 det_temperature 拟合5次函数
        # 求5次多项式公式
        poly_fit_5 = np.poly1d(coef_5)  # 5次多项式公式
        # 利用拟合5次函数求得 B0
        b0_coef_5 = np.polyval(coef_5, det_temperature)
        # 5次函数 R2
        R2_coef_5 = r2_score(b0, b0_coef_5)
        # 画拟合的5次函数曲线
        x5 = np.arange(det_temperature[0], det_temperature[-1])
        y_fit5 = np.polyval(coef_5, x5)
        plt.plot(x5, y_fit5, label=f'5次函数拟合 B0 曲线, \n5次多项式：\n{poly_fit_5}, \nR2：{R2_coef_5}')

        plt.title(f"{sheet_name} 的 B0 vs. Temp 曲线", fontsize=20)  # 标题
        plt.xlabel('Temp (x 0.01k)')
        plt.ylabel('B0')
        plt.grid()  # 生成网格

        plt.legend()
        print(output_dir)
        plt.savefig(f"{output_dir}/{sheet_name}_B0.png", dpi=600, format='png')
        plt.show()

        # 依次将每次的3、4、5次 r2 追加到列表中。
        list_sheet_names.append(sheet_name)
        list3.append(R2_coef_3)
        list4.append(R2_coef_4)
        list5.append(R2_coef_5)

    # 将3、4、5次函数的 r2 输入文件中
    df_r2 = pd.DataFrame()
    df_r2['sheet_name'] = list_sheet_names
    df_r2['3'] = list3
    df_r2['4'] = list4
    df_r2['5'] = list5
    print(df_r2)

    df_r2.to_excel(f'{file_name_part}_R_square.xlsx', index=False)


if __name__ == '__main__':
    det_temperature_row = 131
    b0_row = 173
    bin_path= '../data/0301-2023-02-27 17-14-20 DAQ.xlsx'
    temp_start = 'C'
    temp_end = 'G'
    output_dir = './jpg/'
    create_jpg(bin_path, output_dir, det_temperature_row, b0_row, temp_start, temp_end)

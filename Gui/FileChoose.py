import easygui as gui
import os
import Operator.pdfOperator


def searchFile():
    msg = '请选择pdf文件'
    title = ' '
    default = ''
    # fileType='全部文件'
    filePath = gui.fileopenbox(msg, title, default, '所有文件')
    if filePath is None:
        return
    print(filePath)
    # 此处根据实际情况,进行字符编码设计
    filename = filePath.split('/')[-1]
    print(filename)
    Type = filename[-3:]
    print(Type)
    if Type != 'pdf':
        retry = gui.ccbox(msg='不是pdf格式文件', title='错误', choices=('重新选择', '放弃'))
        if retry == 0:
            return
        searchFile()
    else:
        # 是pdf格式的文件
        pdf = Operator.pdfOperator(filePath)


if __name__ == "__main__":
    searchFile()

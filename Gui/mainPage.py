import easygui as gui

from Gui import FileChoose


def start_page():
    keep_on = gui.ccbox(msg='程序开始运行', title='reference识别', choices=('选择文件', '放弃'), image=None)
    if keep_on:
        FileChoose.searchFile()
    else:
        return


if __name__ == "__main__":
    start_page()

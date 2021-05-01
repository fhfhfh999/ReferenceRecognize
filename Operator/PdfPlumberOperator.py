import pdfplumber
from Operator.DocumentOperator import document
import math


# path = 'D:\code\python\ReferenceRecognize\Publist－Chen.pdf'

def pdf_operate(path):
    sentences = judge(read_pdf(path))
    d = document
    d.seperate_sentences(d, sentences=sentences)


def read_pdf(path):
    pdf = pdfplumber.open(path)

    text = ""
    for page in pdf.pages:
        # 获取当前页面的全部文本信息，包括表格中的文字
        # print(page.extract_text())
        text = text + page.extract_text()

    pdf.close()
    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace('“', '')
    text = text.replace('”', '')
    # text = text.replace('\n', '').replace('\r', '')
    # print(text)
    return text


def judge(text):
    if text.find("1.") != -1 & text.find("2.") != -1 & text.find("3.") != -1:
        return point_seperate(text)
    if text.find("[1]") != -1 & text.find("[2]") != -1 & text.find("[3]") != -1:
        return brackets_seperated(text)


def point_seperate(text):
    i = 1
    sep = "1."
    start = text.find(sep)
    sentences = []
    while True:
        if start != -1:
            start += 1 + len(str(i))
        else:
            break
        i = i + 1
        sep = '\n' + str(i) + ". "
        end = text.find(sep)
        if end != -1:
            sen = text[start:end].strip()
            sentences.append(sen.replace('\n', '').replace('\r', ''))
            end += 1
        else:
            sentences.append(text[start:])
        start = end
    # print(sentences)
    # print(sentences[140])
    return sentences


def brackets_seperated(text):
    i = 1
    sep = "[1]"
    start = text.find(sep)
    sentences = []
    while True:
        if start != -1:
            start += 2 + len(str(i))
        else:
            break
        i = i + 1
        sep = "[" + str(i) + "]"
        end = text.find(sep)
        if end != -1:
            sen = text[start:end].strip()
            sentences.append(sen)
        else:
            sentences.append(text[start:])
        start = end
    # print(sentences)
    return sentences


if __name__ == "__main__":
    path = "D:\code\python\ReferenceRecognize\Publist－Chen.pdf"
    # sentence = read_pdf("D:\code\python\ReferenceRecognize\Publist－Chen.pdf")
    # sentences = judge(sentence)
    #
    # print(sentences)

    pdf_operate(path)

from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfparser import PDFParser, PDFDocument

class pdfOperator:

    def __init__(self, name):
        # 获取文档对象
        fp = open(name, "rb")

        # 创建一个与文档关联的解释器
        parser = PDFParser(fp)

        # PDf文档的对象
        doc = PDFDocument()

        # 链接解释器和文档对象
        parser.set_document(doc)
        doc.set_parser(parser)

        # 初始化文档
        doc.initialize("")

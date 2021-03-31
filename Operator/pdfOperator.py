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

        # 创建PDF资源管理器
        resource = PDFResourceManager()

        # 参数分析器
        laparam = LAParams()

        # 创建一个聚合器
        device = PDFPageAggregator(resource, laparams=laparam)

        # 创建PDF页面解释器
        interpreter = PDFPageInterpreter(resource, device)

        # 使用文档对象得到页面的集合
        for page in doc.get_pages():
            # 使用页面解释器来读取
            interpreter.process_page(page)

            # 使用聚合器来获得内容
            layout = device.get_result()

            for out in layout:
                if hasattr(out, 'get_text'):  # 需要注意的是在PDF文档中不只有 text 还可能有图片等等，为了确保不出错先判断对象是否具有 get_text()方法
                    print(out.get_text())

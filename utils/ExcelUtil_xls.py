import os
import xlrd

"""
xlrd说明：
    只能写xls文件
"""


# 自定义异常
class SheetTypeError:
    pass


"""
步骤：
1. 验证文件是否存在，存在读取，不存在报错
2. 读取sheet方式    【名称/索引】
3. 读取sheet内容
4. 返回结果
"""


class ExcelReader():
    def __init__(self, filepath, sheet_by):
        if os.path.exists(filepath):
            self.filepath = filepath
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("Excel文件不存在")

    def data(self):
        workbook = xlrd.open_workbook(self.filepath)
        if type(self.sheet_by) not in [str, int]:
            raise SheetTypeError("请输入int或str")
        elif type(self.sheet_by) == int:
            sheet = workbook.sheet_by_index(self.sheet_by)
        elif type(self.sheet_by) == str:
            sheet = workbook.sheet_by_name(self.sheet_by)

        # 读取sheet内容,组合数据，格式：[{"title1":"value1", "title2":"value2"},{"title1":"value3", "title2":"value4"} ]
        title = sheet.row_values(0)
        for row in range(1, sheet.nrows):
            row_value = sheet.row_values(row)
            self._data.append(dict(zip(title, row_value)))
        return self._data


if __name__ == '__main__':
    data = ExcelReader("../data/test_data.xlsx", "帖子").data()
    print(data)

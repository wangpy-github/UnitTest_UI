from configparser import ConfigParser


class Parse_INI():
    def __init__(self, filepath):
        self.filepath = filepath
        self.config = ConfigParser()
        self.config.read(self.filepath, encoding="utf-8")

    """
    获取
    """

    # 获取所用的section节点
    def get_sections(self):
        return self.config.sections()

    # 获取指定section 的 options
    def get_options(self, section):
        return self.config.options(section)

    # 获取指点section下指点option的values
    def get_option_val(self, section, option):  # TODO
        return self.config.get(section, option)

    # 获取指点section的所用配置信息
    def get_opt_val_all(self, section):
        return self.config.items(section)

    """
    修改
    """

    # 修改某个option的值，如果不存在该option 则会创建
    def set_option(self, section, option, value):
        self.config.set(section, option, value)  # 修改db_port的值
        with open(self.filepath, "w") as f:
            self.config.write(open(f))

    # 添加section 和 option
    def add_section_option(self, section, option, value):
        if not self.config.has_section(section):  # 检查是否存在section
            self.config.add_section(section)
        if not self.config.has_option(section, option):  # 检查是否存在该option
            self.config.set(section, option, value)
        self.config.write(open(self.filepath, "w"))

    """
    删除
    """

    # 删除section 和 option
    def del_section_option(self):
        self.config.remove_section("default")  # 整个section下的所有内容都将删除
        with open(self.filepath, "w") as f:
            self.config.write(f)


if __name__ == '__main__':
    o = Parse_INI("../Config/item.ini")
    a = o.get_opt_val_all("ip_address")
    o.add_section_option("ip_address","d","ff")
    print(a)

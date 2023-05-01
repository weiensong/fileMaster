from file_master import FileMaster


class XianYuJingJi(FileMaster):
    def __init__(self, path):
        super().__init__(path)

    def run_task(self):
        sheet = self.read_excel('Sheet1')
        for j in range(1, 584):
            lineResult = []
            for i in range(1, 8):
                lineResult.append(str(sheet.cell(j, i).value).replace('_x000D_\n',''))
            if '指 标' in lineResult:
                print(lineResult)
                # todo
            elif '行政区域面积' in lineResult:
                # todo
                # fixme
                ...



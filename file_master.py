import openpyxl


class FileMaster:
    def __init__(self, path):
        self.path = path

    def run_task(self):
        raise NotImplementedError

    def read_excel(self, sheet):
        workbook = openpyxl.load_workbook(self.path)
        worksheet = workbook[f'{sheet}']
        return worksheet

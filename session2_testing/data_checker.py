class DataChecker:

    def __init__(self, csv_or_excel_file, config):
        self.file = csv_or_excel_file
        self.config = {
            'fields': ['date', 'amount', 'description'],
            'date_format': '%d/%m/%Y',
            'currency': '$',
        }

    def check_data(self):
        pass

    def _check_all_dates_are_actually_dates(self):
        pass

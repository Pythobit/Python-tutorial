class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, pages_per_sec: int, capacity: int):
        self.pages_per_sec = pages_per_sec
        self._capacity = capacity

    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError('Printer does not have enough space for the pages.')

        self._capacity -= pages

        return f'Printer {pages} pages in {pages/self.pages_per_sec:.2f} seconds'

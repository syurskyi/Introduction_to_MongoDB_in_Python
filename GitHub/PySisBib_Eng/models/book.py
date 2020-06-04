from models.callnum import CallNum
from datetime import date


class Book:
    def __init__(self, data_cad: date, call_num: CallNum, isbn: str, nome: str, authors: list, edition: int, year: int, publishing_company: str, form_acquisition: str, shelf: int):
        self.__data_cad = data_cad
        self.__call_num = call_num
        self.__isbn = isbn
        self.__nome = nome
        self.__authors = authors
        self.__edition = edition
        self.__year = year
        self.__publishing_company = publishing_company
        self.__form_acquisition = form_acquisition
        self.__shelf = shelf
        self.__data_baixa = None
        self.__motivo_baixa = None





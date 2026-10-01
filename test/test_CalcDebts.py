import pytest
from src.Types import DataType
from src.CalcDebts import CalcDebts
from src.XMLDataReader import XMLDataReader


class TestCalcDebts:

    def test_calc_debts_from_xml(self) -> None:
        reader = XMLDataReader()
        data = reader.read("./data/data.xml")
        
        calc_debts = CalcDebts(data)
        result = calc_debts.calc()
        
        # Сидоров (2 долга), Новикова (2 долга), Соколова (2 долга).
        # Итого должно быть 3 студента.
        assert result == 3

    def test_empty_data(self) -> None:
        calc_debts = CalcDebts({})
        assert calc_debts.calc() == 0
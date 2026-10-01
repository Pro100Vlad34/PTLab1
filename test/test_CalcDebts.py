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
        
        assert isinstance(result, list)
        assert len(result) == 3
        
        assert "Сидоров Сидор Сидорович" in result
        assert "Новикова Елена Владимировна" in result
        assert "Соколова Мария Дмитриевна" in result

    def test_empty_data(self) -> None:
        calc_debts = CalcDebts({})
        assert calc_debts.calc() == []
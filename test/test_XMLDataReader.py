import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    def test_read_valid_xml(self) -> None:
        reader = XMLDataReader()
        
        path = "./data/data.xml"
        
        result = reader.read(path)
        
        assert isinstance(result, dict)
        
        # Проверяем, что Иванов есть в списке
        assert "Иванов Иван Иванович" in result
        
        ivanov_subjects = result["Иванов Иван Иванович"]
        # Обновляем ожидаемые баллы согласно вашему data.xml
        assert ("математика", 80) in ivanov_subjects
        assert ("программирование", 90) in ivanov_subjects
        assert ("литература", 76) in ivanov_subjects

    def test_read_empty_xml(self, tmp_path) -> None:
        xml_content = "<?xml version='1.0'?><root></root>"
        file_path = tmp_path / "empty.xml"
        file_path.write_text(xml_content, encoding='utf-8')

        reader = XMLDataReader()
        result = reader.read(str(file_path))

        assert result == {}

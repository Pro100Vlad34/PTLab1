import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        students: DataType = {}

        for student_tag in root.findall('student'):
            name = student_tag.get('name')
            subjects = []

            for subject_tag in student_tag.findall('subject'):
                subj_name = subject_tag.get('name')
                score = int(subject_tag.text)
                subjects.append((subj_name, score))

            students[name] = subjects

        return students

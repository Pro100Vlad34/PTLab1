from Types import DataType

class CalcDebts:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> list[str]:
        students_with_debts = []
        for student, subjects in self.data.items():
            failures = [subj for subj, score in subjects if score < 61]
            
            if len(failures) == 2:
                students_with_debts.append(student)
                
        return students_with_debts
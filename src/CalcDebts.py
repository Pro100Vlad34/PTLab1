from Types import DataType


class CalcDebts:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0
        for student, subjects in self.data.items():
            failures = sum(1 for _, score in subjects if score < 61)
            
            if failures == 2:
                count += 1
                
        return count
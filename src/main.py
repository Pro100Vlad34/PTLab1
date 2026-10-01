import argparse
import sys
from XMLDataReader import XMLDataReader
from CalcDebts import CalcDebts

def get_path_from_arguments(args):
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def main():
    path = get_path_from_arguments(sys.argv[1:])
    
    reader = XMLDataReader()
    students = reader.read(path)
    
    print(f"Всего загружено студентов: {len(students)}\n")
    
    calc_debts = CalcDebts(students)
    debtors = calc_debts.calc()
    
    print(f"Найдено студентов с ровно двумя задолженностями: {len(debtors)}")
    print("-" * 40)
    
    for name in debtors:
        print(f"Студент: {name}")
        print("Предметы и оценки:")
        for subject, score in students[name]:
            # Помечаем задолженность звездочкой, если балл < 61
            mark = "*" if score < 61 else " "
            print(f"  - {subject}: {score} {mark}")
        print("-" * 40)

if __name__ == "__main__":
    main()
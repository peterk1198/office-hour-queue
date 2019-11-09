import sys
from src import student
from src.queue import ClassQueue

sys.path.append('./src')


def main():
    peter = student.Student('Peter Kwak', 3, 'A')
    print(peter.get_name(), peter.get_class_grade(), peter.get_year())
    q = ClassQueue()
    q.enqueue(peter)
    print(q.peek())


if __name__ == "__main__":
    main()

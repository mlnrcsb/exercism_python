class Garden:
    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)
    def plants(self, student):
        plant_map = {
            'G': 'Grass',
            'C': 'Clover',
            'R': 'Radishes',
            'V': 'Violets'
        }
        if student not in self.students:
            raise ValueError(f'{student} isn\'t a student here in the garden!')
        idx = self.students.index(student)
        return [plant_map[plant_char] for row in self.diagram for plant_char in row[2*idx:2*(idx+1)]]
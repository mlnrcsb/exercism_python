class School:
    def __init__(self):
        self.students = {}
        self._added = []

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        if name not in self.roster():
            self._added.append(True)
            self.students[grade].append(name)
        else:
            self._added.append(False)

    def roster(self):
        full_roster = []
        for grade in sorted(self.students.keys()):
            full_roster += sorted(self.students[grade])
        return full_roster
        

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))
    
    def added(self):
        return self._added

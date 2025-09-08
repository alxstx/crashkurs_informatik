class School:
    def __init__(self, name, specialisation, count, pupils):
        self.name = name
        self.specialisation = specialisation
        self.count = count
        self.pupils = pupils
    def add_pupil(self, pupil):
        self.pupils.append(pupil)
    def del_pupil(self, pupil):
        self.pupils.remove(pupil)
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name


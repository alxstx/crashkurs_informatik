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

class Gymnasium(School):
    def __init__(self, abi_tests):
        self.abi_tests = abi_tests
    def execute_abi(self):
        print("Abitur geplant...")
        # do something


cotta_school = Gymnasium("cotta","wg",500,[])
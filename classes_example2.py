from classes_example import School

class Gymnasium(School):
    def __init__(self, abi_tests):
        self.abi_tests = abi_tests
    def execute_abi(self):
        print("Abitur geplant...")
        # do something


cotta_school = Gymnasium("cotta","wg",500,[])
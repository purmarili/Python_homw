class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.pass_mark = pass_mark
        self.mark_scheme = mark_scheme


class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken

    def take_test(self, test_paper, mark_scheme):
        score = 0
        for i, mark in enumerate(test_paper.mark_scheme):
            if mark == mark_scheme[i]:
                score += 1
        score = round(score / len(mark_scheme) * 100)
        result = f"({score}%)"
        if result[1:-1] >= test_paper.pass_mark:
            result = "Passed! " + result
        else:
            result = "Failed! " + result
        if type(self.tests_taken) is not dict:
            self.tests_taken = {}
        self.tests_taken[test_paper.subject] = result


if __name__ == '__main__':
    paper1 = TestPaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = TestPaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = TestPaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "60%")

    student1 = Student()
    student2 = Student()

    print(student1.tests_taken)
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    print(student1.tests_taken)

    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    print(student2.tests_taken)

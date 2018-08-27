super_grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

"""
aslists(grades), which takes a grades list as specified above and creates a dict[str, list[float]] mapping names to lists of grades.

asdicts(grades), which takes a grades list as specified above and creates a dict[str, dict[str, float]] mapping names to dictionaries of grades.

stud_means(grades), which takes a dict[str, list[float]] mapping names to lists of grades and creates a dict mapping names to grade means.

item_mean(grades, item), which takes a dict[str, dict[str, float]] and create a dict[str, float] mapping items to average for that item across all students.

(Optional) rank(grades, item), which takes a dict[str, dict[str, float]] mapping names to dicts of grades and returns a list[tuple[str, float]] of (student, grade) pairs where grade is the grade for student on item, sorted in descending order by the grades.
"""


def asLists(grades):
    """takes grades list and creates a dict[str, list[float]] mapping names to lists of grades

    Parameters: list[list[str]]

    Returns:
    dict: {str: list}
    """
    return {a_list_of_grades[0]: a_list_of_grades[1:] for a_list_of_grades in grades[1:]}


def asdicts(grades):
    """creates a dict[str, dict[str, float]] mapping names to dictionaries of grades
    Parameters:
    grades: list[list[str]]

    Returns:
    dict[str, dict[str, float]]
    """
    result = {}
    titles = grades[0]
    for grade_line in grades[1:]:
        name = grade_line[0]
        result[name] = {}
        for i in range(1,4):
            exam = titles[i]
            result[name][exam] = grade_line[i]
    return result


def stud_means(grades):
    """creates a dict[str, float] mapping result of asLists to name: grade_average
    """
    # result = {}
    # for key, values in grades.items():
    #     ints = [int(v) for v in values]
    #     total = sum(ints)
    #     mean = total / len(ints)
    #     result[key] = mean
    # return result
    return {key: (sum([int(v) for v in values]) / len(values)) for key, values in grades.items()}

def item_mean(grades):
    """Return dict of mapping item to average of item for all students from grades of result of asdicts
    """
    result = {}
    exams1 = [int(gradeDict['Exam 1']) for _, gradeDict in grades.items()]
    exams2 = [int(gradeDict['Exam 2']) for _, gradeDict in grades.items()]
    exams3 = [int(gradeDict['Exam 3']) for _, gradeDict in grades.items()]
    result['Exam 1'] = sum(exams1) / len(exams1)
    result['Exam 2'] = sum(exams2) / len(exams2)
    result['Exam 3'] = sum(exams3) / len(exams3)
    return result

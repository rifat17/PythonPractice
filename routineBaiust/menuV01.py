dept_choice = {
    'CSE' : '1',
    'EEE' : '2',
    'CE'  : '3',
    'BBA' : '4',
    'ENG' : '5',
    'LAW' : '6'
}
semester = {
    '111' : '1',
    '112' : '2',
    '121' : '3',
    '122' : '4',
    '211' : '5',
    '212' : '6',
    '221' : '7',
    '222' : '8',
    '311' : '9',
    '312' : '10',
    '321' : '11',
    '322' : '12',
    '411' : '13',
    '412' : '14',
    '421' : '15',
    '422' : '16'
    }

def display_dept():
    print("""
    Choose a Department
    1. CSE
    2. EEE
    3. CE
    4. BBA
    5. ENG
    6. LAW
    """)
def display_level():
    print("""
    1. L1
    2. L2
    3. L3
    4. L4
    """)
def display_term():
    print("""
    1. Term_1
    2. Term_2
    """)
def display_section():
    print("""
    1. Section_A
    2. Section_B
    """)
def input_promot():
    display_dept()
    dept = (input())
    display_level()
    level = (input())
    display_term()
    term = (input())
    display_section()
    section = (input())

    # print(level,term,section)
    sem = level+term+section
    # print(semester[sem])
    if (int(dept) > 0 and int(dept) <= 6) and ( int(semester[sem]) > 0 and int(semester[sem]) <= 16):
        return (dept, semester[sem] )
    return None



if __name__ == "__main__":
    
    try:
        dept,semester = input_promot()
        url = "http://routine.baiust.edu.bd/?department_id={deptNo}&semester={semNo}".format(deptNo=dept,semNo=semester)
        print(url)
    except Exception as e:
        print("Wrong info :/")

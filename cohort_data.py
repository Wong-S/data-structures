"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # TODO: replace this with your code
    data_file = open(filename)
    for line in data_file:
        words = line.split("|")
        houses.add(words[2])
    houses.remove("")

    return houses


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # TODO: replace this with your code
    # Conditional statement
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        # if cohort = all and != I or G, then append fullname of student into empty list
        if cohort == "All":
            if words[4] != "I" and words[4] != "G":
                fullname = f"{words[0]} {words[1]}"
                # print(fullnacme)  # Check
                students.append(fullname)
                # print(students)

        else:
            if words[4] == cohort:
                fullname = f"{words[0]} {words[1]}"
                # print(fullname)  # Check
                students.append(fullname)
                # print(students)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        house = words[2]
        # print(house)

        if house == "Dumbledore's Army":
            # print("dumble")
            dumbledores_army.append(f"{words[0]} {words[1]}")
        if house == "Gryffindor":
            gryffindor.append(f"{words[0]} {words[1]}")
        if house == "Hufflepuff":
            hufflepuff.append(f"{words[0]} {words[1]}")
        if house == "Ravenclaw":
            ravenclaw.append(f"{words[0]} {words[1]}")
        if house == "Slytherin":
            slytherin.append(f"{words[0]} {words[1]}")
        if words[4] == "G":
            ghosts.append(f"{words[0]} {words[1]}")
        if words[4] == "I":
            instructors.append(f"{words[0]} {words[1]}")

    return [
        sorted(dumbledores_army),
        sorted(gryffindor),
        sorted(hufflepuff),
        sorted(ravenclaw),
        sorted(slytherin),
        sorted(ghosts),
        sorted(instructors),
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        all_data.append((f"{words[0]} {words[1]}", words[2], words[3], words[4]))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        # if name == fulllname, return words[4] or none
        if name == f"{words[0]} {words[1]}":
            return words[4]
    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    # Save a list of names, as we cycle through list, if not in list, then add.
    # Check if alreday in names.
    # First list = [] --> keep track of list we have
    # Second list = [] --> as we iterate through, check to see if it's in first list, if it is, then add to second list
    all_last_names = []
    duplicate_names = []

    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        if words[1] in all_last_names:
            duplicate_names.append(words[1])

        else:
            all_last_names.append(words[1])

    return set(duplicate_names)


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        if name == f"{words[0]} {words[1]}":
            house = words[2]
            cohort = words[4]
    # print(house)
    # print(cohort)
    housemates = []
    data_file = open(filename)
    for line in data_file:
        words = line.rstrip().split("|")
        # print("second for")
        if words[2] == house and words[4] == cohort:
            # print("found housemate")
            if f"{words[0]} {words[1]}" != name:
                # print("Not the name")
                housemates.append(f"{words[0]} {words[1]}")
    # print(housemates)

    return set(housemates)
    # check if words[2] == student's house, words[4] == student's cohort
    # return set of housemates' names


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py", report=False, optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE)
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")


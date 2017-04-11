dict_teachers = {
    'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', "JavaScript"],
    'Kenneth Love': ['Python Basics', 'Python Collections']
}

def num_teachers(dict_teachers):
  num_of_teachers = 0
  for key in dict_teachers.keys():
    num_of_teachers += 1
  return num_of_teachers


num_teachers(dict_teachers)


def num_courses(dict_teachers):
  num_of_courses = 0
  for value in dict_teachers.values():
    num_of_courses += len(value)
  return num_of_courses

num_courses(dict_teachers)


def courses(dict_teachers):
  all_courses = []
  for value in dict_teachers.values():
    all_courses.extend(value)
  return all_courses

courses(dict_teachers)


def most_courses(dict_teachers):
  count = 0
  teacher_most_courses = None
  for key, value in dict_teachers.items():
    if len(value) > count:
      count = len(value)
      teacher_most_courses = key
    else:
      pass
  return teacher_most_courses

most_courses(dict_teachers)


def teacher_stats(dict_teachers):
  teacher_num_courses = list()
  for key, value in dict_teachers.items():
    teacher_list = [key, len(value)]
    teacher_num_courses.append(teacher_list)
  return teacher_num_courses

teacher_stats(dict_teachers)








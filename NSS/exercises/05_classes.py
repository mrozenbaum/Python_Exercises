# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.
# Create a company, and three employees, and then assign the employees to the company.


class Company():
    """This represents a company in which people work"""

    def __init__(self, name):
      self.name = name
      self.employees = set()

    def get_name(self):
      """Returns the name of the company"""

      return self.name

  # Add the remaining methods to fill the requirements above
    def set_name(name):
        self.name = name

class Employee():

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

    def get_name(self):

      return self.name

    def set_name(name):
        self.name = name

kao_jai_coffee = Company("Kao Jai Coffee", )
meg = Employee("Meg Ducharme", "Co-Founder", "04/04/06")
kyle = Employee("Kyle Ducharme", "Co-Founder", "04/04/06")

kao_jai_coffee.employees.add(meg)
kao_jai_coffee.employees.add(kyle)

print(kao_jai_coffee.employees)
print(meg.get_name())

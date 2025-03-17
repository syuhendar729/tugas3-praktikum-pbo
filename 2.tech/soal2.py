from abc import abstractmethod


class Employee:
    def __init__(self, name, hours_worked, task_completed) -> None:
        self._name = name
        self._hours_worked = hours_worked
        self._task_completed = task_completed
        self._rating = 'None'

    @abstractmethod
    def work(self):
        pass

    def evaluate_performance(self):
        p_value = int(self._task_completed / self._hours_worked)
        if p_value >= 10: self._rating = 'High'
        elif p_value >= 6: self._rating = 'Medium'
        else: self._rating = 'Low'

class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, hours_worked, task_completed)

    def work(self):
        super().evaluate_performance()
        print(f"{self._name} (Software Engineer) is coding.")
        print(f"Performance Rating: {self._rating} Performance")
        print()

        
class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, hours_worked, task_completed)

    def work(self):
        super().evaluate_performance()
        print(f"{self._name} (Data Scientist) is analyzing data.")
        print(f"Performance Rating: {self._rating} Performance")
        print()


class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, hours_worked, task_completed)

    def work(self):
        super().evaluate_performance()
        print(f"{self._name} (Product Manager) is managing the product roadmap.")
        print(f"Performance Rating: {self._rating} Performance")
        print()


oda_se = SoftwareEngineer('Oda', 10, 1000)
oda_ds = DataScientist('Oda', 10, 60)
oda_pm = ProductManager('Oda', 10, 20)

oda_se.work()
oda_ds.work()
oda_pm.work()

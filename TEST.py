import unittest
import datetime
import os

class Reminder:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def is_today(self):
        today = datetime.date.today()
        return self.date.month == today.month and self.date.day == today.day

    def notify(self):
        raise NotImplementedError("Subclasses must implement notify method")

class BirthdayReminder(Reminder):
    def notify(self):
        return f"It's {self.name}'s birthday today!"

class User:
    def __init__(self, name):
        self.name = name
        self.reminders = []

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

    def remove_reminder(self, name):
        self.reminders = [reminder for reminder in self.reminders if reminder.name != name]

    def print_reminders(self):
        today = datetime.date.today()
        reminders_exist = False
        for reminder in self.reminders:
            if reminder.is_today():
                reminders_exist = True
                print(reminder.notify())
        if not reminders_exist:
            print(f"No birthday reminders for {self.name} today.")

class ReminderFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_reminder(self, reminder_type, name, date):
        if reminder_type == "birthday":
            return BirthdayReminder(name, date)
        else:
            raise ValueError("Invalid reminder type")

class ReminderStorage:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.factory = ReminderFactory()
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    user_name, name, date_str = line.strip().split(",")
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    user = self.users.get(user_name)
                    if not user:
                        user = User(user_name)
                        self.users[user_name] = user
                    reminder = self.factory.create_reminder("birthday", name, date)
                    user.add_reminder(reminder)

    def save_data(self):
        with open(self.filename, "w") as file:
            for user_name, user in self.users.items():
                for reminder in user.reminders:
                    file.write(f"{user_name},{reminder.name},{reminder.date}\n")

    def add_reminder(self, user_name, name, date):
        user = self.users.get(user_name)
        if not user:
            user = User(user_name)
            self.users[user_name] = user
        reminder = self.factory.create_reminder("birthday", name, date)
        user.add_reminder(reminder)
        self.save_data()

    def remove_reminder(self, user_name, name):
        user = self.users.get(user_name)
        if user:
            user.remove_reminder(name)
            if not user.reminders: 
                del self.users[user_name]
            self.save_data()

    def print_reminders(self, user_name):
        user = self.users.get(user_name)
        if user:
            user.print_reminders()
        else:
            print("User not found.")

class TestReminderStorage(unittest.TestCase):
    def setUp(self):
        self.storage = ReminderStorage("birthdays.txt")

    def test_add_reminder(self):
        self.storage.add_reminder("Test", "Test", datetime.date.today())
        self.assertTrue(self.storage.users.get("Test"))

    def test_remove_reminder(self):
        self.storage.add_reminder("Test", "Test", datetime.date.today())
        
        self.assertIsNotNone(self.storage.users.get("Test"))

        self.storage.remove_reminder("Test", "Test")
        
        self.assertIsNone(self.storage.users.get("Test"))

    def test_another_test_case(self):
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()



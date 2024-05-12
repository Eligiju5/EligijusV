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
        print(f"It's {self.name}'s birthday today!")


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
                reminder.notify()
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
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        data_file = os.path.join(desktop_path, self.filename)
        if os.path.exists(data_file):
            with open(data_file, "r") as file:
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
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        data_file = os.path.join(desktop_path, self.filename)
        with open(data_file, "w") as file:
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


def main():
    storage = ReminderStorage("birthdays.txt")
    while True:
        print("\nBirthday Reminder Menu:")
        print("1. Add Birthday")
        print("2. Remove Birthday")
        print("3. Print Birthday Reminders")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter user name: ")
            name = input("Enter name: ")
            date = input("Enter birthday (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            storage.add_reminder(user_name, name, date)
            print("Birthday added successfully!")
        elif choice == "2":
            user_name = input("Enter user name: ")
            name = input("Enter name to remove: ")
            storage.remove_reminder(user_name, name)
            print("Birthday removed successfully!")
        elif choice == "3":
            user_name = input("Enter user name: ")
            storage.print_reminders(user_name)
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()



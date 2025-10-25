import random

def load_reminders(path="data/reminders.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    reminders = load_reminders()
    reminder = random.choice(reminders)
    print("\n💡 Crypto Daily Reminder:\n")
    print(reminder)

if __name__ == "__main__":
    main()

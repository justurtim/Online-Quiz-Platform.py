from modules.quiz import Quiz
from modules.user import list_quiz_categories
from modules.utils import print_logo

def main():
    print_logo()
    categories = list_quiz_categories()

    print("\nAvailable Quizzes:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")

    try:
        choice = int(input("\nEnter quiz number to start: "))
        selected = categories[choice - 1]
        quiz = Quiz(selected)
        quiz.start()
    except:
        print("❌ Invalid selection. Exiting.")

if __name__ == "__main__":
    main()

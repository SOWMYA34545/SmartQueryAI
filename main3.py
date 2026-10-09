
from web_search import ask_question

current_question = ""

while True:
    print("\n" + "=" * 50)
    print("                 WEBQUERY AI")
    print("=" * 50)
    print("1. Ask a question")
    print("2. Change the question")
    print("3. Exit")
    print("=" * 50)

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        question = input("\nEnter your question: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        current_question = question

    elif choice == "2":
        if not current_question:
            print("\nNo previous question found.")
            print("Please choose option 1 first.")
            continue

        print("\nCurrent question:", current_question)

        question = input("Enter your new question: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        current_question = question

    elif choice == "3":
        print("\nThank you for using WebQuery AI!")
        print("Program ended.")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
        continue

    try:
        print("\nSearching the web and generating your answer...")

        answer = ask_question(current_question)

        print("\nQUESTION:")
        print(current_question)

        print("\nANSWER:")
        print("-" * 50)
        print(answer)
        print("-" * 50)

    except Exception as e:
        print("\nERROR:")
        print(e)
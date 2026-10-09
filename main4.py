
from web_search import ask_question

while True:
    print("\n========== WEBQUERY AI ==========")
    print("1. Ask a question")
    print("2. Exit")
    print("=================================")

    choice = input("Enter your choice (1-2): ").strip()

    if choice == "2":
        print("Thank you for using WebQuery AI!")
        break

    elif choice != "1":
        print("Invalid choice. Please enter 1 or 2.")
        continue

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a question.")
        continue

    while True:
        print("\nYour question:", question)
        print("\nWhat would you like to do?")
        print("1. Change the question")
        print("2. Proceed with this question")

        option = input("Enter your choice (1-2): ").strip()

        if option == "1":
            question = input("\nEnter your new question: ").strip()

            if not question:
                print("Question cannot be empty.")
                question = input("Please enter your question: ").strip()

                if not question:
                    continue

        elif option == "2":
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    try:
        print("\nSearching the web and generating your answer...")
        answer = ask_question(question)

        print("\nQUESTION:", question)
        print("\nANSWER:")
        print("-" * 45)
        print(answer)
        print("-" * 45)

    except Exception as e:
        print("\nERROR:", e)
        
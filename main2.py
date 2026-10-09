print("MAIN2 IS RUNNING")
from web_search import ask_question

from web_search import ask_question


print("=" * 60)
print("       GEMINI WEB SEARCH QUESTION ANSWER")
print("=" * 60)


while True:

    print("\nWhat would you like to do?")
    print("1. Ask a new question")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "2":
        print("\nProgram ended.")
        break

    if choice != "1":
        print("\nPlease enter 1 or 2.")
        continue

    question = input("\nEnter your question: ")

    if not question.strip():
        print("\nPlease enter a question.")
        continue

    try:

        answer = ask_question(question)

        print("\nANSWER:")
        print("-" * 60)
        print(answer)
        print("-" * 60)

        while True:

            print("\nWould you like to know more about this?")
            print("1. Yes")
            print("2. No")

            more_choice = input("\nEnter your choice: ")

            if more_choice == "1":

                follow_up = input(
                    "\nWhat would you like to know more about? "
                )

                if not follow_up.strip():
                    print("\nPlease enter a question.")
                    continue

                answer = ask_question(follow_up)

                print("\nANSWER:")
                print("-" * 60)
                print(answer)
                print("-" * 60)

            elif more_choice == "2":
                break

            else:
                print("\nPlease enter 1 or 2.")

        print("\nWould you like to continue?")
        print("1. Ask another question")
        print("2. Exit")

        continue_choice = input("\nEnter your choice: ")

        if continue_choice == "2":
            print("\nProgram ended.")
            break

        if continue_choice != "1":
            print("\nInvalid choice. Starting a new question.")

    except Exception as e:

        print("\nERROR:")
        print(e)
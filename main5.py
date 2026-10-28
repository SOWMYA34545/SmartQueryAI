
from web_search_2 import (
    ask_question,
    load_prompt_rules,
    save_prompt_rules,
    DEFAULT_PROMPT_RULES
)


def change_prompt_rules():
    current_rules = load_prompt_rules()

    print("\n========== CURRENT PROMPT RULES ==========")

    for i, rule in enumerate(current_rules, start=1):
        print(f"{i}. {rule}")

    print("\nEnter your new prompt rules, one rule per line.")
    print("Type DONE when you finish entering rules.")
    print("Type DEFAULT as the first entry to restore defaults.")

    new_rules = []

    while True:
        rule = input("\nRule: ").strip()

        if not new_rules and rule.upper() == "DEFAULT":
            save_prompt_rules(DEFAULT_PROMPT_RULES.copy())
            print("\nDefault prompt rules restored.")
            return

        if rule.upper() == "DONE":
            break

        if rule:
            new_rules.append(rule)

    if new_rules:
        save_prompt_rules(new_rules)
        print("\nPrompt rules saved successfully!")
    else:
        print("\nNo new rules entered. Existing rules remain unchanged.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("                 WEBQUERY AI")
        print("                  VERSION 5")
        print("=" * 50)
        print("1. Change prompt rules")
        print("2. Give a question")
        print("3. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            change_prompt_rules()

        elif choice == "2":
            question = input("\nEnter your question: ").strip()

            if not question:
                print("Please enter a question.")
                continue

            try:
                print("\nSearching the web and generating your answer...")

                answer = ask_question(question)

                print("\nQUESTION:")
                print(question)

                print("\nANSWER:")
                print("-" * 50)
                print(answer)
                print("-" * 50)

            except Exception as error:
                print("\nERROR:", error)

        elif choice == "3":
            print("\nThank you for using WebQuery AI!")
            print("Program ended.")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

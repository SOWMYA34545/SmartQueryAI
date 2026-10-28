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

    print("\nHow would you like to change the rules?")
    print("1. Use DEFAULT rules and add extra rules")
    print("2. Enter completely new rules")
    print("3. Keep current rules")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        # Start with all default rules
        new_rules = DEFAULT_PROMPT_RULES.copy()

        print("\nDefault rules selected.")
        print("Now enter your extra rules, one per line.")
        print("Type DONE when you finish.")

    elif choice == "2":
        # Replace the existing rules with new rules
        new_rules = []

        print("\nEnter your new prompt rules, one per line.")
        print("Type DONE when you finish.")

    elif choice == "3":
        print("\nKeeping the current prompt rules unchanged.")
        return

    else:
        print("\nInvalid choice. Rules have not been changed.")
        return

    while True:
        rule = input("\nRule: ").strip()

        if rule.upper() == "DONE":
            break

        if rule:
            new_rules.append(rule)

    if choice == "2" and not new_rules:
        print("\nNo new rules entered. Keeping existing rules.")
        return

    # Save the final rules to prompt_rules5.json
    save_prompt_rules(new_rules)

    print("\nPrompt rules saved successfully!")
    print("\nYour final prompt rules are:")

    for i, rule in enumerate(new_rules, start=1):
        print(f"{i}. {rule}")


def main():
    while True:
        print("\n" + "=" * 50)
        print("             WEBQUERY AI")
        print("              VERSION 5")
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
                print(
                    "\nSearching the web and generating your answer..."
                )

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

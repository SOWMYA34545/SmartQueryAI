from web_search import ask_question

print("=" * 60)
print("       GEMINI WEB SEARCH QUESTION ANSWER")
print("=" * 60)

while True:

    question = input("\nEnter your question (or type 'exit'): ")

    if question.lower() == "exit":
        print("Program ended.")
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    try:
        answer = ask_question(question)

        print("\nANSWER:")
        print("-" * 60)
        print(answer)
        print("-" * 60)

    except Exception as e:
        print("\nERROR:")
        print(e)
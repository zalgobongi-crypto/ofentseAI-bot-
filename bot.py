from datetime import datetime
import random
import ast
import operator

BOT_NAME = "OFENTSE AI BOT"
VERSION = "2.0"

JOKES = [
    "Why do programmers love Python? Because life is short!",
    "Why did the computer get cold? It left its Windows open!",
    "Why do Java developers wear glasses? Because they don't C#!"
]

# Safe arithmetic operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def calculate(expression):
    if len(expression) > 100:
        raise ValueError("Expression too long")

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            if isinstance(node.op, ast.Pow) and abs(evaluate(node.right)) > 10:
                raise ValueError("Exponent too large")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if abs(left) > 1e100 or abs(right) > 1e100:
                raise ValueError("Number too large")

            result = OPERATORS[type(node.op)](left, right)

            if abs(result) > 1e100:
                raise ValueError("Result too large")

            return result

        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.operand))

        raise ValueError("Only basic arithmetic is allowed")

    return evaluate(ast.parse(expression, mode="eval").body)


def show_menu():
    print("""
========== OFENTSE AI BOT ==========
.menu       Show commands
.time       Show current time
.joke       Tell a joke
.calculate  Calculate an expression
.ping       Test the bot
.about      About this bot
.clear      Clear the screen
.exit       Stop the bot
====================================
""")


def main():
    print(f"{BOT_NAME} v{VERSION}")
    print("Status: ONLINE")
    print("Type .menu to see commands.")

    while True:
        try:
            command = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot stopped.")
            break

        if not command:
            continue

        name, _, argument = command.partition(" ")
        name = name.lower()

        if name in (".menu", ".help", "help"):
            show_menu()

        elif name == ".ping":
            print("Pong! Bot is working!")

        elif name == ".time":
            print("Current time:", datetime.now().astimezone().strftime(
                "%Y-%m-%d %H:%M:%S %Z"
            ))

        elif name == ".joke":
            print(random.choice(JOKES))

        elif name == ".calculate":
            try:
                print("Answer:", calculate(argument))
            except (ValueError, SyntaxError, ZeroDivisionError,
                    OverflowError) as error:
                print("Calculation error:", error)

        elif name == ".about":
            print(f"{BOT_NAME}, version {VERSION}.")
            print("Built with Python.")

        elif name == ".clear":
            print("\n" * 30)

        elif name in (".exit", "exit"):
            print("Bot shutting down. Peace!")
            break

        else:
            print("Unknown command. Type .menu")


if __name__ == "__main__":
    main()
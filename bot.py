def main():
    print("================================")
    print("   🐧 OFENTSE AI BOT")
    print("================================")
    print("Bot status: ONLINE")
    print("Version: 1.0")
    print("Type help to see available commands.")

    while True:
        command = input("You: ").strip().lower()

        if command == "help":
            print("Commands: help, ping, about, exit")
        elif command == "ping":
            print("Pong! Bot is online.")
        elif command == "about":
            print("Ofentse AI Bot - built from scratch!")
        elif command == "exit":
            print("Bot shutting down. Peace!")
            break
        else:
            print("Unknown command. Type help.")


if __name__ == "__main__":
    main()
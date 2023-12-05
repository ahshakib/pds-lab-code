import Pyro4

def main():
    uri = input("Enter the URI of the Tic Tac Toe server: ").strip()
    tic_tac_toe = Pyro4.Proxy(uri)

    print(tic_tac_toe.display_board())

    while True:
        try:
            position = int(input(f"Player {tic_tac_toe.current_player}, enter your move (1-9): ")) - 1
            result = tic_tac_toe.make_move(position)
            print(result)

            if "wins" in result or "draw" in result:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()

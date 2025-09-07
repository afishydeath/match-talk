valid_command = tuple[str, int] | tuple[str, str] | str


def process_command(command: valid_command) -> None:
    if (
        isinstance(command, tuple) # Check the command is a tuple, which we use if it has a thing to do and an amount
        and len(command) == 2 # Check the list only has one command and one argument
        and command[0] == "move" # Check the command is to move
        and isinstance((amount := command[1]), int) # Bonus! assign position 2 to the variable "amount" and check it is an int
    ):
        pass

    match command:
        case tuple(["move", int(amount)]):  # noqa:F841 # Do all of those as well!
            pass

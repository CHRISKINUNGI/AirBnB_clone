#!/usr/bin/python3
"""
    consol
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
       args
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ EOF command to exit the program """

        return True

    def do_quit(self, line):
        """ Quit command to exit the program """

        return True

    def emptyline(self):
        """
            nothing happens;
            emptyline + enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
    consol
"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints
            the id. Ex: $ create BaseModel
        """
        if line is None:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_object = BaseModel()
            my_object.save()
            print(my_object.id)

    def do_show(self, line):
        """
           Prints the string representation of an
           instance based on the class name and 
           id. Ex: $ show BaseModel 1234-1234-1234
        """
        line = line.split()
        len_line = len(line)
        if len_line == 0:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len_line == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            obj_found = False
            for obj in storage.all().values():
                if obj.id == line[1]:
                    print(str(obj))
                    obj_found = True
                    break
            if obj_found == False:
                print("** no instance found **")

    def do_destroy(self, line):
        """
           Deletes an instance based on the class
           name and id (save the change
           into the JSON file).
        """
        if line is None:
            print("** class name missing **")
        elif line != "my_object":
            print("** class doesn't exist **")
        elif my_object.id is None:
            print("** instance id missing **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()

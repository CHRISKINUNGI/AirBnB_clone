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
            if obj_found is False:
                print("** no instance found **")

    def do_destroy(self, line):
        """
           Deletes an instance based on the class
           name and id (save the change
           into the JSON file).
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
                    my_line = "{}.{}".format(line[0], line[1])
                    del storage.all()[my_line]
                    storage.save()
                    obj_found = True
                    break
            if obj_found is False:
                print("** no instance found **")

    def do_all(self, line):
        """
           Prints all string representation of all instances based or
           not on the class name
        """
        line = line.split()
        len_line = len(line)
        if len_line == 0:
            my_list = []
            for obj in storage.all().values():
                my_list.append(str(obj))
            print(my_list)
        if line != "BaseModel":
            print("** class doesn't exist **")

    def do_update(self, line):
        """
           Updates an instance based on the class name and id by adding
           or updating attribute (save the change into the JSON file)
           update <class name> <id> <attribute name> "<attribute value>"
        """
        line = line.split()
        len_line = len(line)
        if len_line == 0:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len_line == 1:
            print("** instance id missing **")
        elif len_line == 2:
            print("** attribute name missing **")
        elif len_line == 3:
            print("** value missing **")
        else:
            storage.reload()
            obj_found = False
            for obj in storage.all().values():
                if obj.id == line[1]:
                    obj_found = True
                    setattr(obj, line[2], line[3])
                    storage.save()
                    break
            if obj_found is False:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models.engine import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parses a command string into a list of arguments."""
    pattern = r"(\{[^}]*\}|(\[.*?\]|[^ \t\n,]+))(,|\s+|$)"
    match = re.findall(pattern, arg)
    return [m[0].strip() for m in match]


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a given class."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Print the string representation of a class instance."""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj_dict = storage.all()
            if f"{args[0]}.{obj_id}" not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[f"{args[0]}.{obj_id}"])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj_dict = storage.all()
            if f"{args[0]}.{obj_id}" not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[f"{args[0]}.{obj_id}"]
                storage.save()

    def do_all(self, arg):
        """Print string representations of all instances of a given class."""
        args = parse(arg)
        obj_dict = storage.all()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objs = [obj.__str__() for obj in obj_dict.values()
                    if not args or obj.__class__.__name__ == args[0]]
            print(", ".join(objs))

    def do_count(self, arg):
        """Print the number of instances of a given class."""
        args = parse(arg)
        if not args or args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for instance in Storage.all().values()
                        if instance.__class__.__name__ == args[0])
            print(count)



 if __name__ == "__main__":
    HBNBCommand().cmdloop()

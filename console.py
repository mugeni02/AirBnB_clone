#!/usr/bin/python3
import cmd
import json
import sys
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Console for AirBnB"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the console"""
        sys.exit()

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl-D)"""
        sys.exit()

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of a class and save it to JSON"""
        if not line:
            print("** class name missing **")
            return
        args = re.split(r"\s+", line)
        if len(args) > 1:
            cls_name = args[0]
            if cls_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            del args[0]
        else:
            cls_name = "BaseModel"
        if not args:
            print("** instance name missing **")
            return
        instance = eval(cls_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Print the string representation of an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = re.split(r"\s+", line)
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        if cls_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        del args[0]
        key = "{}.{}".format(cls_name, ' '.join(args))
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = re.split(r"\s+", line)
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        if cls_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        del args[0]
        key = "{}.{}".format(cls_name, ' '.join(args))
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Print all string representation of all instances of a class"""
        if not line:
            print("** class name missing **")
            return
        args = re.split(r"\s+", line)
        if len(args) > 1:
            cls_name = args[0]
            if cls_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            del args[0]
        else:
            cls_name = "BaseModel"
        print([str(val) for key, val in storage.all().items() if key.startswith(cls_name)])

    def do_update(self, line):

        if __name__ == '__main__':
    HBNBCommand().cmdloop()

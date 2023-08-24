#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from shlex import split
from models import storage
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = "(hbnb) "

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def parse(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        arg_list = line.split('.')
        if len(arg_list) >= 2:
            if arg_list[1] == "all()":
                self.do_all(arg_list[0])
            elif arg_list[1] == "count()":
                self.do_count(arg_list[0])
            elif arg_list[1][:4] == "show":
                self.do_show(self.parse(arg_list))
            elif arg_list[1][:7] == "destroy":
                self.do_destroy(self.parse(arg_list))
            elif arg_list[1][:6] == "update":
                args = self.parse(arg_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
            else:
                print('*** Unknown syntax: {}'.format(line))
        else:
            cmd.Cmd.default(self, line)

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print("")
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("EOF signal to exit the program.")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split(" ")
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg_list[0]]()
        print(new_instance.id)
        for num in range(1, len(arg_list)):
            arg_list[num] = arg_list[num].replace('=', ' ')
            attributes = split(arg_list[num])
            attributes[1] = attributes[1].replace('_', ' ')
            try:
                var = eval(attributes[1])
                attributes[1] = var
            except Exception:
                pass
            if type(attributes[1]) is not tuple:
                setattr(new_instance, attributes[0], attributes[1])
        new_instance.save()

    def help_create(self):
        """ Help information for the create method """
        print("Create a new class instance and print its id.")
        print("[Usage]: create <className>")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []
        objects = storage.all()
        if args:
            arg = args.split(' ')[0]  # remove possible trailing args
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key in objects:
                if key.split('.')[0] == arg:
                    print_list.append(objects[key])
        else:
            for k, v in objects.items():
                print_list.append(v)

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Display string representations of all instances of a given \
              class.")
        print("[Usage]: all or all <class> or <class>.all()")

    def do_count(self, args):
        """Count current number of class instances"""
        counter = 0
        arg_list = split(args, " ")
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        for key in objects:
            name = key.split('.')
            if name[0] == arg_list[0]:
                counter += 1
        print(counter)

    def help_count(self):
        """ """
        print("Retrieve the number of instances of a given class.")
        print("Usage: count <class> or <class>.count()")

    def do_update(self, args):
        """ Updates a certain object with new info """
        if args == ' ' or not args:  # class name not present
            print("** class name missing **")
            return
        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        arg_list = split(args, " ")
        if arg_list[0] not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:  # id not present
            print("** instance id missing **")
            return
        objs = storage.all()
        key = arg_list[0] + '.' + arg_list[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(arg_list) < 3:  # check for att_name
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:  # check for att_value
            print("** value missing **")
            return
        obj = objs[key]
        try:
            obj.__dict__[arg_list[2]] = eval(arg_list[3])
        except Exception:
            obj.__dict__[arg_list[2]] = arg_list[3]
        obj.save()   # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

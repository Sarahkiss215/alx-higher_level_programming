#!/usr/bin/python3
""" Module base.py """

import os
import turtle
import json
import csv


class Base:
    """Defines a Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list(map(lambda x:
                                                    x.to_dictionary(),
                                                    list_objs))))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**d) for d in
                        cls.from_json_string(f.read())]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        fname = cls.__name__ + ".csv"

        if list_objs is None:
            with open(fname, "w") as cfile:
                cfile.write("[]")
        else:
            with open(fname, "w") as cfile:
                writer = csv.writer(cfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        fname = cls.__name__ + ".csv"

        with open(fname, "r") as cfile:
            if cls.__name__ == "Rectangle":
                reader = csv.DictReader(
                    cfile, fieldnames={'id', 'width', 'height', 'x', 'y'})
            elif cls.__name__ == "Square":
                reader = csv.DictReader(
                    cfile, fieldnames={'id', 'size', 'x', 'y'})

            instances = []
            for instance in reader:
                instance = {x: int(y) for x, y in instance.items()}
                temp = cls.create(**instance)
                instances.append(temp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()

from Graph import *


class Navigation(object):
    def __init__(self, csv):
        self.__map = Graph(csv)
        self.__prev = None
        self.__finished = False
        self.__cnt = 0

    def navigate(self, start, end, disabled=False):
        try:
            dist, path = self.__map.shortest_path(start, end, disabled)
            self.__map.parse_path(path)
            print("Total distance: " + str(dist))
        except ValueError as err:
            print(err)

    def simulate(self):
        self.__map.print_nodes()
        while True:
            if self.__cnt == 0:
                input("Welcome to the zoo! (press Enter to continue)")
            if self.__finished:
                input("Thanks for using the tool. Bye!")
                return
            start = input("start (press Enter to continue): ")
            if not start or start.strip() == "":
                start = self.__prev
            end = input("end (press Enter to continue): ")
            disabled = input("Need disabled accessibility? Y/N (press Enter to continue): ")
            disabled = True if disabled == "Y" else False
            self.navigate(start, end, disabled)
            self.__prev = end
            self.__cnt += 1
            if input("Do you want to continue? Y/N (press Enter to continue): ") == "N":
                self.__finished = True

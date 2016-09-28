
from abc import abstractmethod, ABCMeta


class BaseInventory():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def pre_item_render(self):
        pass

    @abstractmethod
    def item_callback_list(self):
        pass

    def post_item_render(self):
        pass


class MainMenu(BaseInventory):
    def item_callback_list(self):
        return (('Query', QueryMenu),('Exit', self.exit))

    def exit(self):
        print('Exit!')
        exit(0)


class QueryMenu(BaseInventory):
    def item_callback_list(self):
        return (('No due', self.exit),
                ('Pass Due', self.exit),
                ('Have Due', self.exit))

    def exit(self):
        pass

class MenuOperator:
    def __init__(self, menu):
        self.history_stack = []
        self.menu_instance = menu()
        self.print_menu()
        self.process_input()

    def invoke_menu(self, menu, key):
        pass

    def process_input(self):
        pass

    def print_menu(self):
        item_index = 0
        for item in self.menu_instance.item_callback_list():
            print('({}) {}'.format(item_index, item[0]))
            item_index += 1




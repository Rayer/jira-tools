
from abc import abstractmethod, ABCMeta
import inspect


class BaseInventory:
    __metaclass__ = ABCMeta

    def __init__(self, context):
        self.context = context

    def pre_item_render(self):
        pass

    @abstractmethod
    def item_callback_list(self):
        pass

    def post_item_render(self):
        pass

    def exit(self):
        print('Exit!')
        exit(0)

    def back_previous(self):
        self.context.back_previous()


class MainMenu(BaseInventory):
    def __init__(self, context):
        super().__init__(context)

    def item_callback_list(self):
        return [('Query', QueryMenu),
                ('Bucket Operation', BucketMenu),
                ('Change User', self.change_id),
                ('Generate Weekly Report', self.generate_report)]

    def change_id(self):
        pass

    def generate_report(self):
        pass


class QueryMenu(BaseInventory):
    def __init__(self, context):
        super().__init__(context)

    def item_callback_list(self):
        return [('No due', self.exit),
                ('Pass Due', self.exit),
                ('Have Due', self.exit)]

    def exit(self):
        pass


class BucketMenu(BaseInventory):
    def __init__(self, context):
        super().__init__(context)

    def item_callback_list(self):
        return [('Add issue to bucket', self.add_to_bucket),
                ('Remove issue from bucket', self.remove_from_bucket),
                ('Remove all issues in bucket', self.remove_all_bucket)]

    def add_to_bucket(self):
        pass

    def remove_from_bucket(self):
        pass

    def remove_all_bucket(self):
        pass


class MenuOperator:
    def __init__(self, menu, jira):
        self.history_stack = []
        self.history_stack.append(menu(self))
        self.bucket = []
        self.root = self.current_menu()
        self.jira = jira
        self.loop()

    def loop(self):
        while True:
            item_list = self.generate_item_list(self.current_menu())
            item_callback = self.generate_item_callback(self.current_menu())
            self.print_menu(item_list)
            self.print_bucket()
            self.print_user()
            index = int(input('Select : '))
            callback = item_callback[index]
            print(type(callback))
            if inspect.isclass(callback):
                self.history_stack.append(callback(self))
                continue

            if callable(callback):
                callback()
                continue

    def current_menu(self):
        return self.history_stack[-1]

    def back_previous(self):
        self.history_stack.pop()

    def invoke_menu(self, menu, key):
        pass

    def process_input(self):
        pass

    def print_menu(self, menu_list):
        item_index = 0
        for item in menu_list:
            print('({}) {}'.format(item_index, item[0]))
            item_index += 1

    def print_bucket(self):
        pass

    def print_user(self):
        pass

    def generate_item_list(self, menu):
        item_list = menu.item_callback_list()
        item_list.insert(0, ('Exit', self.current_menu().exit) if self.current_menu() == self.root else (
            'Back to previous menu', self.current_menu().back_previous))
        return item_list

    def generate_item_callback(self, menu):
        return [x[1] for x in self.generate_item_list(menu)]




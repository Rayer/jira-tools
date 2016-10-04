
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

    def print_bugs(self, bugs):
        for jira_entry in bugs['issues']:
            print('{} : {}({})'.format(jira_entry['key'], jira_entry['fields']['summary'],
                                       jira_entry['fields']['duedate']))

    def print_single_bug(self, bug):
        pass


class MainMenu(BaseInventory):
    def __init__(self, context):
        super(MainMenu, self).__init__(context)

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
        super(QueryMenu, self).__init__(context)

    def item_callback_list(self):
        return [('No due', self.no_due),
                ('Pass Due',self.pass_due),
                ('Have Due', self.have_due)]

    def no_due(self):
        self.print_bugs(self.context.jira.no_due())

    def pass_due(self):
        self.print_bugs(self.context.jira.pass_due())

    def have_due(self):
        self.print_bugs(self.context.jira.have_due())

    def exit(self):
        pass


class BucketMenu(BaseInventory):
    def __init__(self, context):
        super(BucketMenu, self).__init__(context)

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





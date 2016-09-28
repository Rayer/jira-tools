#!/usr/bin/python3
from jira import JiraAdaptor
import sys
import Menu

#For Python 2.7 compitible
try: input = raw_input
except NameError: pass

def print_bugs(bugs):
    for jira_entry in bugs['issues']:
        print('{} : {}({})'.format(jira_entry['key'], jira_entry['fields']['summary'], jira_entry['fields']['duedate']))


if __name__ == '__main__':
    bucket = set()
    acc = sys.argv[1] if sys.argv.__len__() >= 2 is not None else input('Account name : ')
    password = sys.argv[2] if sys.argv.__len__() >= 2 is not None else input('password : ')

    # j = JiraAdaptor(acc, password)
    m = Menu.MenuOperator(Menu.MainMenu)


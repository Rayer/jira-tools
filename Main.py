#!/usr/bin/python3
from jira import JiraAdaptor
import sys
import BaseInventory

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

    j = JiraAdaptor(acc, password)
    print('Successfully logged in as user : {}'.format(acc))

    print('have due             -------')
    print_bugs(j.have_due())
    print('no due               -------')
    print_bugs(j.no_due())
    print('pass due             -------')
    print_bugs(j.pass_due())
    print('Recently Resolved    -------')
    print_bugs(j.recently_resolved())
import requests
import sys


class JiraAdaptor:

    base_login_url = 'https://{}:{}@jira.ruckuswireless.com'
    base_jira_url = 'https://jira.ruckuswireless.com/rest/api/latest/{}'

    def __init__(self, user, password):
        self.session = requests.session()
        self.user = user
        self.password = password
        self.login()

    def login(self):
        result = self.session.get(self.base_login_url.format(self.user, self.password))
        if result.status_code == 522:
            raise BaseException('Jira seems down now, please try again later.')
        if result.status_code != 200:
            raise PermissionError('Not able to login Jira, please check Account and Password.')
        return result

    def raw_search(self, jql_query):
        query_url = self.base_jira_url.format('search?jql=' + jql_query)
        print('Querying : {}'.format(query_url))
        return self.session.get(query_url).json()

    def not_resolved_me(self, additional_jql=''):
        return self.raw_search('assignee={} AND resolution=unresolved '.format(self.user) + additional_jql)

    def no_due(self, additional_jql = ''):
        return self.not_resolved_me('AND duedate is EMPTY ' + additional_jql)

    def have_due(self, additional_jql=''):
        return self.not_resolved_me('AND duedate is not EMPTY ' + additional_jql)

    def pass_due(self, additional_jql=''):
        return self.not_resolved_me('AND duedate <= now() ' + additional_jql)

    def gen_weekly_report(self):
        issues = self.raw_search('')
        pass

    def recently_resolved(self, additional_jql=''):
        return self.raw_search('assignee={} AND resolutiondate >=-1w'.format(self.user))


def print_bugs(bugs):
    for jira_entry in bugs['issues']:
        print('{} : {}({})'.format(jira_entry['key'], jira_entry['fields']['summary'], jira_entry['fields']['duedate']))

def main():
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


if __name__ == '__main__':
    main()





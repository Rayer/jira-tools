import requests
import sys


class JiraAdaptor:

    debug = True
    base_login_url = 'https://{}:{}@jira.ruckuswireless.com'
    base_jira_url = 'https://jira.ruckuswireless.com/rest/api/latest/{}'

    def __init__(self, user, password):
        self.session = requests.session()
        self.user = user
        self.password = password
        self.login()

    def debug_print(self, string):
        if self.debug is True:
            print(string)

    def login(self):
        result = self.session.get(self.base_login_url.format(self.user, self.password))
        if result.status_code == 522:
            raise BaseException('Jira seems down now, please try again later.')
        if result.status_code != 200:
            raise PermissionError('Not able to login Jira, please check Account and Password.')
        return result

    def raw_search(self, jql_query):
        return self.raw_request('GET', 'search?jql=' + jql_query)

    def raw_request(self, request_type, cmd):
        url = self.base_jira_url.format(cmd)
        self.debug_print('({}){}'.format(request_type, url))
        return self.session.request(request_type, url).json()

    def not_resolved_me(self, additional_jql=''):
        return self.raw_search('assignee={} AND resolution=unresolved '.format(self.user) + additional_jql)

    def no_due(self, additional_jql = ''):
        return self.not_resolved_me('AND duedate is EMPTY ' + additional_jql)

    def have_due(self, additional_jql=''):
        return self.not_resolved_me('AND duedate is not EMPTY ' + additional_jql)

    def pass_due(self, additional_jql=''):
        return self.not_resolved_me('AND duedate <= now() ' + additional_jql)

    def have_commented(self, days=7, additional_jql=''):
        return self.raw_search('assignee = {id} AND updated >= -{days}d AND issuefunction in commented("by {id}") '.format(id=self.user, days=days) + additional_jql)

    def recently_resolved(self, days = 7, additional_jql=''):
        return self.raw_search('assignee={} AND resolutiondate >=-{}d'.format(self.user, days))

    def get_issue(self, issue_id):
        return self.raw_request('GET', 'issue/{}'.format(issue_id))








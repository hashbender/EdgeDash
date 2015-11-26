from dashing.widgets import NumberWidget
import requests
import time
import lxml.html as lh
import random
from django.contrib.auth.decorators import login_required

class WorkToClientWidget(NumberWidget):
    title = 'Work Sent To Client'
    more_info = "Last Updated: " + time.strftime('%c')
    todaysDate = time.strftime("%m/%d/%Y")

    def get_title(self):
        print "WorkToClientWidget title"
        return self.title

    def get_more_info(self):
        more_info = "Last Updated: " + time.strftime('%c')
        return self.more_info

    def get_updated_at(self):
        return self.updated_at

    def get_detail(self):
        return self.detail

    def get_value(self):
        print "Starting to get values"
        #self.value = random.random()
        more_info = "Last Updated: " + time.strftime('%c')
        site = 'https://www.propertypreswizard.com/control.php/login/login/?event=verify'
        reportSite = 'https://www.propertypreswizard.com/control.php/report/invoice_client_test/'
        runReportUrl = 'https://www.propertypreswizard.com/control.php/report/invoice_client_test/?event=processFields'

        values = {
            'username' : os.environ['PWW_USERNAME'],
            'password' : os.environ['PWW_PASSWORD']}
        print "Posting"
        session = requests.Session()
        resp = session.post(site,data=values)
        print "Done authorizing"

        resp = session.get(reportSite)
        print "Running report for today's date: " + self.todaysDate
        values = {'submit_to_bank_start' : self.todaysDate,
           'show_contractor_total' : '1',
            'invoice_saved' : '1',
            'invoice_complete' : '1',
            'show_client_total' : '1',
            'chargeback_processed' : '0',
            'run' : 'Run Report',
            'export' : '0'
        }

        resp = session.post(runReportUrl, values)
        doc = lh.fromstring(resp.text)
        grandTotal = doc.xpath('//*[@id="tblResults"]/tr[last()-1]/td[7]/text()')

        print "Total work sent to client on " + self.todaysDate + ": " + grandTotal[0]
        self.value = grandTotal[0]
        return self.value

    def get_context(self):
        return {
            'title': self.get_title(),
            'moreInfo': self.get_more_info(),
            'updatedAt': self.get_updated_at(),
            'detail': self.get_detail(),
            'value': self.get_value(),
        }

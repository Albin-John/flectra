import flectra.tests


class TestUi(flectra.tests.HttpCase):

    post_install = True
    at_install = False

    def test_admin(self):
        # Seen that:
        # - this test relies on demo data that are entirely in USD (pricelists)
        # - that main demo company is gelocated in US
        # - that this test awaits for hardcoded USDs amount
        # we have to force company currency as USDs only for this test
        self.env.ref('base.main_company').write({'currency_id': self.env.ref('base.USD').id})
        self.phantom_js("/", "flectra.__DEBUG__.services['web_tour.tour'].run('event_buy_tickets')", "flectra.__DEBUG__.services['web_tour.tour'].tours.event_buy_tickets.ready", login="admin")

    def test_demo(self):
        self.phantom_js("/", "flectra.__DEBUG__.services['web_tour.tour'].run('event_buy_tickets')", "flectra.__DEBUG__.services['web_tour.tour'].tours.event_buy_tickets.ready", login="demo")

    # TO DO - add public test with new address when convert to web.tour format.

import pytest
from model.contact import Contact
from fixture.application import  Application

@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture


def setUp(self):
    self.app = Application()


def test_add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_add_contact_page()
    app.contact.create(Contact(name="pyt", last_name="pyt", company_name="pyt", address="pyt", mail="pyt@pyt.py"))
    app.session.logout()


import pytest
from model.group import Group
from fixture.application import  Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def setUp(self):
    self.app = Application()


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.init_group_creation()
    app.create_group(Group(name="pyt", header="pyt", footer="pyt"))
    app.logout()

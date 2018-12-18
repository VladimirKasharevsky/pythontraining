from model.group import Group


def test_add_group(app):
    app.group.open_group_page()
    app.group.init_group_creation()
    app.group.create(Group(name="pyt", header="pyt", footer="pyt"))
   # app.session.logout()

def test_add_empty_group(app):
    app.group.open_group_page()
    app.group.init_group_creation()
    app.group.create(Group(name="", header="", footer=""))

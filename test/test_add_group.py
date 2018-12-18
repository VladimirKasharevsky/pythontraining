from model.group import Group


def test_add_group(app):
    app.group.open_group_page()
    app.group.init_group_creation()
    app.group.create(Group(name="pyt", header="pyt", footer="pyt"))

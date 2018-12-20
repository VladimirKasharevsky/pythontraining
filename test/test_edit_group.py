from model.group import Group


def test_edit_firs_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.select_edited_group()
    app.group.edit(Group(name="pytedit", header="pytedit", footer="pytedit"))

def test_edit_first_grop_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.select_edited_group()
    app.group.modify_first_group(Group(name="New group"))

def test_edit_first_grop_header(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.select_edited_group()
    app.group.modify_first_group(Group(header="New header"))
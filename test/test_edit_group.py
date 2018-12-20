from model.group import Group


def test_edit_firs_group(app):
    app.group.select_edited_group()
    app.group.edit(Group(name="pytedit", header="pytedit", footer="pytedit"))

def test_edit_first_grop_name(app):
    app.group.select_edited_group()
    app.group.modify_first_group(Group(name="New group"))

def test_edit_first_grop_header(app):
    app.group.select_edited_group()
    app.group.modify_first_group(Group(header="New header"))
from model.group import Group


def test_edit_firs_group(app):
    app.group.select_edited_group()
    app.group.edit(Group(name="pytedit", header="pytedit", footer="pytedit"))
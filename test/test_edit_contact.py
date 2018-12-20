from model.contact import Contact


def test_add_contacts(app):
    if app.contact.count()==0:
        app.contact.open_add_contact_page()
        app.contact.create(Contact(name="py", last_name="py", company_name="py", address="py", mail="py@py.py"))
    app.contact.edit_first_contact()
    app.contact.edit(Contact(name="pytedit", last_name="pytedit", company_name="pytedit", address="pytedit", mail="pytedit@pytedit.py"))
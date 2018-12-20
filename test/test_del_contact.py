from model.contact import Contact

def test_del_contacts(app):
    if app.contact.count()==0:
        app.contact.open_add_contact_page()
        app.contact.create(Contact(name="py", last_name="py", company_name="py", address="py", mail="py@py.py"))
    app.contact.delete_first_contact()
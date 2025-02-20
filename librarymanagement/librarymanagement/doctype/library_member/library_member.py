import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class LibraryMember(Document):
    def before_save(self):
        """Generate full name and naming series before saving."""
        self.full_name = f"{self.first_name} {self.last_name or ''}"


@frappe.whitelist()
def get_naming_series(library_member):
    """Generates the next available naming series with auto-increment."""
    if not library_member:
        return "LIB"  

    prefix = f"{library_member[:3].upper()}-"  

    last_entry = frappe.db.sql(f"""
        SELECT name FROM `tabLibrary Member`
        WHERE library_member = '{library_member}'  
        ORDER BY creation DESC
        LIMIT 1
    """, as_dict=True)

    if last_entry:
        last_number = int(last_entry[0]["name"].split('-')[-1])
        last_number += 1 
    else:
        last_number = 1  

    print('last_number', last_number)
    print('Prefix', prefix)

    return f"{prefix}{last_number}" 

@frappe.whitelist()
def receive_post_data():
    data = frappe.request.data
    print("data", data)
    return

 # def before_insert(self):
    #     if not self.name:
    #         self.name = make_autoname("LIBM-.YYYY.-.####")

 # last_name = frappe.db.sql('''
            #     SELECT name FROM `tabLibrary Member` 
            #     WHERE name LIKE %s 
            #     ORDER BY creation DESC LIMIT 1
            # ''', (f"{self.naming_series[:5]}%",))

# @frappe.whitelist()
# def custom_button_action(docname):
#     doc = frappe.get_doc("Library Member", docname)
#     frappe.msgprint(f"Button clicked for {doc.full_name}")
#     return "Success"	

# @frappe.whitelist()
# def get_naming_series_by_library(library_name):
#     get_library_member = frappe.get_all('Library Member', filters={'library_member': library_name}, fields=['naming_series'])
#     print('get_library_member', get_library_member)
#     if get_library_member:
#         return get_library_member[0]['naming_series']
#     else:
#         return None

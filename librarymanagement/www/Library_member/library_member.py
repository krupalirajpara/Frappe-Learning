import frappe

def get_context(context):
    context.librarys = frappe.get_all("Library", fields=["library_name"])

    context.library_member = frappe.get_all("Library Member", fields=["*"])

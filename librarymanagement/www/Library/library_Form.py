import frappe

def get_context(context):
    context.token = frappe.sessions.get_csrf_token()


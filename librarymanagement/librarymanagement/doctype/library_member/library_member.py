# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	def before_save(self):
 		self.full_name = f'''{self.first_name} {self.last_name or ""}'''

# @frappe.whitelist()
# def custom_button_action(docname):
#     doc = frappe.get_doc("Library Member", docname)
#     frappe.msgprint(f"Button clicked for {doc.full_name}")
#     return "Success"	

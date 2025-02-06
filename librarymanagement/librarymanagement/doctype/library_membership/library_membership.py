# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils import nowdate
from frappe import _

class LibraryMembership(Document):
	# data can't be saved 
    # def validate(self):
    #     self.check_active_membership()

    # def before_submit(self):
    #     self.check_active_membership()

    # data can't be submit
    def before_submit(self):
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "active_membership": "Active",
            },
        )

        if valid_membership:
            frappe.throw(_(f"{self.library_member} has an already active membership!"))

def set_status():
    today_date = nowdate()
    print('today_date:', today_date)

    check_membership = frappe.get_all("Library Membership",
        filters={
            "docstatus": DocStatus.submitted(),
            "to_date": ("<=", today_date),
            "active_membership": "Active"
        },
        fields=["name"]
	)
    print('check_membership:', check_membership)
    if len(check_membership) != 0:  
         for membership in check_membership:
            try:
                membership_name = membership["name"]
                membership_doc = frappe.get_doc("Library Membership", membership_name)
                # print('membership_docs:', membership_doc.as_dict())
                frappe.db.set_value("Library Membership", membership_name, "active_membership", "Deactive")
                frappe.db.commit()
                # updated_doc = frappe.get_doc("Library Membership", membership_name)
                print("Deactivated membership:", membership_name)
            except Exception as e:
                print(f"Error deactivating {membership_name}: {str(e)}")
                frappe.log_error(f"Error deactivating {membership_name}: {str(e)}", "Library Membership Deactivation")
			
// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Membership", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Library Membership', {
    refresh: function(frm) {
        frm.add_custom_button('Create Transaction', () => {
        frappe.new_doc('Library Transaction', {
        library_member: frm.doc.name
        })
        })
    }
   });
   
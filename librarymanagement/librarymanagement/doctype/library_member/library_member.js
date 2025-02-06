// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Member", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
    frm.add_custom_button('Create Membership', () => {
    frappe.new_doc('Library Membership', {
    library_member: frm.doc.name
    })
    })
    }
});


// frappe.ui.form.on('Library Member', {
//     refresh: function(frm) {
//         frm.add_custom_button(__('Click Me'), function() {
//             frappe.call({
//                 method: "library_management.library_management.doctype.library_member.custom_button_action",
//                 args: { docname: frm.doc.name },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                 }
//             });
//         }).addClass("btn-primary");
//     }
// });
   
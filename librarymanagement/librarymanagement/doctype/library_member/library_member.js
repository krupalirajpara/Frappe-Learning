// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt
frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });
    },

    library_member: function (frm) {  
        if (frm.doc.library_member) {  // Ensure library_member is not empty
            frappe.call({
                method: "librarymanagement.librarymanagement.doctype.library_member.library_member.get_naming_series",
                args: {
                    library_member: frm.doc.library_member
                },
                callback: function (r) {
                    if (r.message) {
                        console.log("Naming Series Updated:", r.message);
                        frm.set_value("naming_series", r.message);
                    }
                }
            });
        } else {
            frm.set_value("naming_series", "LIB");  // Default naming series when empty
        }
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
   
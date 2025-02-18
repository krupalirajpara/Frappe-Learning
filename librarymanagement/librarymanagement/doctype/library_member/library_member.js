// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt
frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });
        ///

        frappe.msgprint("Welcome! Show Login USer Name in console using F12!");
        
        frappe.db.get_value("User", frappe.session.user, "full_name")
            .then(response => console.log(response.message.full_name));

        ///
        frm.add_custom_button(__('Show Data In '), function() {
            let d = new frappe.ui.Dialog({
                title: 'Enter details',
                fields: [
                    {
                        label: 'First Name',
                        fieldname: 'first_name',
                        fieldtype: 'Data'
                    },
                    {
                        label: 'Last Name',
                        fieldname: 'last_name',
                        fieldtype: 'Data'
                    },
                ],
                size: 'small', 
                primary_action_label: 'Submit',
                primary_action(values) {
                    console.log(values);
                    frappe.msgprint(__('Data Show IN Console: ') + 'First Name: ' + values.first_name + ', Last Name: ' + values.last_name);
                    d.hide();
                }
            });
            d.show();
           
        });
    },

    library_member: function (frm) {  
        if (frm.doc.library_member) { 
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
            frm.set_value("naming_series", "LIB"); 
        }
    },
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
   
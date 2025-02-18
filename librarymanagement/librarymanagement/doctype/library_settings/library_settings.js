// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Settings", {
    refresh: function(frm) {
        // using dialog API new_doc
        frm.add_custom_button('Create Library Settings', function() {
            frappe.new_doc('Library Settings', {
                'loan_period': 1,
                'issued_articles_counts': 1,
            });

            frappe.new_doc("Library Settings", {"voucher_type": "Bank Entry"}, doc => {
                doc.posting_date = frappe.datetime.get_today();
                let row = frappe.model.add_child(doc, "accounts");
                row.loan_period = 'Bank - A';
                row.issued_articles_counts = 'USD';
            });

            // frappe.new_doc("Library Settings", {subject: "New Task"});

        });
    },
});

frappe.listview_settings['Library Membership'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Add New Membership', function() {
            frappe.new_doc('Library Membership', {});
        });
    }
};

frappe.ui.form.on("Library Membership", "refresh", function (frm) { console.log("External Script Loaded!"); });

// const doctypes = ['Library Membership', 'Library Member'];

frappe.db.get_list('DocType', {
    fields: ['name']
}).then(records => {
    const doctypes = records.map(record => record.name);
    console.log('Doctype Names:', doctypes);

    doctypes.forEach(doctype => {
        frappe.ui.form.on(doctype, {
            refresh: function(frm) {
                if (frm.is_new()) { 
                    frm.add_custom_button(__('Remove Collapse'), function() {
                        removeCollapse(frm);
                    }).addClass("btn-danger");
                } else {
                    frm.remove_custom_button(__('Remove Collapse'));
                }
            }
        });
    });
});

function removeCollapse(frm) {
    $(".form-section .section-head.collapsible").removeClass("collapsible");
    $(".collapse-indicator").remove();
    $(".form-section").css("display", "block"); 

    let sections = frm.meta.fields.filter(field => field.fieldtype === 'Section Break');

    sections.forEach(section => {
        frappe.call({
            method: "frappe.client.insert",
            args: {
                doc: {
                    doctype: "Property Setter",
                    doc_type: frm.doctype,
                    field_name: section.fieldname,
                    property: "collapsible",
                    value: "0", 
                    property_type: "Check",
                    apply_to: "Section Break",
                    doctype_or_field: "DocField"
                }
            },
            callback: function(response) {
                if (!response.exc) {
                    console.log(`Collapse permanently removed for section: ${section.label}`);
                } else {
                    console.log(`Error removing collapse for section: ${section.label}`);
                }
            }
        });
        $(`[data-fieldname='${section.fieldname}']`).css("display", "block").show();
    });
    frappe.msgprint("All sections are now permanently expanded.");
}


///
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        console.log('inside sales invoice!')
        if (frm.fields_dict["items"]) {
            frm.fields_dict["items"].grid.wrapper.css("overflow-x", "auto");
        }
    }
});

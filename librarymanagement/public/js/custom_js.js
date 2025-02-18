

// From Dialog API In Library Doctype
frappe.ui.form.on('Library', {
    refresh: function (frm) {

        // frappe.msgprint({
        //     title: __('Notification'),
        //     message: __('Are you sure you want to proceed?'),
        //     primary_action:{
        //         action(values) {
        //             console.log(values);
        //         }
        //     }
        // });

        // frappe.confirm(
        //     'Are you sure you want to proceed?',
        //     () => {
        //         frappe.msgprint(__('You clicked Yes! Performing action'));
        //     },
        //     () => {
        //         frappe.msgprint(__('You clicked No! Action cancelled.'));
        //     }
        // );

        // frappe.warn(
        //     'Are you sure you want to proceed?',
        //     'There are unsaved changes on this page.',
        //     () => {
        //         frappe.msgprint(__('You clicked Continue!'));
        //     },
        //     'Continue',
        //     true 
        // );

        // frappe.show_alert('Hi, you have a new message', 5);

        // frappe.show_alert({
        //     message:__('Hi, you have a new message'),
        //     indicator:'green'
        // }, 5);

        frm.add_custom_button('Set Library Data', function() {
            frappe.new_doc("Library", doc => {
                    doc.library_name = "Name From Dialog API";
                    doc.city = "Ahmd";
                    // doc.posting_date = frappe.datetime.get_today();

                    let row1 = frappe.model.add_child(doc, "article");
                    row1.article_name = 'Dialog API Article 1';
                    row1.description = 'We can fetch data using Dialog API Row 1';
                    
                    let row2 = frappe.model.add_child(doc, "article");
                    row2.article_name = 'Dialog API Article 2';
                    row2.description = 'We can fetch data using Dialog API Row 2';
            });
        });

        frm.add_custom_button('Multi Select From Child', function() {
            new frappe.ui.form.MultiSelectDialog({
                doctype: "Article",
                target: frm.wrapper,
                setters: {
                    status: 'Issued'
                },
                add_filters_group: 1,
                get_query() {
                    return {
                        filters: {
                            docstatus: ['!=', 2]
                        }
                    };
                },
                action(selections) {
                    console.log("Selected Articles:", selections);
                    frappe.new_doc("Library", {}, function(doc) {
                            doc.library_name = "Library Document with Selected Articles";
                            doc.city = "Ahmd";
                            selections.forEach(function(article_name) {
                                    let row = frappe.model.add_child(doc, "article");
                                    row.article_name = article_name;
                            });
                            frm.refresh_field("article");
                    });
                }
            });
        });
        // 
        frm.add_custom_button('Multi Select Dialog 123', function() {
            new frappe.ui.form.MultiSelectDialog({
                doctype: "Article",  
                target: frm.wrapper,  
                setters: {
                    status: 'Issued' 
                },
                add_filters_group: 1, 
                get_query() {
                    return {
                        query: "librarymanagement.librarymanagement.doctype.library.library.get_articles", 
                        filters: {
                            docstatus: ['!=', 2], 
                        }
                    };
                },
                action(selections) {
                    console.log("Selected Articles:", selections);
        
                    // Create a new Library document
                    frappe.new_doc("Library", {}, function(doc) {
                        doc.library_name = "Library Document with Selected Articles";
                        doc.city = "Ahmd";  // Example additional field
        
                        // Loop through selected Articles and add them to the Library as child rows
                        selections.forEach(function(article) {
                            let row = frappe.model.add_child(doc, "article");  // Add child row to the "article" table
                            row.article_name = article.name;  // Use the Article name as the child field value
                            row.description = article.description || "No description available";  // Use description
                        });
        
                        // Refresh the child table field to reflect new rows
                        frm.refresh_field("article");
                    });
                }
            });
        });
    //     
    frm.add_custom_button('Grid Table', function() {
            let dialog = new frappe.ui.Dialog({
                title: 'Add Multiple People',
                fields: [
                    {
                        fieldname: 'article',
                        fieldtype: 'Table',
                        label: 'Article',
                        fields: [
                            {
                                fieldtype: 'Data',
                                fieldname: 'article_name',
                                label: 'Article Name',
                                in_list_view: 1
                            },
                            {
                                fieldtype: 'Data',
                                fieldname: 'description',
                                label: 'Description',
                                in_list_view: 1
                            },
                        ],
                        data: [],
                        get_data: function() {
                            return this.data;
                        }
                    }
                ],
                primary_action_label: 'Add to Gate Pass',
                primary_action: function() {
                    let data = dialog.get_values().article;
                    if (data && data.length > 0) {
                        data.forEach(row => {
                            let child = frm.add_child('article');
                            child.article_name = row.article_name;
                            child.description = row.last_name;
                        });
                        frm.refresh_field('article');
                    }
                    dialog.hide();
                }
            });
            // Show the dialog
            dialog.show();
        });    
    }
});


// frappe.ui.form.on('Library Membership', {
//     refresh: function(frm) {
//         remove_collapse_behavior(frm);

//         frm.add_custom_button(__('Remove Collapse Permanently'), function() {
//             remove_collapse_behavior(frm);
//             frappe.msgprint(__('Collapse permanently removed!'));
//         });
//     }
// });

// function remove_collapse_behavior(frm) {
//     var collapsibleSections = frm.$wrapper.find('.section-head.collapsible');
//     if (collapsibleSections.length) {
//         collapsibleSections.each(function() {
//             var sectionBody = $(this).next('.section-body');
//             var collapseIndicator = $(this).find('.collapse-indicator');
//             sectionBody.removeClass('collapse').removeClass('collapsed').show();
//             collapseIndicator.removeClass('collapsed');
//             $(this).removeClass('collapsible');
//             $(this).off('click'); 
//             sectionBody.removeAttr('style');
//         });
//     }
// }


frappe.ui.form.on("Library Membership", "refresh", function (frm) { console.log("External JS!"); });

// const doctypes = ["Library Membership"]; 

// doctypes.forEach(dt => {
//     frappe.ui.form.on(dt, {
//         refresh: function (frm) {
//             if (!frm.__islocal) {
//                 if (!frm.custom_buttons["Remove Collapse"]) {
//                     frm.add_custom_button("Remove Collapse", function () {
//                         remove_collapse_sections(frm);
//                     }).addClass("btn-danger");
//                 }
//             }
//         }
//     });
// });

// function remove_collapse_sections(frm) {
//     frappe.confirm("Are you sure you want to remove all collapsible sections permanently?", () => {
//         setTimeout(() => {
//             // Remove collapsible class from all sections
//             document.querySelectorAll(".section-head.collapsible").forEach(el => {
//                 el.classList.remove("collapsible");
//             });

//             // Generate Property Setters dynamically
//             create_property_setters(frm);
            
//             frappe.msgprint("All collapsible sections have been removed permanently.");
//         }, 500);
//     });
// }

// function create_property_setters(frm) {
//     const doctype = frm.doctype;

//     frappe.call({
//         method: "frappe.client.get_list",
//         args: {
//             doctype: "Custom Field",
//             filters: { dt: doctype, fieldtype: "Section Break" },
//             fields: ["name", "label"]
//         },
//         callback: function (response) {
//             if (response.message) {
//                 response.message.forEach(section => {
//                     frappe.call({
//                         method: "frappe.client.insert",
//                         args: {
//                             doc: {
//                                 doctype: "Property Setter",
//                                 doc_type: doctype,
//                                 field_name: section.label,
//                                 property: "collapsible",
//                                 value: "0",
//                                 property_type: "Check"
//                             }
//                         },
//                         callback: function (res) {
//                             if (res.message) {
//                                 console.log(`Removed collapse for section: ${section.label}`);
//                             }
//                         }
//                     });
//                 });
//             }
//         }
//     });
// }


# import frappe

# @frappe.whitelist()
# def remove_collapse_from_sections(doctypes=None):
#     """
#     Remove collapsible property from Section Break fields for selected DocTypes.
#     If no doctypes are provided, fetch all relevant ones.
#     """

#     # If no doctypes provided, fetch all doctypes under 'Library Management' module
#     if not doctypes:
#         doctypes = frappe.get_all("DocType", 
#             filters={"module": "Library Management"},
#             pluck="name"
#         )

#     if isinstance(doctypes, str):
#         doctypes = frappe.parse_json(doctypes)  # Ensure it's a list if coming from JS

#     for doctype in doctypes:
#         # Get all Section Break fields for the given Doctype
#         section_breaks = frappe.get_all("DocField", 
#             filters={"parent": doctype, "fieldtype": "Section Break"},
#             fields=["fieldname"]
#         )

#         for section in section_breaks:
#             if section.get("fieldname"):
#                 # Check if Property Setter already exists
#                 exists = frappe.db.exists("Property Setter", {
#                     "doc_type": doctype,
#                     "field_name": section["fieldname"],
#                     "property": "collapsible"
#                 })

#                 if not exists:
#                     # Create Property Setter to disable collapsibility
#                     property_setter = frappe.get_doc({
#                         "doctype": "Property Setter",
#                         "doctype_or_field": "DocField",
#                         "doc_type": doctype,
#                         "field_name": section["fieldname"],
#                         "property": "collapsible",
#                         "value": 0,  # Set collapsible to False (0)
#                         "property_type": "Check"
#                     })
#                     property_setter.insert(ignore_permissions=True)

#     frappe.msgprint("Collapsible sections removed for selected DocTypes. Please refresh.")

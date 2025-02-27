# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe import whitelist
from frappe.website.website_generator import WebsiteGenerator


class Library(WebsiteGenerator):
	pass

@frappe.whitelist()
def get_articles():
    articles = frappe.get_all(
        'Article',
        fields=["article_name", "description"],
    )
    return articles

# used in www from 
@frappe.whitelist(allow_guest=True)
def get_city(city_name):
    library_data = frappe.db.get_value(
        'Library',city_name, "address"
    )
    return library_data

# def publish_data():
#     data = {
#         'label': 1,
#         'points': [10]
#     }
#     frappe.publish_realtime('test_event', data)

# not need to mention in hooks when create API
@whitelist(allow_guest=True)
def get_public_data():
    articles = frappe.get_all(
        'Article',
        fields=["article_name", "description"], 
    )
    return articles

@whitelist(allow_guest=True)
def post_public_data():
    try:
        doc = frappe.get_doc({
            "doctype": "Library",  
            "library_name": 'IT library',
            "city": 'ahmedabad',
            "address": '308, ship corporate park',
        })
        doc.insert(ignore_permissions=True) 
        frappe.db.commit() 
        return {"success": True, "message": "Library entry added successfully", "data": doc.name}
    except Exception as e:
        return {"success": False, "error": str(e)}

@whitelist(allow_guest=True) 
def post_public_data_from_API():
    try:
        data = frappe.request.json  
        doc = frappe.get_doc({
            "doctype": "Library",  
            "library_name": data.get("library_name"),
            "city": data.get("city"),
            "address": data.get("address"),
        })
        doc.save(ignore_permissions=True)  
        frappe.db.commit()  
        return {"success": True, "message": "Library entry added successfully", "data": doc.name}
    except Exception as e:
        return {"success": False, "error": str(e)}

@frappe.whitelist(allow_guest=True)  
def delete_library_entry():
    try:
        data = frappe.request.json  
        if not data.get("name"):
            return {"success": False, "error": "Missing 'name' parameter"}
        if not frappe.db.exists("Library", data.get("name")):
            return {"success": False, "error": "Library entry not found"}
        frappe.delete_doc("Library", data.get("name"), ignore_permissions=True)  # Bypass permissions
        frappe.db.commit()  
        return {"success": True, "message": "Library entry deleted successfully", "data": data.get("name")}
    except Exception as e:
        return {"success": False, "error": str(e)}

@frappe.whitelist()  
def delete_library_entry_Private_API():
    try:
        data = frappe.request.json  
        if not data.get("name"):
            return {"success": False, "error": "Missing 'name' parameter"}
        if not frappe.db.exists("Library", data.get("name")):
            return {"success": False, "error": "Library entry not found"}
        frappe.delete_doc("Library", data.get("name"))
        frappe.db.commit()  
        return {"success": True, "message": "Library entry deleted successfully", "data": data.get("name")}
    except Exception as e:
        return {"success": False, "error": str(e)}

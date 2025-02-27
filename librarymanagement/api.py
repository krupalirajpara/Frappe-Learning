import frappe
import json

@frappe.whitelist(allow_guest=True)
def receive_data():
    try:
        data = frappe.request.get_data()
        frappe.log_error("Data Received", "API Debug") 

        data = json.loads(data)  
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        is_student = data.get("is_student")

        doc = frappe.get_doc({
            "doctype": "API Doctype",  
            "first_name": first_name,
            "last_name": last_name,
            "is_student": is_student
        })
        doc.insert(ignore_permissions=True) 
        frappe.db.commit()
        frappe.log_error(f"Data Inserted: {doc.name}", "API Debug")  
        return {"status": "success", "message": "Data added successfully!"}
    
    except Exception as e:
        frappe.log_error(f"Error in receive_data: {str(e)}", "API Error")
        return {"status": "error", "message": str(e)}

# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document

class APIIntegration(Document):
    def after_insert(self): 
        send_data_to_api(self)

def send_data_to_api(doc):
    try:
        data = {
            "first_name": doc.first_name,
            "last_name": doc.last_name,
            # "gender": doc.gender,
			"is_student": doc.is_student,
        }
        response = requests.post(
            "http://192.168.2.127:8007/api/method/librarymanagement.api.receive_data",
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        if response.status_code == 200:
            frappe.msgprint("Data successfully sent to API.")
        else:
            frappe.msgprint(f"API Error: {response.text}")
    except Exception as e:
        frappe.log_error(f"Error sending data: {str(e)}", "API Error! ")

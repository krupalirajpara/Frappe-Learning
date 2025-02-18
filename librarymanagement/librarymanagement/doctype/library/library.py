# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Library(WebsiteGenerator):
	pass

@frappe.whitelist()
def get_articles():
    # Query the Article doctype with the provided filters
    articles = frappe.get_all(
        'Article',
        fields=["article_name", "description"],  # Add other fields as needed
       
    )
    return articles

def publish_data():
    data = {
        'label': 1,
        'points': [10]
    }
    frappe.publish_realtime('test_event', data)

// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt

frappe.query_reports["Member Script Report"] = {
	"filters": [
		{
			'fieldname': 'library_member',
			'label': 'Member Name',
			'fieldtype': 'Link',
			'options': 'Library Member',
		},
		{
			'fieldname': 'from_date',
			'label': 'From Date',
			'fieldtype': 'Date',
		},
		{
			'fieldname': 'active_membership',
			'label': 'Active Membership',
			'fieldtype': 'Data',
			// 'options': ['Active', 'Deactive'],
		}
	]
};

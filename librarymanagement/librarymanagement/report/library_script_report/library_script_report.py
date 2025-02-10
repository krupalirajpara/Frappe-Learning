# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
	if not filters: filters = {}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No record found!'))
		return columns, data

	data = []
	for d in cs_data:
		row = frappe._dict({
			'name': d.name,
			'library_name': d.library_name,
			'city': d.city,
		})
		data.append(row)
	chart = get_chart(chart_data)
	return columns, data

def get_columns():
	return[
		{
			'field_name': 'name',
			'label': 'Name', # must be same as a Doctype label 
			'field_type': 'data',
			'width': '120',
		},
		{
			'field_name': 'library_name',
			'label': 'Library Name',
			'field_type': 'data',
			'width': '200',
		},
		{
			'field_name': 'city',
			'label': 'City',
			'field_type': 'data',
			'width': '100',
		}
	]

def get_cs_data(filters):
	condidtions = get_conditions(filters)  # if we want apply filters
	data = frappe.get_all(
		doctype = 'Library',
		fields = ['name', 'library_name', 'city',],
		filters = condidtions,
		order_by = 'name desc'
	)
	return data
	
# for filter data
def get_conditions(filters):
	conditions = {}
	for key, values in filters.items():
		if filters.get(key):
			conditions[key] = values # f"%{value}%" 
	return conditions

# chart
def get_chart(chart_data):
	if not chart_data:
		return None
	
	labels = [age<=45, age>= 45]

	datasets = []
# Copyright (c) 2025, Demo and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.utils import nowdate


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
			# key and value same as doctype field_name
			'full_name': d.full_name,
			'from_date': d.from_date,
			'to_date': d.to_date,
			'active_membership': d.active_membership,
		})
		data.append(row)
	chart = get_chart(data)
	return columns, data, None, chart

def get_columns():
	return[
		{
			'field_name': 'full_name',
			'label': 'Full Name',
			'field_type': 'Data',
			'width': '200',
		},
		{
			'field_name': 'from_date',
			'label': 'From Date',
			'field_type': 'Date',
			'width': '100',
		},
		{
			'field_name': 'to_date',
			'label': 'To Date',
			'field_type': 'Date',
			'width': '100',
		},
		{
			'field_name': 'active_membership',
			'label': 'Active Membership',
			'field_type': 'data',
			'width': '120',
		}
	]

def get_cs_data(filters):
	condidtions = get_conditions(filters)  # if we want apply filters
	data = frappe.get_all(
		doctype = 'Library Membership',
		fields = ['full_name', 'from_date', 'to_date', 'active_membership',],
		filters = condidtions,
		order_by = 'from_date desc'
	)
	return data
	
# conditions for filter data
def get_conditions(filters):
	conditions = {}
	for key, values in filters.items():
		if filters.get(key):
			conditions[key] = values 
	return conditions

# for chart
# def get_chart(data):
# 	today_date = nowdate()
# 	if not data:
# 		return None
	
# 	labels = [f'from_date<={today_date}', f'from_date> {today_date}']

# 	total_person = {
# 		f'from_date<={today_date}': 0,
# 		f'from_date> {today_date}': 0,
# 	}

# 	datasets = []
# 	for d in data:
# 		if d.from_date != '':
# 			if d.from_date <= {today_date}:
# 				total_person[f'from_date<={today_date}'] += 1
# 			else:
# 				total_person[f'from_date>{today_date}'] += 1
# 		else:
# 			pass
# 	datasets.append({
# 		'name': 'Total Person',
# 		'values': [total_person.get(f'from_date<={today_date}'), f'from_date> {today_date}']
# 	})

# 	chart = {
# 		'data': {
# 			'labels': labels,
# 			'datasets': datasets,
# 		},
# 		'type': 'pie',
# 		'height': 300,
# 	}
# 	return chart

# for chart
def get_chart(data):
	today_date = nowdate()
	if not data:
		return None
	
	labels = ['Active', 'Deactive', 'Invalid']

	total_person = {
		'Active': 0,
		'Deactive': 0,
		'Invalid': 0,
	}

	datasets = []
	for d in data:
		if d.active_membership != '':
			if d.active_membership == 'Active':
				total_person['Active'] += 1
			elif d.active_membership == 'Deactive':
				total_person['Deactive'] += 1
			else:
				total_person['Invalid'] += 1
		else:
			pass

	datasets.append({
		'name': 'Total Person',
		'values': [total_person.get('Active'), total_person.get('Deactive'), total_person.get('Invalid')]
	})

	chart = {
		'data': {
			'labels': labels,
			'datasets': datasets,
		},
		'type': 'pie',
		'height': 300,
	}
	return chart


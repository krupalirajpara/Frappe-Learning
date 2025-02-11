frappe.pages['library-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Library Management System',
		single_column: true
	});


	
	page.set_title('Library Management System (For Learning)')
	page.set_indicator('Process', 'red')
	let $primary_btn = page.set_primary_action('New', ()=> frappe.msgprint('Button Clicked!'), 'octicon octicon-plus')
	let $secondary_btn = page.set_secondary_action('Refresh', ()=> frappe.msgprint('Button Clicked!'), 'octicon octicon-plus')
	page.add_menu_item('Send Email', ()=> frappe.msgprint('Send Mail Button Clicked!'))
	page.add_action_item('Delete', ()=> frappe.msgprint('Delete Button Clicked!'))

	let first_name = page.add_field({
		label: 'First Name', 
		fieldtype: 'Data',
		fieldname: 'first_name',
	});
	let last_name = page.add_field({
		label: 'Last Name', 
		fieldtype: 'Data',
		fieldname: 'last_name',
	});
	let select_gender = page.add_field({
		label: 'Gender', 
		fieldtype: 'Select',
		fieldname: 'gender',
		options: ['Male', 'Female', 'Other'],
		change(){
			frappe.msgprint(field.get_value());
		}
	});
	let library_name = page.add_field({
		label: 'Choose Library', 
		fieldtype: 'Link',
		fieldname: 'library_name',
		options: 'Library'
	});
	// $(frappe.render_template("library_page", {})).appendTo(page.body);

	$(frappe.render_template("library_page", {
		data: " Hello"
	})).appendTo(page.body);
}

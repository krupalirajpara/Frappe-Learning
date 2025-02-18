frappe.ready(function() {
	// bind events here
		frappe.web_form.after_load = () => {
		frappe.msgprint('Please fill all values carefully');
	};
	console.log('its loading!')
});

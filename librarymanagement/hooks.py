app_name = "librarymanagement"
app_title = "Librarymanagement"
app_publisher = "Demo"
app_description = "Library Management System"
app_email = "krupali@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "librarymanagement",
# 		"logo": "/assets/librarymanagement/logo.png",
# 		"title": "Librarymanagement",
# 		"route": "/librarymanagement",
# 		"has_permission": "librarymanagement.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/librarymanagement/css/external_css.css"
# app_include_js = "/assets/librarymanagement/js/librarymanagement.js"
# librarymanagement is a app name
app_include_js = ["/assets/librarymanagement/js/remove_collapasble.js"]


# include js, css files in header of web template
# web_include_css = "/assets/librarymanagement/css/librarymanagement.css"
# web_include_js = "/assets/librarymanagement/js/librarymanagement.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "librarymanagement/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
   
# include js in doctype views
doctype_js = { 
    "Library Membership": "public/js/remove_collpase.js"
}
doctype_list_js = {
    # "Library Membership": "public/js/library_membership.js",
    # "Library Member": "public/js/library_membership.js",

    # "*": "public/js/library_membership.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "librarymanagement/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "librarymanagement.utils.jinja_methods",
# 	"filters": "librarymanagement.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "librarymanagement.install.before_install"
# after_install = "librarymanagement.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "librarymanagement.uninstall.before_uninstall"
# after_uninstall = "librarymanagement.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "librarymanagement.utils.before_app_install"
# after_app_install = "librarymanagement.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "librarymanagement.utils.before_app_uninstall"
# after_app_uninstall = "librarymanagement.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "librarymanagement.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"librarymanagement.tasks.all"
# 	],
# 	"daily": [
# 		"librarymanagement.tasks.daily"
# 	],
# 	"hourly": [
# 		"librarymanagement.tasks.hourly"
# 	],
# 	"weekly": [
# 		"librarymanagement.tasks.weekly"
# 	],
# 	"monthly": [
# 		"librarymanagement.tasks.monthly"
# 	],
    "cron": {
            "* * * * *":[
            "librarymanagement.librarymanagement.doctype.library_membership.library_membership.set_status"  
            ]
        }
}

# Testing
# -------

# before_tests = "librarymanagement.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "librarymanagement.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "librarymanagement.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["librarymanagement.utils.before_request"]
# after_request = ["librarymanagement.utils.after_request"]

# Job Events
# ----------
# before_job = ["librarymanagement.utils.before_job"]
# after_job = ["librarymanagement.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"librarymanagement.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

after_migrate = "librarymanagement.utils.remove_collapse_from_sections" 

# Copyright (c) 2026, Innosphereconsulting and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.naming import make_autoname


def autoname(doc, method=None):
	"""Name the Purchase Order from its Order Category's Purchase Order series

	Without a category Frappe falls back to the standard naming series.
	Amended POs are named from the original PO by Frappe before this runs.
	"""
	if not doc.get("custom_order_category"):
		return

	series = frappe.db.get_value(
		"Naming Category Series",
		{
			"parenttype": "Naming Category",
			"parent": doc.custom_order_category,
			"document_type": "Purchase Order",
		},
		"series",
	)
	if not series:
		frappe.throw(
			_("Naming Category {0} has no series for Purchase Order. Add it in the Naming Category.").format(
				frappe.bold(doc.custom_order_category)
			)
		)

	doc.naming_series = series
	doc.name = make_autoname(series, doc=doc)

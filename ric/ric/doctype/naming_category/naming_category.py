# Copyright (c) 2026, Innosphereconsulting and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class NamingCategory(Document):
	def validate(self):
		seen_doctypes = set()
		for row in self.series_details:
			row.series = "".join((row.series or "").split())

			if row.document_type in seen_doctypes:
				frappe.throw(
					_("Row {0}: {1} already has a series in this category.").format(
						row.idx, frappe.bold(row.document_type)
					)
				)
			seen_doctypes.add(row.document_type)

			if "#" not in row.series:
				frappe.throw(
					_("Row {0}: Series {1} must contain # for the running number, e.g. PO-TRD-.YYYY.-.#####").format(
						row.idx, frappe.bold(row.series)
					)
				)

			self.validate_unique_series(row)

	def validate_unique_series(self, row):
		"""Two rows sharing a series would share one counter."""
		for other in self.series_details:
			if other.idx != row.idx and other.series == row.series:
				frappe.throw(
					_("Row {0}: Series {1} is repeated in row {2}.").format(
						row.idx, frappe.bold(row.series), other.idx
					)
				)

		used_by = frappe.db.get_value(
			"Naming Category Series",
			{"series": row.series, "parenttype": "Naming Category", "parent": ["!=", self.name]},
			"parent",
		)
		if used_by:
			frappe.throw(
				_("Row {0}: Series {1} is already used by Naming Category {2}.").format(
					row.idx, frappe.bold(row.series), frappe.bold(used_by)
				)
			)

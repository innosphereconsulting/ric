// Copyright (c) 2026, Innosphereconsulting and contributors
// For license information, please see license.txt

// The SO name comes from the Order Category's Sales Order series (set on the server),
// so the Series field is hidden while a category is selected.
frappe.ui.form.on("Sales Order", {
	setup(frm) {
		frm.set_query("custom_order_category", () => ({
			filters: [["Naming Category Series", "document_type", "=", "Sales Order"]],
		}));
	},

	refresh(frm) {
		toggle_so_series(frm);
	},

	custom_order_category(frm) {
		toggle_so_series(frm);
	},
});

function toggle_so_series(frm) {
	frm.toggle_display("naming_series", !frm.doc.custom_order_category);
}

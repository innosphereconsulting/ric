// Copyright (c) 2026, Innosphereconsulting and contributors
// For license information, please see license.txt

// The PO name comes from the Order Category's Purchase Order series (set on the server),
// so the Series field is hidden while a category is selected.
frappe.ui.form.on("Purchase Order", {
	setup(frm) {
		frm.set_query("custom_order_category", () => ({
			filters: [["Naming Category Series", "document_type", "=", "Purchase Order"]],
		}));
	},

	refresh(frm) {
		toggle_po_series(frm);
	},

	custom_order_category(frm) {
		toggle_po_series(frm);
	},
});

function toggle_po_series(frm) {
	frm.toggle_display("naming_series", !frm.doc.custom_order_category);
}

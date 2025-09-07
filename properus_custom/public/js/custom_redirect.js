frappe.router.on('change', () => {
    // kalau route ke workspace Pengeluaran
    if (frappe.get_route()[0] === "workspace" && frappe.get_route()[1] === "Testing") {
        frappe.set_route("Form", "Pengeluaran Barang", "new");
    }
});

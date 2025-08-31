frappe.router.on("change", (route) => {
    if (route[0] === "pemasukan") {
        frappe.set_route("List", "Pemasukan Barang");
    }
});

import frappe

@frappe.whitelist()
def save_jenis_dokumen(nama_jenis_dokumen):
    doc = frappe.get_doc({
        "doctype": "Jenis Dokumen",  # pastikan Doctype sudah ada
        "nama_jenis_dokumen": nama_jenis_dokumen
    })
    doc.insert()
    return "success"

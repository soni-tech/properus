import frappe

@frappe.whitelist()
def get_items_by_purchase_receipt(custom_nomor_dokumen, custom_tanggal_dokumen=None):
    # Ambil Purchase Receipt berdasarkan custom_nomor_dokumen
    pr_list = frappe.get_list(
        'Purchase Receipt',
        filters={'custom_nomor_dokumen': custom_nomor_dokumen},
        fields=['name', 'custom_tanggal_dokumen']
    )
    if not pr_list:
        return []

    pr_name = pr_list[0].name

    # Ambil item_code dari Purchase Receipt Item
    items = frappe.get_list(
        'Purchase Receipt Item',
        filters={'parent': pr_name},
        fields=['item_code']
    )

    item_codes = [i.item_code for i in items]
    if not item_codes:
        return []

    # Ambil Item master sesuai item_code
    item_master = frappe.get_list(
        'Item',
        filters={'item_code': ['in', item_codes]},
        fields=['name', 'item_code', 'item_name']
    )

    return item_master

from frappe import _

def get_data():
    return [
        {
            "module_name": "properus_custom",  # Workspace / Module Name
            "color": "blue",
            "icon": "octicon octicon-package",
            "type": "module",
            "label": _("Testing"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Pemasukan Barang",
                    "label": _("Pemasukan"),
                    "description": _("Form input Pemasukan Barang"),
                    # Ini bikin shortcut langsung buka form baru
                    "link": "/app/pemasukan-barang/new"
                }
            ]
        }
    ]

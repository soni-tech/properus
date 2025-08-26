from frappe import _

def get_data():
    return [
        {
            "module_name": "Pemasukan Custom",
            "category": "Modules",
            "label": _("Pemasukan Custom"),
            "icon": "octicon octicon-plus",   # bebas, ikon opsional
            "type": "module",
            "description": "Menu untuk Pemasukan Custom"
        }
    ]

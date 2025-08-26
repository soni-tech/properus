from frappe import _

def get_data():
    return [
        {
            "module_name": "Pemasukan Custom",
            "category": "Modules",
            "label": _("Stock Entry"),
            "type": "route",
            "route": "/app/stock-entry/new-stock-entry"
        }
    ]

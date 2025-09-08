import frappe
import requests

@frappe.whitelist(allow_guest=True)
def test_httpbin():
    res = requests.post(
        "https://httpbin.org/post",
        json={"hello": "erpnext"}
    )
    return res.json()

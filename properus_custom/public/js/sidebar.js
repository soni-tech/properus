frappe.provide('frappe.desk');

$(document).ready(function () {
    const createSidebarItem = (item) => `
        <div class="sidebar-item-container is-draggable"
             item-parent="${item.categoryName}"
             item-name="${item.label}"
             item-public="1"
             item-is-hidden="0">
            <a href="${item.route}" class="sidebar-label">
                <span class="sidebar-item-icon"><i class="${item.icon}"></i></span>
                <span class="sidebar-item-label">${item.label}</span>
            </a>
        </div>
    `;

    const items = [
        {
            categoryName: "Custom",
            label: "Stock Entry",
            route: "/app/stock-entry/new-stock-entry",
            icon: "fa fa-cube"
        },
        {
            categoryName: "Custom",
            label: "Sales Invoice Report",
            route: "/app/query-report/Sales%20Invoice",
            icon: "fa fa-file-text"
        }
    ];

    items.forEach(item => {
        $(".standard-sidebar").append(createSidebarItem(item));
    });
});

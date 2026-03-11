

def main(request):
    main_pages = 0
    sidebar = 0
    if not request.user.is_anonymous:
        main_pages = {
            1: "admin/main.html",
            2: "seller/main.html",
            3: "buyer/main.html",
        }.get(request.user.role, 0)

        sidebar = {
            1: "sidebars/admin.html",
            2: "sidebars/seller.html",
            3: "sidebars/buyer.html",
        }.get(request.user.role)



    return {
        "main_page": main_pages,
        "sidebar": sidebar
    }










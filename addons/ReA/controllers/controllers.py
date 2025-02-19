# -*- coding: utf-8 -*-
from odoo import http


class Books(http.Controller):
    @http.route("/library/books")
    def list(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.search([])
        return http.request.render("library.book_qweb_template", {"books": books})

# class Library(http.Controller):
#     @http.route('/library/library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library/library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library.listing', {
#             'root': '/library/library',
#             'objects': http.request.env['library.library'].search([]),
#         })

#     @http.route('/library/library/objects/<model("library.library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library.object', {
#             'object': obj
#         })

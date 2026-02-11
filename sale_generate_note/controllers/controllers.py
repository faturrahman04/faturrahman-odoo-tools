# -*- coding: utf-8 -*-
# from odoo import http


# class SaleGenerateNote(http.Controller):
#     @http.route('/sale_generate_note/sale_generate_note', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_generate_note/sale_generate_note/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_generate_note.listing', {
#             'root': '/sale_generate_note/sale_generate_note',
#             'objects': http.request.env['sale_generate_note.sale_generate_note'].search([]),
#         })

#     @http.route('/sale_generate_note/sale_generate_note/objects/<model("sale_generate_note.sale_generate_note"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_generate_note.object', {
#             'object': obj
#         })


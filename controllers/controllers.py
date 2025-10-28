# -*- coding: utf-8 -*-
# from odoo import http


# class Tiendaonline(http.Controller):
#     @http.route('/tiendaonline/tiendaonline', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiendaonline/tiendaonline/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiendaonline.listing', {
#             'root': '/tiendaonline/tiendaonline',
#             'objects': http.request.env['tiendaonline.tiendaonline'].search([]),
#         })

#     @http.route('/tiendaonline/tiendaonline/objects/<model("tiendaonline.tiendaonline"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiendaonline.object', {
#             'object': obj
#         })


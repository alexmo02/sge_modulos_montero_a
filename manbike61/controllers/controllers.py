# -*- coding: utf-8 -*-
# from odoo import http


# class Manbike61(http.Controller):
#     @http.route('/manbike61/manbike61/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manbike61/manbike61/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manbike61.listing', {
#             'root': '/manbike61/manbike61',
#             'objects': http.request.env['manbike61.manbike61'].search([]),
#         })

#     @http.route('/manbike61/manbike61/objects/<model("manbike61.manbike61"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manbike61.object', {
#             'object': obj
#         })

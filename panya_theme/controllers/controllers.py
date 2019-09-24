# -*- coding: utf-8 -*-
from odoo import http

# class PanyaTheme(http.Controller):
#     @http.route('/panya_theme/panya_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/panya_theme/panya_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('panya_theme.listing', {
#             'root': '/panya_theme/panya_theme',
#             'objects': http.request.env['panya_theme.panya_theme'].search([]),
#         })

#     @http.route('/panya_theme/panya_theme/objects/<model("panya_theme.panya_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('panya_theme.object', {
#             'object': obj
#         })
from odoo import fields,models,api


class SaleReport(models.Model):
    _name = 'saleproduct.report'

    name = fields.Many2one('product.template', 'Product Name')

    sold_quantity = fields.Integer(string='Quantity Sold')
    remaining_quantity = fields.Integer(string='Quantity Remaining')



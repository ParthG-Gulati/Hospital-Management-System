from odoo import fields,api,models


class PurchaseAdd(models.Model):
    _name = "hospitalproduct.purchase"

    product_name = fields.Many2one('product.template', 'Product Name')

    vendor_name = fields.Char(string="Vendor Name")
    purchase_quantity = fields.Integer(string="Purchase Quantity")

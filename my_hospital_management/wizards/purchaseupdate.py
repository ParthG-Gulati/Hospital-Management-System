from odoo import api, models, fields


class Purchases(models.Model):
    _name = "purchase.update"

    purchase_qty = fields.Integer(string="Quantity Purchased")

    def update_purchase(self):
        print('Test purchase')


from odoo import api,models,fields

class Sales(models.Model):
    _name="sale.update"

    sold_qty  = fields.Integer(string="Quantity Sold")

    def update_sell(self):
        print('Test')
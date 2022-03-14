from odoo import models, fields


class HospitalAppointmentInherited(models.Model):
    _inherit = 'calendar.event'

    patient_app = fields.Many2one('res.partner', string='Patient Name', required=True)
    doctor_app = fields.Many2one('hr.employee', string='Doctor Name')
    hospitalization_selection = fields.Boolean(string='Hospitalize')

    def action_hospitalize(self):
        return{
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("sale.view_order_form").id,
            'target': 'self'
        }


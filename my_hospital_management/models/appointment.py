from odoo import models, fields


class HospitalAppointmentInherited(models.Model):
    _inherit = 'calendar.event'

    patient_app = fields.Many2one('res.partner', string='Patient Name', required=True)
    doctor_app = fields.Many2one('hr.employee', string='Doctor Name')
    # hospitalization_selection = fields.Boolean(string='Hospitalize')
    symptom_lines = fields.One2many('patient.symptom','sequence','Symptoms List')
    states = fields.Selection([
        ('confirm','Confirm'),
        ('cancel','Cancel')
    ])

    def action_confirm(self):
        for rec in self:
            rec.states = 'confirm'
            return{
                'effect':{
                    'fadeout': 'slow',
                    'message': 'Appontment Created !!!!!',
                    'type': 'rainbow_man',
                }
            }


    def action_hospitalize(self):
        '''jbkbg'''
        return{
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("sale.view_order_form").id,
            'target': 'self'
        }

from odoo import models, fields


class HospitalAppointmentInherited(models.Model):
    _inherit = 'calendar.event'

    patient_app = fields.Many2one('res.partner', string='Patient Name', required=True)
    doctor_app = fields.Many2one('hr.employee', string='Doctor Name')
    symptom_lines = fields.One2many('patient.symptom','sequence','Symptoms List')
    state_appo = fields.Selection([
        ('confirm','Confirm'),
        ('cancel','Cancel')
    ])

    # _sql_constraints = [
    #     ('user_unique_appointment', 'UNIQUE(start)', 'Other Appointment On similar Timeslot. Please try with the other slot')
    # ]

    # _sql_constraints = [
    #     ('new_user_unique_appointment', 'check(UNIQUE(start) and UNIQUE(doctor_app))',
    #      'Other Appointment On similar Timeslot. Please try with the other slot')
    # ]

    _sql_constraints = [
        ('user_appoint', 'UNIQUE(start)',
         'Other Appointment On similar Timeslot. Please try with the other slot')
    ]

    def action_confirm(self):
        for rec in self:
            rec.state_appo = 'confirm'
            return{
                'effect':{
                    'fadeout': 'slow',
                    'message': 'Appontment Created !!!!!',
                    'type': 'rainbow_man',
                }
            }


    def action_hospitalize(self):
        '''If patient needs to hospitalize open hospitalize directly'''
        return{
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("sale.view_order_form").id,
            'target': 'self'
        }

    def action_cancel(self):
        self.state_appo = 'cancel'

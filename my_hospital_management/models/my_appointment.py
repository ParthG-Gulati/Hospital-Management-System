from odoo import fields, api, models, _


class HospitalAppointment(models.Model):
    _name = 'my_hospital.appointment'
    _rec_name = 'name_id'

    appointment_sequence = fields.Char(string='APPOINTMENT', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    name_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('hr.employee', string='Doctor')
    appointment_start = fields.Datetime(string='Appointment Date', required=True)
    appointment_end = fields.Datetime(string='Appointment End')
    patient_type = fields.Selection([
        ('inpatient', 'Inpatient'),
        ('outpatient', 'Outpatient')
    ], string='Patient Type', default='inpatient')
    patient_urgency = fields.Selection([
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('Emergency', 'Emergency')
    ])
    patient_notes = fields.Text()

    @api.model
    '''Sequence for appointments'''
    def create(self, vals):

        if vals.get('appointment_sequence', _('New')) == _('New'):
            vals['appointment_sequence'] = self.env['ir.sequence'].next_by_code('my_hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

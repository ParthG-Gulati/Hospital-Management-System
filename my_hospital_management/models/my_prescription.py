from odoo import fields, api, models, _


class HospitalPrescription(models.Model):
    _name = 'my_hospital.prescription'
    _rec_name = 'patient_prescription_name_id'
    prescription_id = fields.Char(string='Prescription Id', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    patient_prescription_name_id = fields.Many2one('res.partner', string='Patient Name', required=True)
    doctor_prescription_name_id = fields.Many2one('hr.employee', string='Prescribing Doctor', required=True)
    prescription_date = fields.Datetime(string="Prescription Date",help="Please select the Prescription date", required=True, default=fields.Datetime.now)
    prescription_line_ids = fields.One2many('prescription.line', 'medicine_id', 'Patient Name')
    patient_diet = fields.Text(string='Diet Suggestion')
    diet_notes = fields.Text(string='Notes')
    email_id = fields.Char(string='Email')
    user_id = fields.Many2one('res.users', 'User')

    def print_report(self):
        return self.env.ref('my_hospital_management.patient_prescription_report').report_action(self)

    @api.model
    def create(self, vals):
        '''Sequence for prescription'''
        if vals.get('prescription_id', ('New')) == ('New'):
            vals['prescription_id'] = self.env['ir.sequence'].next_by_code('my_hospital.prescription') or _('New')
        res = super(HospitalPrescription, self).create(vals)
        return res

    def send_prescription(self):
        '''Send Mail action for Prescription'''
        template_id = self.env.ref('my_hospital_management.prescription_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


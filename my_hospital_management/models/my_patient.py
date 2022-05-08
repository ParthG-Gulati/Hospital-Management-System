from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    pat_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],string='Gender', default='male')
    pat_age = fields.Integer(string='Patient_Age')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    # patient_blood_type = fields.Selection([
    #     ('A', 'A'),
    #     ('B', 'B'),
    #     ('AB', 'AB'),
    #     ('O', 'O')
    # ], string='Blood Type')

    blood = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ], string='Blood Type')

    rh = fields.Selection([
        ('+', '+'),
        ('-', '-')
    ], string='RH Type')
    patient_primary_doctor = fields.Many2one('hr.employee', required=True, string='Primary Doctor')
    # patient_deceased = fields.Boolean(string='Deceased')
    patient_exercise_info = fields.Boolean(string='Exercise')
    patient_smokes = fields.Boolean(string='Smokes')
    patient_drinks_alcohol = fields.Boolean(string='Drinks alcohol')
    patient_drug_addict = fields.Boolean(string='Drug addict')
    patient_disease_lines = fields.One2many('main.disease','patient_disease_line','Disease Record')
    medication_line_ids = fields.One2many('medication.line', 'medication_id', 'Medications')
    hospital_management_vaccination_ids = fields.One2many('hospital.vaccination', 'hospital_management_vaccine_id', string='Vaccination')
    appointment_count = fields.Integer(string='Appointmnt Count',compute='patient_appointment_count')
    lab_count = fields.Integer(string='Lab reports',compute='patient_lab_count')
    prescription_count = fields.Integer(string='Prescription',compute='patient_prescription_count')
    # @api.constrains('pat_age')
    # def check_age(self):
    #     '''To Validate Age Cannot be 0'''
    #     for rec in self:
    #         if rec.pat_age == 0:
    #             raise ValidationError("Age cannot be zero")
    #
    # @api.constrains('mobile')
    # def check_mobile(self):
    #     '''To Validate Age Cannot be 0'''
    #     for rec in self:
    #         if len(rec.mobile) != 10:
    #             raise ValidationError("Incorrect Mobile Number")

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('res.partner') or _('New')
        res = super(ResPartner, self).create(vals)
        return res


    def patient_appointment_count(self):
        '''Patients Appointments Count'''
        for rec in self:
            appointment_count=self.env['calendar.event'].search_count([('patient_app','=',rec.id)])
            rec.appointment_count = appointment_count

    def action_oppen_appointment(self):
        '''Open Appointment from patient form'''
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model':'calendar.event',
            'domain' : [('patient_app','=',self.id)],
            'view_mode': 'calendar,form,tree',
            'target': 'current',
        }

    def patient_lab_count(self):
        '''Lab test Count for Patient'''
        for rec in self:
            lab_count=self.env['hospital.laboratory'].search_count([('lab_patient','=',rec.id)])
            rec.lab_count = lab_count

    def action_open_lab(self):
        '''Open Lab test'''
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lab Sessions',
            'res_model':'hospital.laboratory',
            'domain' : [('lab_patient','=',self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }


    def patient_prescription_count(self):
        '''Prescriptions by doctor'''
        for rec in self:
            prescription_count=self.env['my_hospital.prescription'].search_count([('patient_prescription_name_id','=',rec.id)])
            rec.prescription_count = prescription_count

    def action_open_prescription(self):
        '''Open prescription'''
        return {
            'type': 'ir.actions.act_window',
            'name': 'Prescription',
            'res_model':'my_hospital.prescription',
            'domain' : [('patient_prescription_name_id','=',self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def print_medical_card(self):
        return self.env.ref('my_hospital_management.patient_medical_report_card').report_action(self)

    def action_medical_card(self):
        '''Send mail action for medical card'''

        template_id = self.env.ref('my_hospital_management.medical_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

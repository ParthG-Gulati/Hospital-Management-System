from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    pat_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],string='Gender')
    pat_age = fields.Integer(string='Patient_Age')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string='Blood Type')
    rh = fields.Selection([
        ('+', '+'),
        ('-', '-')
    ], string='RH Type')
    patient_primary_doctor = fields.Many2one('hr.employee', string='Primary Doctor')
    patient_deceased = fields.Boolean(string='Deceased')
    patient_exercise_info = fields.Boolean(string='Exercise')
    patient_smokes = fields.Boolean(string='Smokes')
    patient_drinks_alcohol = fields.Boolean(string='Drinks alcohol')
    patient_drug_addict = fields.Boolean(string='Drug addict')
    # hospital_management_vaccination_ids = fields.One2many('hospital.vaccination', 'hospital_management_vaccine_id', string='Vaccination')

    @api.model
    def create(self, vals):

        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(ResPartner, self).create(vals)
        return res







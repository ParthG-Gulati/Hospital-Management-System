from odoo import http
from odoo.http import request

class WebsitePrescription(http.Controller):
    @http.route('/patient/form', type='http',auth='user',website=True)

    def prescription_web(self,**kwargs):
        patient_record = request.env['res.partner'].search([])
        doctor_record = request.env['hr.employee'].search([])
        state_record = request.env['res.country.state'].search([])
        country_record = request.env['res.country'].search([])
        return request.render('my_hospital_management.patient_form_online',
                              {'doctor_record': doctor_record, 'patient_record': patient_record, 'state_record' : state_record,'country_record' : country_record})

    @http.route('/form/submit', type='http', auth='public', website=True)
    def create_appointment(self,**kwargs):
        val_list = {
            'name': kwargs.get('patient_name'),
            'street': kwargs.get('street'),
            'city': kwargs.get('city'),
            'state_id': kwargs.get('state'),
            'country_id': kwargs.get('country'),
            'zip': kwargs.get('zip'),
            'patient_primary_doctor': kwargs.get('doctor_name'),
            'pat_gender': kwargs.get('gender'),
            'pat_age': kwargs.get('patient_age'),
            'mobile': kwargs.get('mobile'),
        }
        # xyz = request.env['res.partner'].sudo().search([("id","=",request.env.user.partner_id.id)])
        # xyz.sudo().update(val_list)
        # print("Working.............................")
        # print(request.env['res.partner'].sudo().write(val_list))
        return request.render('my_hospital_management.appointment_submit', {})

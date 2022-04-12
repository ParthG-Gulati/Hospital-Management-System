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

    @http.route('/form/submit', type='http', auth='user', website=True)
    def create_appointment(self,**kwargs):
        # val_list = {
        #     'name': kwargs.get('patient_name'),
        #     'street': kwargs.get('meeting_subject'),
        #     'city': datetime.strptime(kwargs.get('appointment_date'), '%Y-%m-%dT%H:%M') + relativedelta(hours=-6,
        #                                                                                                  minutes=30),
        #     'state_id': kwargs.get('doctor_name'),
        #     'country_id': kwargs.get('doctor_name'),
        #     'zip': kwargs.get('doctor_name'),
        #     'patient_primary_doctor': datetime.strptime(kwargs.get('appointment_date_end'), '%Y-%m-%dT%H:%M') + relativedelta(hours=-6,
        #                                                                                                     minutes=30),
        #     'pat_gender': kwargs.get('doctor_name'),
        #     'pat_age': kwargs.get('doctor_name'),
        #     'mobile': kwargs.get('doctor_name'),
        # }
        xyz = request.env['res.partner'].sudo().search([])
        print(".........",xyz)
        # xyz = request.env['my_hospital.prescription'].sudo().search(
        #     [("name", "=", request.env.user.partner_id.id)])
        # xyz.write(val_list)
        return request.render('my_hospital_management.appointment_submit', {})

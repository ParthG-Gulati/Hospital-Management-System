from odoo import http
from odoo.http import request
class WebPatientAppointmentRecord(http.Controller):
    @http.route('/patient/record', type='http',auth='user',website=True)
    def view_prescriptions(self,**kwargs):
        appointment_record = request.env['calendar.event'].sudo().search([("patient_app","=",request.env.user.partner_id.id)])
        return request.render('my_hospital_management.patient_appointments_details',{'appointment_record': appointment_record})

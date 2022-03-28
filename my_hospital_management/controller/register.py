from odoo import http
from odoo.http import request

class WebRegister(http.Controller):
    @http.route('/register/',type='http',auth='public',website=True)
    def patient_register(self,**kw):
        return request.render('my_hospital_management.registration_online',{})

    @http.route('/registered', type='http', auth='public', website=True)
    def create_patient(self, **kw):
        val_list1 = {
            'name': kw.get('registry_name'),
            'login': kw.get('registry_email'),
        }
        # val_list2 = {
        #     'wizard_id' : kw.get('registry_email'),
        #     'new_passwd' : kw.get('registry_pass'),
        #     'user_id' : kw.get('registry_email'),
        # }
        # val_list = Merge(val_list)
        request.env['res.users'].sudo().create(val_list1)
        # request.env['change.password.user'].sudo().create(val_list2)
        return request.render('my_hospital_management.register_submit', {})
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Area(models.Model):
    _name = 'bangunan.area'
    _description = 'bangunan area'
    _rec_name = 'nama'

    kode=fields.Char(string='Kode', track_visibility='always' )
    nama=fields.Char(string='Nama area', required=True)

    @api.constrains('kode')
    def cek_kode(self):
        count = self.env['bangunan.area'].search_count([('kode', '=', self.kode)])
        if (count > 1 ):
            raise ValidationError(_('Kode sudah digunakan '))

    # @api.model
    # def create(self, vals):
    #     if vals.get('kode', ('New')) == ('New'):
    #         vals['kode'] = self.env['ir.sequence'].next_by_code('bangunan.area.sequence') or ('New')
    #     return super(Area, self).create(vals)
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Zona(models.Model):
    _name = 'bangunan.zona'
    _description = 'bangunan zona'
    _rec_name = 'nama'

    kode=fields.Char(string='Kode', track_visibility='always' )
    nama=fields.Char(string='Nama zona', required=True)
    area_id=fields.Many2one('bangunan.area', string='Area')

    @api.constrains('kode')
    def cek_kode(self):
        count = self.env['bangunan.zona'].search_count([('kode', '=', self.kode)])
        if (count > 1):
            raise ValidationError(_('Kode sudah digunakan '))
    # @api.model
    # def create(self, vals):
    #     if vals.get('kode', ('New')) == ('New'):
    #         vals['kode'] = self.env['ir.sequence'].next_by_code('bangunan.zona.sequence') or ('New')
    #     return super(Zona, self).create(vals)
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Ruang(models.Model):
    _name = 'bangunan.ruang'
    _description = 'bangunan ruang'
    _rec_name = 'name'

    kode=fields.Char(string='Kode', track_visibility='always')
    name=fields.Char(string='Nama Ruangan', required=True)
    bangunan_id=fields.Many2one('bangunan.bangunan', string='Bangunan')
    lantai_id = fields.Many2one('bangunan.lantai', string='Lantai')

    @api.constrains('kode')
    def cek_kode(self):
        count = self.env['bangunan.ruang'].search_count([('kode', '=', self.kode)])
        if (count > 1):
            raise ValidationError(_('Kode sudah digunakan '))

    @api.onchange('bangunan_id')
    def onchange_bangunan(self):
        for rec in self:
            return {'domain': {'lantai_id': [('bangunan_id', '=', rec.bangunan_id.id)]}}


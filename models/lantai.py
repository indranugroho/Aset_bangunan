from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Lantai(models.Model):
    _name = 'bangunan.lantai'
    _description = 'bangunan lantai'
    _rec_name = 'name'

    kode=fields.Char(string='Kode',track_visibility='always')
    name=fields.Char(string='Nama Lantai', required=True)
    bangunan_id=fields.Many2one('bangunan.bangunan', string='Bangunan')
    ruang_count = fields.Integer(string='Ruang', compute="get_ruang_count")

    @api.constrains('kode')
    def cek_kode(self):
        count = self.env['bangunan.lantai'].search_count([('kode', '=', self.kode)])
        if (count > 1):
            raise ValidationError(_('Kode sudah digunakan '))

    @api.multi
    def get_ruang_count(self):
        count = self.env['bangunan.ruang'].search_count([('lantai_id', '=', self.id)])
        self.ruang_count = count

    # @api.model
    # def create(self, vals):
    #     if vals.get('kode', ('New')) == ('New'):
    #         vals['kode'] = self.env['ir.sequence'].next_by_code('bangunan.lantai.sequence') or ('New')
    #     return super(Lantai, self).create(vals)
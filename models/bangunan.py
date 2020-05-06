from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Bangunan(models.Model):
    _name = 'bangunan.bangunan'
    _description = 'bangunan'
    _rec_name = 'name'

    kode=fields.Char(string='Kode',track_visibility='always' )
    name=fields.Char(string='Nama Bangunan', required=True)
    area_id = fields.Many2one('bangunan.area', string='Area')
    zona_id = fields.Many2one('bangunan.zona', string='Zona')
    jenis_bangunan=fields.Selection([
        ('kantor', 'Kantor'),
        ('sekolah', 'Sekolah'),
        ('ibadah', 'Ibadah'),
        ('sosial', 'sosial')
    ], string='Jenis Bangunan')
    nomer_imb=fields.Char(string='Nomer IMB')
    alamat=fields.Char(string='Alamat')
    sertifikat=fields.Selection([
        ('shm', 'SHM'),
        ('shgb', 'SHGB')
    ], string='Sertifikat')
    nomer_sertifikat=fields.Char(string='No. Sertifikat')
    keterangan=fields.Text(String='Keterangan')

    lantai_count = fields.Integer(string='Lantai', compute="get_lantai_count")

    # @api.model
    # def create(self, vals):
    #     if vals.get('kode', ('New')) == ('New'):
    #         vals['kode'] = self.env['ir.sequence'].next_by_code('bangunan.bangunan.sequence') or ('New')
    #     return super(Bangunan, self).create(vals)

    @api.constrains('kode')
    def cek_kode(self):
        count = self.env['bangunan.bangunan'].search_count([('kode', '=', self.kode)])
        if (count > 1):
            raise ValidationError(_('Kode sudah digunakan '))

    @api.onchange('area_id')
    def onchange_area(self):
        for rec in self:
            return {'domain': {'zona_id': [('area_id', '=', rec.area_id.id)]}}

    @api.multi
    def get_lantai_count(self):
        count = self.env['bangunan.lantai'].search_count([('bangunan_id', '=', self.id)])
        self.lantai_count = count
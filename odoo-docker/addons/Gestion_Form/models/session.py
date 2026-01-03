from odoo import models, fields, api


class GestionFormationSession(models.Model):
    _name = "gestion.formation.session"
    _description = "Session de formation"

    name = fields.Char(string="Nom de la session", required=True)
    formation_id = fields.Many2one(
        comodel_name="gestion.formation",
        string="Formation",
        required=True,
        ondelete="cascade",
    )

    ville = fields.Selection(string="Ville", related="formation_id.ville", store=True, readonly=True)
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    capacite = fields.Integer(string="Capacité", default=20)

    formateur_id = fields.Many2one(
        comodel_name="res.partner",
        string="Formateur",
    )

    state = fields.Selection(
        [
            ("draft", "Brouillon"),
            ("confirmed", "Confirmée"),
            ("in_progress", "En cours"),
            ("done", "Terminée"),
            ("cancel", "Annulée"),
        ],
        string="Statut",
        default="draft",
        required=True,
    )

    inscription_ids = fields.One2many(
        comodel_name="gestion.formation.inscription",
        inverse_name="session_id",
        string="Inscriptions",
    )

    seats_taken = fields.Integer(string="Inscriptions", compute="_compute_seats", store=False)
    seats_available = fields.Integer(string="Places restantes", compute="_compute_seats", store=False)

    @api.depends("inscription_ids", "inscription_ids.state", "capacite")
    def _compute_seats(self):
        for rec in self:
            taken = len(rec.inscription_ids.filtered(lambda x: x.state != "cancel"))
            rec.seats_taken = taken
            rec.seats_available = (rec.capacite or 0) - taken

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancel"})

    def action_set_draft(self):
        self.write({"state": "draft"})

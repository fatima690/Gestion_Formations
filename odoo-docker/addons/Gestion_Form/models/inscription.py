from odoo import models, fields


class GestionFormationInscription(models.Model):
    _name = "gestion.formation.inscription"
    _description = "Inscription à une session"

    session_id = fields.Many2one(
        comodel_name="gestion.formation.session",
        string="Session",
        required=True,
        ondelete="cascade",
    )

    participant_id = fields.Many2one(
        comodel_name="res.partner",
        string="Participant",
        required=True,
    )

    formation_id = fields.Many2one(
        comodel_name="gestion.formation",
        string="Formation",
        related="session_id.formation_id",
        store=True,
        readonly=True,
    )

    formateur_id = fields.Many2one(
        comodel_name="res.partner",
        string="Formateur",
        related="session_id.formateur_id",
        store=True,
        readonly=True,
    )

    qty = fields.Integer(string="Nombre", default=1)

    date_inscription = fields.Date(string="Date d'inscription", default=fields.Date.context_today)

    state = fields.Selection(
        [
            ("draft", "Brouillon"),
            ("confirmed", "Confirmée"),
            ("cancel", "Annulée"),
        ],
        string="Statut",
        default="draft",
        required=True,
    )

    note = fields.Text(string="Remarques")

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_cancel(self):
        self.write({"state": "cancel"})

    def action_set_draft(self):
        self.write({"state": "draft"})

from odoo import models, fields

class GestionFormation(models.Model):
    _name = "gestion.formation"
    _description = "Gestion des Formations"

    name = fields.Char(string="Nom de la formation", required=True)
    responsable = fields.Char(string="Responsable de formation")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    duree = fields.Integer(string="Durée (jours)")
    statut = fields.Selection([
        ("planifie", "Planifié"),
        ("en_cours", "En cours"),
        ("termine", "Terminé"),
        ("annule", "Annulé"),
    ], string="Statut", default="planifie")
    nombre_places = fields.Integer(string="Nombre de places", default=20)
    description = fields.Text(string="Description")
    prix = fields.Float(string="Prix (DH)")

    ville = fields.Selection(
        [
            ("casablanca", "Casablanca"),
            ("rabat", "Rabat"),
            ("marrakech", "Marrakech"),
            ("fes", "Fès"),
            ("tanger", "Tanger"),
            ("agadir", "Agadir"),
            ("meknes", "Meknès"),
            ("oujda", "Oujda"),
            ("tetouan", "Tétouan"),
            ("kenitra", "Kénitra"),
        ],
        string="Ville",
        default="casablanca",
    )

    session_ids = fields.One2many(
        comodel_name="gestion.formation.session",
        inverse_name="formation_id",
        string="Sessions",
    )
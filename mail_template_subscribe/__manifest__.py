{
    "name": "Mail Template Subscribe",
    "summary": """
        When sending a mail subscribe matching template subscribe domain.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Social",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mail"],
    "data": [
        "views/mail_template_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}

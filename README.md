# Grafana Daily Report Automation

En 2026, avec l’existence de Selenium, aucun reporting ne devrait encore être manuel.  
Ce projet automatise la capture des dashboards Grafana et l’envoi quotidien par email.

## 🛠️ Fonctionnalités

- Se connecte automatiquement à Grafana avec les identifiants fournis.
- Capture des captures d’écran de dashboards définis dans la configuration.
- Envoie les screenshots par email à une ou plusieurs adresses.
- Fonctionne sur Windows avec Chrome (ou tout OS avec Chrome et ChromeDriver).

## ⚙️ Configuration

1. Crée un environnement virtuel Python (recommandé) :

```bash
python -m venv venv

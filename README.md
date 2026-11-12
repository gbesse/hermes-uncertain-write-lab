# hermes-uncertain-write-lab

## Français

Réconcilier une écriture distante dont la réponse est perdue.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m hermes_uncertain_write_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Réconcilier une écriture distante dont la réponse est perdue : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reconcile a remote write with a lost response.

Synthetic data; no network access or secret required.

```sh
python -m hermes_uncertain_write_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Reconcile a remote write with a lost response: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Conciliar escritura remota con respuesta perdida.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m hermes_uncertain_write_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Conciliar escritura remota con respuesta perdida: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://hermes-agent.nousresearch.com/docs/developer-guide/plugins
- https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [agent-branch-guard](https://github.com/gbesse/agent-branch-guard) est un autre diagnostic du portefeuille. Ici : Réconcilier une écriture distante dont la réponse est perdue. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [agent-branch-guard](https://github.com/gbesse/agent-branch-guard) is a different portfolio diagnostic. Here: Reconcile a remote write with a lost response. Scope comparison only, no affiliation or superiority benchmark.

ES: [agent-branch-guard](https://github.com/gbesse/agent-branch-guard) es otro diagnóstico del portafolio. Aquí: Conciliar escritura remota con respuesta perdida. Comparación de alcance, sin afiliación ni benchmark de superioridad.

## Hermes — FR / EN / ES

FR : dépôt utilisable comme plugin de répertoire Hermes (`plugin.yaml`, `register(ctx)`) avec un outil de laboratoire et enveloppe FR/EN/ES. Installer le dépôt source dans le répertoire de plugins d’un profil isolé, puis valider et activer explicitement selon la documentation Hermes. Les tests locaux vérifient le contrat d’enregistrement et le handler sans modèle ni secrets ; ils ne prouvent pas une session Hermes complète. Aucun appel à incwo/Bruno ni commande métier réelle. Les effets des laboratoires sont confinés à des temporaires et au loopback.

EN: directory-style Hermes plugin (`plugin.yaml`, `register(ctx)`) exposing a laboratory tool and FR/EN/ES envelope. Install the source repository into an isolated profile’s plugin directory, then explicitly validate and enable following Hermes documentation. Local tests verify registration and handler contracts without a model or secrets; they do not prove a complete Hermes session. No incwo/Bruno calls or real business commands. Lab effects are confined to temporary files and loopback.

ES: plugin de directorio Hermes (`plugin.yaml`, `register(ctx)`) con herramienta de laboratorio y envoltura FR/EN/ES. Instalar código fuente en directorio de plugins de un perfil aislado, validar y activar explícitamente según documentación Hermes. Pruebas locales verifican registro y handler sin modelo ni secretos; no prueban sesión Hermes completa. Sin llamadas incwo/Bruno ni comandos empresariales reales. Efectos limitados a temporales y loopback.

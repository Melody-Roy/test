name: Tests automatiques

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Récupération du dépôt
        uses: actions/checkout@v3

      - name: Installation de Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Installation de pytest
        run: pip install pytest

      - name: Exécution des tests
        run: pytest -q
#!/bin/bash
# Esperar até que o banco de dados PostgreSQL esteja pronto
wait-for-it db:5432 -t 60

# Iniciar a aplicação Flask na porta 9001
python run.py --port 9001

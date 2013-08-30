#!/usr/bin/env bash
cd $(dirname "${BASH_SOURCE[0]}")

VENV='heitmgt'

if [ -e ../.venv ]
then
  VENV=$(cat ../.venv)
fi

. ~/.virtualenvs/$VENV/bin/activate
. ~/.virtualenvs/$VENV/bin/postactivate

ROOT_DIR=$(python ./get_config.py project_root_dir)
DB_NAME=$(python ./get_config.py db_name)
DB_USER=$(python ./get_config.py db_user)

OUT_DIR="${ROOT_DIR}/var/pgdump"
OUT_FILE="${DB_NAME}.$(date +%Y%m%d-%H%M%S)"
OUT_PATH="${OUT_DIR}/${OUT_FILE}"

pg_dump -Fc -U ${DB_USER} ${DB_NAME} > ${OUT_PATH}

python ./pg_purge.py
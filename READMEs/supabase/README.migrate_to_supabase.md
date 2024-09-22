# TLDR

Documenting steps of moving Postgres DB from Render.com

## PHASE 1

- 1st created a project called `kalygo3` in the default Org
- Copied the credentials for the DB provisioned in Supabase into this project
- Run all migrations
  - `alembic upgrade head` WORKED √

## PHASE 2

- Backed up Kalygo DB
  - ansible-playbook --inventory inventory.prod --key-file "<PATH_TO_PEM_FILE>" backup_db.yml

## PHASE 3

TLDR: `kalygo-v3` is now the project ID for the SWARMS PLAYGROUND and `kalygo` is now the project ID for KALYGO

- Run another Cloud Run service dedicated to Kalygo
  - right now `kalygo-v3` is running the SWARMS PLAYGROUND application
  - rename `kalygo-v3` to be called `swarms-playground`
  - create new project called `kalygo`

## PHASE 4

- Copying the "Swarms Playground" version of the repos to another GitHub repo
- Setting up CICD for these new "Swarms Playground" version
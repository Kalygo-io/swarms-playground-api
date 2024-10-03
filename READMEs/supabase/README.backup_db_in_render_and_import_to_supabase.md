
# Backup data in Render.com

pg_dump -h <render_host> -U <render_user> -d <render_db_name> -F c -b -v -f /path/to/backup.dump

# Import into Supabase

pg_restore -h <supabase_host> -U <supabase_user> -d <supabase_db_name> -v /path/to/backup.dump
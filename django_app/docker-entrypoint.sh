#!/bin/sh

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python /usr/src/black_hole/manage.py migrate  2>&1; do
    echo "Migration is in progress status"
    sleep 3
done

echo "Collect static at startup of project"

# Wait for few minute and run db migraiton
while ! python /usr/src/black_hole/manage.py collectstatic  2>&1; do
    echo "collectstatic is in progress status"
    sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"
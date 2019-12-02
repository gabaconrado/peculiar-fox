# Sync files with latest commit on master
git fetch
#git reset --hard origin/master

# TODO: Generate env vars
# Rebuild docker-images
docker-compose -f docker-compose.yml -f ../deploy/docker-compose.yml down && \
docker-compose -f docker-compose.yml -f ../deploy/docker-compose.yml up --build -d

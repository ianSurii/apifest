FROM postgres:latest
# RUN -d  --name ${POSTGRES_DB} \
#     -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD}\
#     -e PGDATA=/var/lib/postgresql/data/pgdata \
#     -v /app-db-data:/var/lib/postgresql/data \
#     postgres
# COPY ./timezone.sh /
# RUN chmod +x /timezone.sh
# RUN ./timezone.sh
RUN ln -fs /usr/share/zoneinfo/Africa/Nairobi /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN echo Africa/Nairobi > /etc/timezone
EXPOSE 5432
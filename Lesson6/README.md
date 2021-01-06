https://www.notion.so/Scheduler-HA-Public-8faed2642bc849158052ba9f0e1a2c39

astro dev init
astro d start

In old,
Change the docker image of Airflow in the Dockerfile

```docker
FROM astronomerinc/ap-airflow:1.10.12-alpine3.10
```

Once Airflow is running your might need to do that

```docker
docker exec <container_webserver> airflow sync_perm
```

Run the example DAG brought with the Astro CLI and kill the scheduler

```bash
docker ps

docker kill <container_scheduler>
```

In new,
Change the docker image of Airflow in the Dockerfile

```docker
FROM astronomerio/ap-airflow:2.0.0-buster-onbuild-22237
```

Run the example DAG brought with the Astro CLI and kill the scheduler

```bash
docker ps

docker kill <container_scheduler>
```

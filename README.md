# Analysis of PostgreSQL connection poolers (PGBouncer and PgCat)

This repo contains all the necessary data to reproduce the tests shown in iFood's Medium post.

- Configuration Files
- Scripts

## Infraestructure Details

| | |
|----------------------|-----------------------------------------------|
| **VM**               | c5.4xlarge (16 vCPUs, 32 GiB Memory)          |
| **Storage**          | dedicated /data in RAID 0 - 12k IOPS          |
| **Operating System** | Rocky Linux 9.4                               |
| **Postgres**         | 16.4                                          |
| **Pgbouncer**        | v1.23                                         |
| **Pgcat**            | v1.2.0                                        |

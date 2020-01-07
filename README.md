Verbum
---
Client-server system to find similar sentences in uploaded snippets.

## Build & Run

First copy `env.env` to `.env` and edit to your liking.
Names of env variables there are self-explanatory. Just take
special care of `API_URL`: it has to point to the machine that runs
Docker container and it has to have either real IP or hostname.

After that do:

```bash
$ docker-compose build
$ docker-compose up
```

Once the build and launch is complete, the site will be
available at `http://<your host name>/`. Build might take quite
a while since it downloads a few gigabytes of language data.

## Development

Take a look at `client/Dockerfile` and `server/Dockerfile`
to see what steps need to be taken to setup respective
systems. After that use standard Flask/NextJS dev practices.

## TODO

In random order:

- Improve UI: it's ugly
- Optimize Docker builds
- Fix some code-smell both in `server` and `client`
- Add tests
- Add other languages
- Migrate to something more serious than SQLite

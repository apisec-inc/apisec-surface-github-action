# APIsec Surface GitHub Action

Finds the APIs in your code with [APIsec Surface](https://pypi.org/project/apisec-surface/) and sends them to APIsec. Each repository becomes one APIsec application, and every later run updates that same application.

## Quick start

1. In APIsec, create a personal access token.
2. In your repository, add it as the secret `APISEC_PAT` (Settings, Secrets and variables, Actions).
3. Add `.github/workflows/apisec-surface.yml`:

```yaml
name: APIsec Surface

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: apisec-surface-${{ github.ref }}
  cancel-in-progress: true

jobs:
  surface:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: apisec-inc/apisec-surface-github-action@v1
        with:
          apisec-pat: ${{ secrets.APISEC_PAT }}
```

Pushes to `main` upload to APIsec. Pull requests only analyze, so they need no token and work from forks.

## Inputs

| Input | Default | Description |
|---|---|---|
| `apisec-pat` | | APIsec personal access token. Required unless `dry-run` is true. |
| `registration-code` | `ci-github-action` | Registration code for the applications this creates. |
| `api-url` | `https://api.apisecapps.com` | APIsec API URL. |
| `path` | `.` | Path to the code to analyze. |
| `dry-run` | true on pull requests | `true` analyzes without uploading. |
| `cli-version` | newest 1.x | Pin a Surface CLI version, for example `1.2.1`. |
| `fail-on-error` | `true` | `false` keeps the job green when the scan or upload fails. |

## Outputs

| Output | Description |
|---|---|
| `endpoints-count` | Number of API routes found. |
| `frameworks-detected` | Comma-separated list of detected frameworks. |
| `application-id` | APIsec application id. Empty on dry runs. |
| `success` | `true` when the scan, and the upload unless dry-run, succeeded. |

## Scanning a whole organization

To scan every repository in an organization from one place, use the [APIsec orchestrator](https://github.com/apisec-inc/apisec-orchestrator) instead.

## Versions

`@v1` always points to the newest 1.x release of this action, and each run installs the newest Surface CLI 1.x. Pin `@v1.0.0` and `cli-version` to freeze both.

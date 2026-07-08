#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${DEPLOY_ENV:-production}"
VERSION="${GITHUB_SHA:-local}"

echo "Starting deploy to ${ENVIRONMENT}"
echo "Version: ${VERSION}"
echo "API_KEY is set: ${API_KEY:+yes}"
echo "Deploy complete."

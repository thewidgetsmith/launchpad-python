# See here for image contents: https://harbor.usu.edu/harbor/projects/29/repositories/base-images%2Fpython-instantclient/tags/3.9-buster-slim

# Python 3.9 Buster Slim with Oracle Instant Client
ARG VARIANT="3.9-buster-slim"
FROM harbor.usu.edu/base-images/python-instantclient:${VARIANT}

# Add user for VSCode
RUN useradd -ms /bin/bash vscode
WORKDIR /home/vscode
USER vscode

# [Optional] Add container modifications below (additional packages/configuration)
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

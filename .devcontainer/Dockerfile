# Python 3.9 Buster Slim with Oracle Instant Client
# See here for image contents: https://harbor.usu.edu/harbor/projects/29/repositories/base-images%2Fpython-instantclient/tags/3.9-buster-slim
ARG VARIANT="3.9-buster-slim"
FROM harbor.usu.edu/base-images/python-instantclient:${VARIANT}

# Copy scripts to execute
COPY .devcontainer/scripts/*.sh .devcontainer/scripts/*.env /tmp/scripts/

# [Option] Install zsh
ARG INSTALL_ZSH="true"

# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1099
ARG USER_GID=$USER_UID

# Run package updates/maintenance
RUN apt-get update \
  && export DEBIAN_FRONTEND=noninteractive \
    # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    && apt-get purge -y imagemagick imagemagick-6-common \

    # Install common packages, non-root user
    && bash /tmp/scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \

    # Clean up packages and remove apt-cache
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Setup default python tools in a venv via pipx to avoid conflicts
ENV PIPX_HOME=/usr/local/py-utils \
    PIPX_BIN_DIR=/usr/local/py-utils/bin
ENV PATH=${PATH}:${PIPX_BIN_DIR}
RUN bash /tmp/scripts/python-debian.sh "none" "/usr/local" "${PIPX_HOME}" "${USERNAME}" \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
RUN if ! cat /etc/group | grep -e "^pip-global:" > /dev/null 2>&1; then groupadd -r pip-global; fi \
    && usermod -a -G pip-global vscode \
    && umask 0002 && mkdir -p ${PIP_TARGET} \
    && chown :pip-global ${PIP_TARGET} \
    && ( [ ! -f "/etc/profile.d/00-restore-env.sh" ] || sed -i -e "s/export PATH=/export PATH=\/usr\/local\/pip-global:/" /etc/profile.d/00-restore-env.sh )

# Remove scripts for final image
RUN rm -rf /tmp/scripts

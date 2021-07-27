SHELL:=/bin/bash

install:
	bash <(curl -sL https://github.com/Athesto/CLI_Checker/raw/main/install.sh)

uninstall:
	sudo rm -rf /opt/checker/
	sudo rm /usr/local/bin/checker

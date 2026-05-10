autosub:
	dnf -y install rpm-build rpmdevtools libcurl-devel libcurl
	spectool -g -R $(spec)/autosub.spec
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec)/autosub.spec

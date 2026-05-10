autosubqt:
	dnf -y install rpm-build rpmdevtools
	spectool -g -R $(spec)/autosubqt.spec
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec)/autosubqt.spec

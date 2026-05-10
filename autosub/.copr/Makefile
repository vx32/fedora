srpm:
        dnf -y install rpm-build rpmdevtools libcurl-devel libcurl
        spectool -g -R autosub.spec
        rpmbuild -bs --define "_srcrpmdir $(outdir)" autosub.spec

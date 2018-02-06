# Copyright (c) Sydney Erickson 2017
import os

import buildlib
import buildsettings

os.chdir(buildsettings.buildbase + "/pkg-src")

buildlib.execute_shell("tar -xvf dmd-2.078.1.tar.gz")
os.chdir("dmd-2.078.1")	
buildlib.execute_shell("make -f posix.mak AUTO_BOOTSTRAP=1")
buildlib.execute_shell("make install -f posix.mak INSTALL_DIR=$PWD/installdir AUTO_BOOTSTRAP=1")
buildlib.execute_shell("cp installdir/osx/bin/dmd {}/bin/dmd".format(buildsettings.builddir))
# Copyright (c) Sydney Erickson 2017
import buildlib
import buildsettings

buildlib.build_configure("git-2.15.1.tar.gz", "", presetup_command="make configure")
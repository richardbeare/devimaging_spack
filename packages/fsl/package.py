# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install fslinstaller-py
#
# You can edit this file again by typing:
#
#     spack edit fslinstaller-py
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from spack.util.environment import EnvironmentModifications

import os
import stat

class Fsl(Package):
    """FSL prebuilt"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://fsl.fmrib.ox.ac.uk/"
    url = "https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # We're fetching the installer, which is the same for all versions - i.e 
    # a common checksum. Doesn't appear to be a way of disabling at this level,
    # perhaps from the spack commandline
    checksum = "ea53c1821c7e397668ea7be6cb1417ee55bdf565c7600fdff7d9b05597418e52"
    version("6.0.6.5", checksum, expand = False)
    version("6.0.7.12", checksum ,expand = False)

    # FIXME: Add dependencies if required.
    depends_on("miniconda3", type = ("build", "run"))

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        
        runfile = join_path(self.stage.source_path, 'fslinstaller.py')
        arguments = [runfile,
                "-s",
                "-m",
                "--fslversion",
                str(self.version),
                "--miniconda",
                self.spec["miniconda3"].prefix,
                "--dest",
                join_path(self.prefix, "FSL"),
                "--extras_dir",
                join_path(self.prefix, "FSL", "envs")]
        install_shell = which("python3")
        install_shell(*arguments)
        fslsetup = join_path(self.prefix, "FSL", "etc", "fslconf", "fsl.sh")
        os.chmod(fslsetup, stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH | stat.S_IRGRP | stat.S_IRUSR | stat.S_IROTH)

    def setup_run_environment(self, env):
        # Set the environment variables after copying tree
        env.set("FSLDIR", join_path(self.prefix, "FSL"))
        env.prepend_path("PATH", join_path(self.prefix, "FSL", "share", "fsl", "bin"))
        fslsetup = join_path(self.prefix, "FSL", "etc", "fslconf", "fsl.sh")
        print(fslsetup)
        if os.path.isfile(fslsetup):
            # needs to be executable
            env.extend(EnvironmentModifications.from_sourcing_file(fslsetup))


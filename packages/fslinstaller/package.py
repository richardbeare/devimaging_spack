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
import os

class Fslinstaller(Package):
    """FSL prebuilt"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions and checksums here.
    version("6.0.7.12", "ee0b6cefbf9a2a4596fa1bc21a32ecbff40af833fca532600c4106cee29360f2" ,expand = False)

    # FIXME: Add dependencies if required.
    depends_on("miniconda3", type = ("build", "run"))

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        
        runfile = join_path(self.stage.source_path, 'fslinstaller.py')
        arguments = [runfile,
                "-s",
                "-m",
                "--fslversion",
                "6.0.7.12",
                "--miniconda",
                self.spec["miniconda3"].prefix,
                "--dest",
                join_path(self.prefix, "FSL"),
                "--extras_dir",
                join_path(self.prefix, "FSL", "envs")]
        install_shell = which("python3")
        install_shell(*arguments)

    def setup_run_environment(self, env):
        # Set the environment variables after copying tree
        env.set("FSLDIR", join_path(self.prefix, "FSL"))
        env.prepend_path("PATH", join_path(self.prefix, "FSL", "share", "fsl", "bin"))
        fslsetup = join_path(self.prefix, "etc", "fslconf", "fsl.sh")

        if os.path.isfile(fslsetup):
            env.extend(EnvironmentModifications.from_sourcing_file(fslsetup))


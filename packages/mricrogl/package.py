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
#     spack install mricrogl
#
# You can edit this file again by typing:
#
#     spack edit mricrogl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Mricrogl(Package):
    """MRIcroGL : medical image viewer."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/rordenlab/MRIcroGL/releases/download/v1.2.20220720/MRIcroGL_linux.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.2.20220720", sha256="e2ee9805622b2053712b9229545c0e55fbbdcddf8217cf8c884337c8b816276a")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix)

    def install(self, spec, prefix):
        # inspired by oracle instant client
        # will be extracted automatically
        install_tree("./", prefix)


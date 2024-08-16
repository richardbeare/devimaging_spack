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
#     spack install smt
#
# You can edit this file again by typing:
#
#     spack edit smt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Smt(CMakePackage):
    """Spherical Mean Technique - microscopic diffusion anisotropy imaging"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ekaden/smt"
    #url = "https://github.com/ekaden/smt/archive/refs/tags/v0.4.tar.gz"
    git = "https://github.com/ekaden/smt.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.4", tag="v0.4")

    # FIXME: Add dependencies if required.
    depends_on("cmake", type = ("build"))
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

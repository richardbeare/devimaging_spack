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
#     spack install dcm
#
# You can edit this file again by typing:
#
#     spack edit dcm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDcm2bids(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    # url = "https://pypi.org/project/dcm2bids"
    #url = "https://github.com/UNFmontreal/Dcm2Bids/archive/refs/tags/3.2.0.tar.gz"
    pypi = "dcm2bids/dcm2bids-3.2.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("3.2.0", sha256="f04a6d0fea604901fc71495a91bf78f4acd9cf5d4d9af1d3b51ba47616c02407")
    version("3.1.1", sha256="c9ee032d8b488e632820d050fd5fbad8c9d062a7722b1d43fdef74d535b02d05")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("python@3.11", type = ("build", "run"), when="@3.2.0:")
    depends_on("py-setuptools", type="build")


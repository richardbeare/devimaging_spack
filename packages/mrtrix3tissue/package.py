# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mrtrix3tissue(Package):
    """MRtrix provides a set of tools to perform various advanced diffusion MRI
    analyses, including constrained spherical deconvolution (CSD),
    probabilistic tractography, track-density imaging, and apparent fibre
    density."""

    homepage = "https://www.mrtrix.org/"
    #url = "https://github.com/3Tissue/mrtrix3/archive/refs/tags/3.0.3.tar.gz"
    git = "https://github.com/3Tissue/MRTrix3Tissue.git"

    license("MPL-2.0")


    version(
        "5.2.9",
        commit = "f8ba0e3fa17cb3b6bb51bcc4939cde83243b8f4c",
        preferred=True,
    )

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("glu")
    depends_on("qt+opengl@4.7:")
    # MRTrix <= 3.0.3 can't build with eigen >= 3.4 due to conflicting declarations
    depends_on("eigen@3.3", when="@5.2.9")
    depends_on("zlib-api")
    depends_on("libtiff")
    depends_on("fftw")

    patch("fix_includes.patch", when="@5.2.9")

    # from original mrtrix3 - not sure if we'll ever need it
    conflicts("%gcc@7:", when="@2017-09-25")  # MRtrix3/mrtrix3#1041

    def install(self, spec, prefix):
        configure = Executable("./configure")
        build = Executable("./build")
        configure()
        build()
        install_tree(".", prefix)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix)

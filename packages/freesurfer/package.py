# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack.package import *
from spack.util.environment import EnvironmentModifications
from spack.util.executable import Executable


class Freesurfer(Package):
    """Freesurfer is an open source software suite for processing and analyzing
    (human) brain MRI images."""

    homepage = "https://freesurfer.net/"

    # A license is required, but is free to obtain.
    license_required = True
    license_files = [".license"]

    maintainers("robgics")
    gitv81 = "https://github.com/freesurfer/freesurfer.git"
    version("8.1.0", git = gitv81, tag="v8.1.0", submodules = True, get_full_repo = True)
    version("7.4.1", sha256="313a96caeb246c5985f483633b5cf43f86ed8f7ccc6d6acfac8eedb638443010")
    version("7.4.0", sha256="6b65c2edf3b88973ced0324269a88966c541f221b799337c6570c38c2f884431")
    version("7.3.2", sha256="58518d3ee5abd2e05109208aed2eef145c4e3b994164df8c4e0033c1343b9e56")
    version("7.2.0", sha256="4cca78602f898bf633428b9d82cbb9b07e3ab97a86c620122050803779c86d62")
    version("7.1.1", sha256="6098b166fee8644f44f9ec88f3ffe88d05f2bc033cca60443e99e3e56f2e166b")
    version("7.1.0", sha256="1b8f26fe5c712433ddb74c47fe1895ed1d9fbff46cfae8aaae2697cb65ae8840")

    depends_on("mesa-glu")
    depends_on("qt+opengl@4.7:", when='@:8.0.99')
    depends_on("qt+opengl@5.15:", when='@8.1.0', type=('link')) 
    #depends_on("vtk@8.2.0", when='@8.1.0', type=('link', 'build')) 
    #depends_on("qt")
    depends_on("tcsh")
    depends_on("bc")
    depends_on("perl")

    depends_on('cmake@3.5:', type='build', when='@8.1.0')
    depends_on("git", type="build", when='@8.1.0')
    depends_on("git-annex", type="build", when='@8.1.0')
    #depends_on("minc-toolkit", type=("build", "link"), when='@8.1.0')
    #depends_on("python@3.8:", type=("build" ,"link", "run"), when='@8.1.0')
    #depends_on("py-pip", type=("build" ,"link", "run"), when='@8.1.0')

    def url_for_version(self, version):
        return "https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/{0}/freesurfer-linux-centos7_x86_64-{1}.tar.gz".format(
            version, version
        )

    def setup_run_environment(self, env):
        source_file = join_path(self.prefix, "SetUpFreeSurfer.sh")
        env.prepend_path("PATH", self.prefix.bin)
        env.set("FREESURFER_HOME", self.prefix)
        env.set("FREESURFER", self.prefix)
        env.set("SUBJECTS_DIR", join_path(self.prefix, "subjects"))
        env.set("FUNCTIONALS_DIR", join_path(self.prefix, "sessions"))
        env.append_path("PERL5LIB", join_path(self.prefix, "mni/share/perl5"))
        env.append_path("PATH", join_path(self.prefix, "mni/bin"))
        env.extend(EnvironmentModifications.from_sourcing_file(source_file))

    def install(self, spec, prefix):
        if spec.satisfies("@8.1.0"):
            annex_remote = "https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/repo/annex.git"
            git = Executable('git')
            git_annex = Executable('git-annex')
            py3 = Executable("python3")
            print(self.stage.source_path)
            with working_dir(self.stage.source_path):
                # add remote annex and fetch
                try:
                    git("remote", "add", "datasrc", annex_remote)
                    git("fetch", "datasrc")
                except ProcessError:
                    pass
                try:
                    git_annex("enableremote", "datasrc")
                except ProcessError:
                    pass
                try:
                    git_annex("get", ".")
                except ProcessError:
                    pass
                # do it twice, in case of failure
                try:
                    git_annex("get", ".")
                except ProcessError:
                    pass
            # build packages
            fs_packages_dir = join_path("/tmp/FS/freesurfer/", "fspackages")            
            #mkdirp(fs_packages_dir)
            #print(fs_packages_dir)
            #with working_dir(self.stage.source_path):
            #    py3("packages/build_packages.py", "-no-vtk", "-no-petsc", "-no-ann", "-no-gts", fs_packages_dir)
            cmake_args = []
            cmake_args += [f"-DBUILD_GUIS=ON"]
            cmake_args += [f"-DCMAKE_CXX_STANDARD=17", f"-DCMAKE_VERBOSE_MAKEFILE=ON"]
            cmake_args += [f"-DCMAKE_INSTALL_PREFIX={prefix}"]
            cmake_args += [f"-DCMAKE_BUILD_TYPE=Release"]
            cmake_args += [f"-DCMAKE_VERBOSE_MAKEFILE=ON"]
            cmake_args += [f"-DINFANT_MODULE=ON"]
            cmake_args += [f"-DDISTRIBUTE_FSPYTHON=ON"]
            cmake_args += [f"-DPYTHON_EXECUTABLE={fs_packages_dir}/fspython/3.8/bin/python3"]
            cmake_args += [f"-DFS_PACKAGES_DIR={fs_packages_dir}", f"-DITK_DIR={fs_packages_dir}/itk/5.4.5", f"-DVTK_DIR={fs_packages_dir}/vtk/8.2/", f"-DANN_DIR={fs_packages_dir}/ann/1.1.2"]
            with working_dir("spack-build", create=True):
                cmake("..", *cmake_args)
                make()
                make("install")
        else:
            scripts = ["sources.csh", "SetUpFreeSurfer.csh"]
            scripts.extend(glob.glob("bin/*"))
            scripts.extend(glob.glob("subjects/**/*", recursive=True))
            scripts.extend(glob.glob("fsfast/bin/*", recursive=True))
            scripts.extend(glob.glob("mni/bin/*", recursive=True))
            for s in scripts:
                if os.path.isfile(s):
                    filter_file(r"(\/usr)?(\/local?)\/bin\/tcsh", "/usr/bin/env -S tcsh", s)
                    filter_file(r"(\/usr)?(\/local?)\/bin\/csh", "/usr/bin/env -S csh", s)
                    filter_file(r"(\/usr)?(\/local)?\/bin\/perl", "/usr/bin/env -S perl", s)
            install_tree(".", prefix)

# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyFastjsonschema(PythonPackage):
    """Fast JSON schema validator for Python."""

    pypi = "fastjsonschema/fastjsonschema-2.15.1.tar.gz"

    version('2.15.1', sha256='671f36d225b3493629b5e789428660109528f373cf4b8a22bac6fa2f8191c2d2')

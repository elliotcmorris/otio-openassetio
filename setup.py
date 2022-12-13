# Copyright Contributors to the OpenTimelineIO project
# Copyright The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0

import setuptools

setuptools.setup(
    packages=setuptools.find_packages(),
    entry_points={"opentimelineio.plugins": "otio_openassetio = otio_openassetio"},
    package_data={
        "otio_openassetio": [
            "plugin_manifest.json",
        ],
    },
)

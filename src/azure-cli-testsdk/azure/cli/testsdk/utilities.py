# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure_devtools.scenario_tests import create_random_name as create_random_name_base


def create_random_name(prefix='clitest', length=24):
    create_random_name_base(prefix=prefix, length=length)


def find_recording_dir(test_file):
    """ Find the directory containing the recording of given test file based on current profile. """
    from azure.cli.core._profile import get_active_cloud, init_known_clouds
    from azure.cli.core.cloud import CloudNotRegisteredException
    try:
        api_profile = get_active_cloud().profile
    except CloudNotRegisteredException:
        init_known_clouds()
        api_profile = get_active_cloud().profile

    base_dir = os.path.join(os.path.dirname(test_file), 'recordings')
    return os.path.join(base_dir, api_profile)


def get_active_api_profile():
    from azure.cli.core._profile import get_active_cloud, init_known_clouds
    from azure.cli.core.cloud import CloudNotRegisteredException
    try:
        return get_active_cloud().profile
    except CloudNotRegisteredException:
        init_known_clouds()
        return get_active_cloud().profile

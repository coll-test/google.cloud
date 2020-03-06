#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_dns_managed_zone
description:
- A zone is a subtree of the DNS namespace under one administrative responsibility.
  A ManagedZone is a resource that represents a DNS zone hosted by the Cloud DNS service.
short_description: Creates a GCP ManagedZone
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  description:
    description:
    - A mutable string of at most 1024 characters associated with this resource for
      the user's convenience. Has no effect on the managed zone's function.
    required: true
    type: str
  dns_name:
    description:
    - The DNS name of this managed zone, for instance "example.com.".
    required: true
    type: str
  dnssec_config:
    description:
    - DNSSEC configuration.
    required: false
    type: dict
    suboptions:
      kind:
        description:
        - Identifies what kind of resource this is.
        required: false
        default: dns#managedZoneDnsSecConfig
        type: str
      non_existence:
        description:
        - Specifies the mechanism used to provide authenticated denial-of-existence
          responses.
        - 'Some valid choices include: "nsec", "nsec3"'
        required: false
        type: str
      state:
        description:
        - Specifies whether DNSSEC is enabled, and what mode it is in.
        - 'Some valid choices include: "off", "on", "transfer"'
        required: false
        type: str
      default_key_specs:
        description:
        - Specifies parameters that will be used for generating initial DnsKeys for
          this ManagedZone. If you provide a spec for keySigning or zoneSigning, you
          must also provide one for the other.
        required: false
        type: list
        suboptions:
          algorithm:
            description:
            - String mnemonic specifying the DNSSEC algorithm of this key.
            - 'Some valid choices include: "ecdsap256sha256", "ecdsap384sha384", "rsasha1",
              "rsasha256", "rsasha512"'
            required: false
            type: str
          key_length:
            description:
            - Length of the keys in bits.
            required: false
            type: int
          key_type:
            description:
            - Specifies whether this is a key signing key (KSK) or a zone signing
              key (ZSK). Key signing keys have the Secure Entry Point flag set and,
              when active, will only be used to sign resource record sets of type
              DNSKEY. Zone signing keys do not have the Secure Entry Point flag set
              and will be used to sign all other types of resource record sets. .
            - 'Some valid choices include: "keySigning", "zoneSigning"'
            required: false
            type: str
          kind:
            description:
            - Identifies what kind of resource this is.
            required: false
            default: dns#dnsKeySpec
            type: str
  name:
    description:
    - User assigned name for this resource.
    - Must be unique within the project.
    required: true
    type: str
  name_server_set:
    description:
    - Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet
      is a set of DNS name servers that all host the same ManagedZones. Most users
      will leave this field unset.
    required: false
    type: str
  labels:
    description:
    - A set of key/value label pairs to assign to this ManagedZone.
    required: false
    type: dict
  visibility:
    description:
    - 'The zone''s visibility: public zones are exposed to the Internet, while private
      zones are visible only to Virtual Private Cloud resources.'
    - 'Must be one of: `public`, `private`.'
    - 'Some valid choices include: "private", "public"'
    required: false
    default: public
    type: str
  private_visibility_config:
    description:
    - For privately visible zones, the set of Virtual Private Cloud resources that
      the zone is visible from.
    required: false
    type: dict
    suboptions:
      networks:
        description:
        - The list of VPC networks that can see this zone.
        required: true
        type: list
        suboptions:
          network_url:
            description:
            - The fully qualified URL of the VPC network to bind to.
            - This should be formatted like `U(https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`)
              .
            required: true
            type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/dns/api/v1/managedZones)'
- 'Managing Zones: U(https://cloud.google.com/dns/zones/)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a managed zone
  gcp_dns_managed_zone:
    name: test_object
    dns_name: test.somewild2.example.com.
    description: test zone
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
description:
  description:
  - A mutable string of at most 1024 characters associated with this resource for
    the user's convenience. Has no effect on the managed zone's function.
  returned: success
  type: str
dnsName:
  description:
  - The DNS name of this managed zone, for instance "example.com.".
  returned: success
  type: str
dnssecConfig:
  description:
  - DNSSEC configuration.
  returned: success
  type: complex
  contains:
    kind:
      description:
      - Identifies what kind of resource this is.
      returned: success
      type: str
    nonExistence:
      description:
      - Specifies the mechanism used to provide authenticated denial-of-existence
        responses.
      returned: success
      type: str
    state:
      description:
      - Specifies whether DNSSEC is enabled, and what mode it is in.
      returned: success
      type: str
    defaultKeySpecs:
      description:
      - Specifies parameters that will be used for generating initial DnsKeys for
        this ManagedZone. If you provide a spec for keySigning or zoneSigning, you
        must also provide one for the other.
      returned: success
      type: complex
      contains:
        algorithm:
          description:
          - String mnemonic specifying the DNSSEC algorithm of this key.
          returned: success
          type: str
        keyLength:
          description:
          - Length of the keys in bits.
          returned: success
          type: int
        keyType:
          description:
          - Specifies whether this is a key signing key (KSK) or a zone signing key
            (ZSK). Key signing keys have the Secure Entry Point flag set and, when
            active, will only be used to sign resource record sets of type DNSKEY.
            Zone signing keys do not have the Secure Entry Point flag set and will
            be used to sign all other types of resource record sets. .
          returned: success
          type: str
        kind:
          description:
          - Identifies what kind of resource this is.
          returned: success
          type: str
id:
  description:
  - Unique identifier for the resource; defined by the server.
  returned: success
  type: int
name:
  description:
  - User assigned name for this resource.
  - Must be unique within the project.
  returned: success
  type: str
nameServers:
  description:
  - Delegate your managed_zone to these virtual name servers; defined by the server
    .
  returned: success
  type: list
nameServerSet:
  description:
  - Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is
    a set of DNS name servers that all host the same ManagedZones. Most users will
    leave this field unset.
  returned: success
  type: str
creationTime:
  description:
  - The time that this resource was created on the server.
  - This is in RFC3339 text format.
  returned: success
  type: str
labels:
  description:
  - A set of key/value label pairs to assign to this ManagedZone.
  returned: success
  type: dict
visibility:
  description:
  - 'The zone''s visibility: public zones are exposed to the Internet, while private
    zones are visible only to Virtual Private Cloud resources.'
  - 'Must be one of: `public`, `private`.'
  returned: success
  type: str
privateVisibilityConfig:
  description:
  - For privately visible zones, the set of Virtual Private Cloud resources that the
    zone is visible from.
  returned: success
  type: complex
  contains:
    networks:
      description:
      - The list of VPC networks that can see this zone.
      returned: success
      type: complex
      contains:
        networkUrl:
          description:
          - The fully qualified URL of the VPC network to bind to.
          - This should be formatted like `U(https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`)
            .
          returned: success
          type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(required=True, type='str'),
            dns_name=dict(required=True, type='str'),
            dnssec_config=dict(
                type='dict',
                options=dict(
                    kind=dict(default='dns#managedZoneDnsSecConfig', type='str'),
                    non_existence=dict(type='str'),
                    state=dict(type='str'),
                    default_key_specs=dict(
                        type='list',
                        elements='dict',
                        options=dict(
                            algorithm=dict(type='str'), key_length=dict(type='int'), key_type=dict(type='str'), kind=dict(default='dns#dnsKeySpec', type='str')
                        ),
                    ),
                ),
            ),
            name=dict(required=True, type='str'),
            name_server_set=dict(type='str'),
            labels=dict(type='dict'),
            visibility=dict(default='public', type='str'),
            private_visibility_config=dict(
                type='dict', options=dict(networks=dict(required=True, type='list', elements='dict', options=dict(network_url=dict(required=True, type='str'))))
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']

    state = module.params['state']
    kind = 'dns#managedZone'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'dns')
    return return_if_object(module, auth.post(link, resource_to_request(module)), kind)


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if (
        response.get('description') != request.get('description')
        or response.get('labels') != request.get('labels')
        or response.get('privateVisibilityConfig') != request.get('privateVisibilityConfig')
    ):
        description_update(module, request, response)


def description_update(module, request, response):
    auth = GcpSession(module, 'dns')
    auth.patch(
        ''.join(["https://www.googleapis.com/dns/v1/", "projects/{project}/managedZones/{name}"]).format(**module.params),
        {
            u'description': module.params.get('description'),
            u'labels': module.params.get('labels'),
            u'privateVisibilityConfig': ManagedZonePrivatevisibilityconfig(module.params.get('private_visibility_config', {}), module).to_request(),
        },
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'dns')
    return return_if_object(module, auth.delete(link), kind)


def resource_to_request(module):
    request = {
        u'kind': 'dns#managedZone',
        u'description': module.params.get('description'),
        u'dnsName': module.params.get('dns_name'),
        u'dnssecConfig': ManagedZoneDnssecconfig(module.params.get('dnssec_config', {}), module).to_request(),
        u'name': module.params.get('name'),
        u'nameServerSet': module.params.get('name_server_set'),
        u'labels': module.params.get('labels'),
        u'visibility': module.params.get('visibility'),
        u'privateVisibilityConfig': ManagedZonePrivatevisibilityconfig(module.params.get('private_visibility_config', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'dns')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/dns/v1/projects/{project}/managedZones/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/dns/v1/projects/{project}/managedZones".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'description': response.get(u'description'),
        u'dnsName': response.get(u'dnsName'),
        u'dnssecConfig': ManagedZoneDnssecconfig(response.get(u'dnssecConfig', {}), module).from_response(),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'nameServers': response.get(u'nameServers'),
        u'nameServerSet': response.get(u'nameServerSet'),
        u'creationTime': response.get(u'creationTime'),
        u'labels': response.get(u'labels'),
        u'visibility': response.get(u'visibility'),
        u'privateVisibilityConfig': ManagedZonePrivatevisibilityconfig(response.get(u'privateVisibilityConfig', {}), module).from_response(),
    }


class ManagedZoneDnssecconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'kind': self.request.get('kind'),
                u'nonExistence': self.request.get('non_existence'),
                u'state': self.request.get('state'),
                u'defaultKeySpecs': ManagedZoneDefaultkeyspecsArray(self.request.get('default_key_specs', []), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'kind': self.request.get(u'kind'),
                u'nonExistence': self.request.get(u'nonExistence'),
                u'state': self.request.get(u'state'),
                u'defaultKeySpecs': ManagedZoneDefaultkeyspecsArray(self.request.get(u'defaultKeySpecs', []), self.module).from_response(),
            }
        )


class ManagedZoneDefaultkeyspecsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict(
            {u'algorithm': item.get('algorithm'), u'keyLength': item.get('key_length'), u'keyType': item.get('key_type'), u'kind': item.get('kind')}
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {u'algorithm': item.get(u'algorithm'), u'keyLength': item.get(u'keyLength'), u'keyType': item.get(u'keyType'), u'kind': item.get(u'kind')}
        )


class ManagedZonePrivatevisibilityconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'networks': ManagedZoneNetworksArray(self.request.get('networks', []), self.module).to_request()})

    def from_response(self):
        return remove_nones_from_dict({u'networks': ManagedZoneNetworksArray(self.request.get(u'networks', []), self.module).from_response()})


class ManagedZoneNetworksArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'networkUrl': item.get('network_url')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'networkUrl': item.get(u'networkUrl')})


if __name__ == '__main__':
    main()

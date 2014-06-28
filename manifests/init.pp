# Donatecommunity API setup manifest
#
# Copyright 2013 Tom Noonan II (TJNII)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class donatecommunity-api(
  $install_dir = '/opt/donatecommunity'
  ) {


  # Provided by the commonpackages class
  # https://github.com/TJNII/puppet-commonpackages
  include commonpackages::python::yaml
  include commonpackages::python::flask-restful

  file { [ "$install_dir",
           "$install_dir/bin" ]:
    ensure  => directory,
    recurse => true,
    owner   => root,
    group   => root,
    mode    => 755,
  }

  file { "$install_dir/bin/donatecommunity-api.py":
    ensure  => file,
    owner   => root,
    group   => root,
    mode    => 755,
    source  => "puppet:///modules/donatecommunity-api/bin/donatecommunity-api.py",
    require => File["$install_dir/bin"],
  }

}

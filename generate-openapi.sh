#!/usr/bin/env bash
#
# Copyright (C) 2023 Dremio
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
#

set -e

root_dir="$(realpath "$(dirname $0)")"

nessie_version="0.73.0"
min_python_version="3.8"

package_name="pynessie.api.rest"
package_dir="$(echo ${package_name} | sed 's/[.]/\//g' )"

target_src_dir="${root_dir}/${package_dir}"

if ! which openapi-python-client >/dev/null ; then
    echo "openapi-python-client executable not found"
    exit 1
fi

src_url="https://github.com/projectnessie/nessie/releases/download/nessie-${nessie_version}/nessie-openapi-${nessie_version}.yaml"
src_url="/home/snazy/devel/projectnessie/nessie/nessie/api/model/build/generated/openapi/META-INF/openapi/openapi.json"

echo "Generating OpenAPI model..."

openapi-python-client \
    generate \
    --path "${src_url}"


exit 0

datamodel-codegen \
    --output "${package_dir}/nessie_model.py" \
    --url "${src_url}" \
    --input-file-type yaml \
    --output-model-type pydantic_v2.BaseModel \
    --disable-timestamp \
    --class-name NessieModel \
    --use-annotated \
    --use-union-operator \
    --use-unique-items-as-set \
    --snake-case-field \
    --use-default-kwarg \
    --use-generic-container-types \
    --target-python-version "${min_python_version}" \
    --collapse-root-models \
    --use-subclass-enum \
    --reuse-model \
    --openapi-scopes parameters

exit 0

    --output-model-type pydantic_v2.BaseModel \
    --output-model-type msgspec.Struct \
    --output-model-type dataclasses.dataclass \
    --output-model-type typing.TypedDict \

    --disable-appending-item-suffix \
    --enable-faux-immutability \
    --use-schema-description \
    --use-field-description \

    --http-headers "Nessie-Client-Spec: 2" \


yaml_file="nessie-openapi.yaml"
yaml_path="${package_dir}/${yaml_file}"
echo "Downloading ${src_url}"
curl --location --output "${yaml_path}" "${src_url}"

    --input "${yaml_path}" \


tmp_gen_dir="${root_dir}/tmp/openapi-gen"
rm -rf "${tmp_gen_dir}"
mkdir -p "${tmp_gen_dir}"

echo "Generating code in ${tmp_gen_dir} ..."
podman run \
    --rm \
    --volume "${tmp_gen_dir}:/local" \
    docker.io/openapitools/openapi-generator-cli \
    generate \
    --input-spec "/local/${yaml_file}" \
    --generator-name python \
    --output "/local" \
    --package-name "${package_name}" \
    --model-package "../models"

rm -rf "${target_src_dir}"
mkdir -p "${target_src_dir}"

rm -rf ${package_dir}
mkdir -p "${package_dir}"
cp -r "${tmp_gen_dir}/${package_dir}" "${package_dir}/.."
cat <<! > pynessie/api/rest/internal/README.md
THIS DIRECTORY CONTAINS GENERATED CODE!
DO NOT EDIT OR ALTER!
!

rm -rf "${tmp_gen_dir}"

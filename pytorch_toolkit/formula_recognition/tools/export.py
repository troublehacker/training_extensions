"""
 Copyright (c) 2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import argparse

from tools.utils.get_config import get_config
from tools.utils.exporter import Exporter


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--config')
    return args.parse_args()


if __name__ == "__main__":
    args = parse_args()
    export_config = get_config(args.config, section='export')
    exporter = Exporter(export_config)
    exporter.export_encoder()
    exporter.export_decoder()
    print("Model succesfully exported to ONNX")
    if export_config.get("export_ir"):
        exporter.export_encoder_ir()
        exporter.export_decoder_ir()
        print("Model succesfully exported to OpenVINO IR")

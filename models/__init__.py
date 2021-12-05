# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .detr import build
from .detr_v1 import build_v1            ### wenchi


def build_model(args):
    return build(args)

## wenchi ###
def build_model_v1(args):
	return build_v1(args)
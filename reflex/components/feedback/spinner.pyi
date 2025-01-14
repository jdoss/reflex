"""Stub file for spinner.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Spinner(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, empty_color: Optional[Union[Var[str], str]] = None, label: Optional[Union[Var[str], str]] = None, speed: Optional[Union[Var[str], str]] = None, thickness: Optional[Union[Var[int], int]] = None, size: Optional[Union[Var[str], str]] = None, **props) -> "Spinner": ...  # type: ignore

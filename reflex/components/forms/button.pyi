"""Stub file for button.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, List, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Button(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, icon_spacing: Optional[Union[Var[int], int]] = None, is_active: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_full_width: Optional[Union[Var[bool], bool]] = None, is_loading: Optional[Union[Var[bool], bool]] = None, loading_text: Optional[Union[Var[str], str]] = None, size: Optional[Union[Var[str], str]] = None, variant: Optional[Union[Var[str], str]] = None, color_scheme: Optional[Union[Var[str], str]] = None, type_: Optional[Union[Var[str], str]] = None, invalid_children: Optional[List[str]] = None, **props) -> "Button": ...  # type: ignore

class ButtonGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, is_attached: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, spacing: Optional[Union[Var[int], int]] = None, **props) -> "ButtonGroup": ...  # type: ignore

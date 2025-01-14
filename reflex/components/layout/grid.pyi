"""Stub file for grid.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, List, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Grid(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, auto_columns: Optional[Union[Var[str], str]] = None, auto_flow: Optional[Union[Var[str], str]] = None, auto_rows: Optional[Union[Var[str], str]] = None, column: Optional[Union[Var[str], str]] = None, row: Optional[Union[Var[str], str]] = None, template_columns: Optional[Union[Var[str], str]] = None, template_rows: Optional[Union[Var[str], str]] = None, **props) -> "Grid": ...  # type: ignore

class GridItem(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, area: Optional[Union[Var[str], str]] = None, col_end: Optional[Union[Var[str], str]] = None, col_start: Optional[Union[Var[int], int]] = None, col_span: Optional[Union[Var[int], int]] = None, row_end: Optional[Union[Var[str], str]] = None, row_start: Optional[Union[Var[int], int]] = None, row_span: Optional[Union[Var[int], int]] = None, **props) -> "GridItem": ...  # type: ignore

class ResponsiveGrid(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, auto_columns: Optional[Union[Var[str], str]] = None, auto_flow: Optional[Union[Var[str], str]] = None, auto_rows: Optional[Union[Var[str], str]] = None, column: Optional[Union[Var[str], str]] = None, row: Optional[Union[Var[str], str]] = None, columns: Optional[Union[Var[List[int]], List[int]]] = None, min_child_width: Optional[Union[Var[str], str]] = None, spacing: Optional[Union[Var[str], str]] = None, spacing_x: Optional[Union[Var[str], str]] = None, spacing_y: Optional[Union[Var[str], str]] = None, template_areas: Optional[Union[Var[str], str]] = None, template_columns: Optional[Union[Var[str], str]] = None, template_rows: Optional[Union[Var[str], str]] = None, **props) -> "ResponsiveGrid": ...  # type: ignore

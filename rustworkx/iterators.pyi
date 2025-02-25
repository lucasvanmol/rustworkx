# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# This file contains only type annotations for PyO3 functions and classes
# For implementation details, see __init__.py and src/iterators.rs

from typing import (
    Any,
    Generic,
    ItemsView,
    KeysView,
    ValuesView,
    Iterator,
    Mapping,
    TypeVar,
    overload,
    final,
)
from abc import ABC
from collections.abc import Sequence
from typing_extensions import Self

import numpy as np

S = TypeVar("S")
T_co = TypeVar("T_co", covariant=True)

__all__ = [
    "NodeIndices",
    "PathLengthMapping",
    "PathMapping",
    "AllPairsPathLengthMapping",
    "AllPairsPathMapping",
    "BFSPredecessors",
    "BFSSuccessors",
    "EdgeIndexMap",
    "EdgeIndices",
    "Chains",
    "EdgeList",
    "NodeMap",
    "NodesCountMapping",
    "Pos2DMapping",
    "WeightedEdgeList",
    "CentralityMapping",
    "EdgeCentralityMapping",
    "BiconnectedComponents",
    "ProductNodeMap",
    "MultiplePathMapping",
    "AllPairsMultiplePathMapping",
]

class RustworkxCustomVecIter(Generic[T_co], Sequence[T_co], ABC):
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, index: int) -> T_co: ...
    @overload
    def __getitem__(self: Self, index: slice) -> Self: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: Sequence[T_co]) -> None: ...
    def __array__(self, _dt: np.dtype | None = ...) -> np.ndarray: ...

class RustworkxCustomHashMapIter(Generic[S, T_co], Mapping[S, T_co], ABC):
    def __init__(self) -> None: ...
    def items(self) -> ItemsView[S, T_co]: ...
    def keys(self) -> KeysView[S]: ...
    def values(self) -> ValuesView[T_co]: ...
    def __contains__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, index: S) -> T_co: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[S]: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: Mapping[S, T_co]) -> None: ...

@final
class NodeIndices(RustworkxCustomVecIter[int]): ...

@final
class PathLengthMapping(RustworkxCustomHashMapIter[int, float]): ...

@final
class PathMapping(RustworkxCustomHashMapIter[int, NodeIndices]): ...

@final
class AllPairsPathLengthMapping(RustworkxCustomHashMapIter[int, PathLengthMapping]): ...

@final
class AllPairsPathMapping(RustworkxCustomHashMapIter[int, PathMapping]): ...

@final
class BFSSuccessors(Generic[T_co], RustworkxCustomVecIter[tuple[T_co, list[T_co]]]): ...

@final
class BFSPredecessors(Generic[T_co], RustworkxCustomVecIter[tuple[T_co, list[T_co]]]): ...

@final
class EdgeIndexMap(Generic[T_co], RustworkxCustomHashMapIter[int, tuple[int, int, T_co]]): ...

@final
class EdgeIndices(RustworkxCustomVecIter[int]): ...

@final
class Chains(RustworkxCustomVecIter[EdgeIndices]): ...

@final
class EdgeList(RustworkxCustomVecIter[tuple[int, int]]): ...

@final
class NodeMap(RustworkxCustomHashMapIter[int, int]): ...

@final
class NodesCountMapping(RustworkxCustomHashMapIter[int, int]): ...

@final
class Pos2DMapping(RustworkxCustomHashMapIter[int, tuple[float, float]]): ...

@final
class WeightedEdgeList(Generic[T_co], RustworkxCustomVecIter[tuple[int, int, T_co]]): ...

@final
class CentralityMapping(RustworkxCustomHashMapIter[int, float]): ...

@final
class EdgeCentralityMapping(RustworkxCustomHashMapIter[int, float]): ...

@final
class BiconnectedComponents(RustworkxCustomHashMapIter[tuple[int, int], int]): ...

@final
class ProductNodeMap(RustworkxCustomHashMapIter[tuple[int, int], int]): ...

@final
class MultiplePathMapping(RustworkxCustomHashMapIter[int, list[list[int]]]): ...

@final
class AllPairsMultiplePathMapping(RustworkxCustomHashMapIter[int, MultiplePathMapping]): ...

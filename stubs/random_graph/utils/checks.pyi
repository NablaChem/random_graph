import collections
import typing

def valid_bipartite_graph(nx: int, ny: int, edges: typing.List[typing.Tuple[int, int]]) -> bool: ...
def valid_directed_graph(n: int, edges: typing.List[typing.Tuple[int, int]]) -> bool: ...
def valid_multi_hypergraph(n: int, edges: typing.List[typing.Set[int]]) -> bool: ...
def valid_simple_graph(n: int, edges: typing.List[typing.Set[int]]) -> bool: ...
def all_unique(x: typing.Iterable[collections.abc.Hashable]) -> bool: ...
def bipartite_degree_sequence_graphical(dx: typing.Sequence[int], dy: typing.Sequence[int]) -> bool: ...
def directed_degree_sequence_graphical(degree_sequence: typing.Sequence[typing.Tuple[int, int]]) -> bool: ...
def simple_degree_sequence_graphical(degree_sequence: typing.Sequence[int]) -> bool: ...

from src.graph_utils import Graph
import pytest


# Use pytest.fixture to instantiate a new Graph class for each test
@pytest.fixture
def graph():
    return Graph()


def test_add_edge(graph):
    graph.add_edge('A', 'B')
    assert graph.get_edges('A') == ['B']


def test_get_edges(graph):
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    assert graph.get_edges('A') == ['B', 'C']


def test_add_duplicate_edge(graph):
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'B')
    assert graph.get_edges('A') == ['B']


def test_add_self_edge(graph):
    graph.add_edge('A', 'A')
    assert graph.get_edges('A') == ['A']


def test_add_nonexistent_node(graph):
    graph.add_edge('A', 'B')
    assert graph.get_edges('C') == []


def test_invalid_input(graph):
    with pytest.raises(TypeError):
        graph.add_edge(None, 'B')

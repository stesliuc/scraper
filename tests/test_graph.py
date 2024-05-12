from src.graph_utils import Graph
import pytest


# Use pytest.fixture to instantiate a new Graph class for each test
@pytest.fixture
def graph():
    return Graph()


def test_add_node(graph):
    graph.add_node('A')
    assert len(graph.get_edges('A')) == 0, "Single node edge set failed"
    assert len(graph.get_content('A')) == 0, "Single node content set failed"


def test_add_edge(graph):
    graph.add_edge('A', 'B')
    assert graph.get_edges('A') == ['B'], "Edge did not add"


def test_get_edges(graph):
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    assert graph.get_edges('A') == ['B', 'C'], "Edge did not add"


def test_add_duplicate_edge(graph):
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'B')
    assert graph.get_edges('A') == ['B'], "Duplicate edges found"


def test_add_self_edge(graph):
    graph.add_edge('A', 'A')
    assert graph.get_edges('A') == ['A'], "Self edge not created"


def test_add_nonexistent_node(graph):
    graph.add_edge('A', 'B')
    assert graph.get_edges('C') == [], "Edges in empty node"


def test_add_content(graph):
    graph.add_node('A')
    graph.add_content('A', "Test string")
    graph.add_edge('A', 'B')
    assert graph.get_content('A')[0] == "Test string", "Edg changed cntnt"


def test_invalid_input(graph):
    with pytest.raises(TypeError):
        graph.add_edge(None, 'B')

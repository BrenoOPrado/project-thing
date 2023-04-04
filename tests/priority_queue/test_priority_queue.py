from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    queue = PriorityQueue()
    valueTest = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['linha1', 'linha2', 'linha3'],
    }
    valueTest2 = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": [...],
    }

    assert queue.__len__() == 0
    assert queue.is_priority(valueTest) is True
    assert queue.is_priority(valueTest2) is False
    assert queue.dequeue() is None
    assert queue.enqueue(valueTest) is None
    assert queue.enqueue(valueTest2) is None
    assert queue.__len__() == 2
    assert queue.search(0) is valueTest
    assert queue.search(1) is valueTest2
    assert queue.dequeue() is valueTest
    assert queue.__len__() == 1
    assert queue.dequeue() is valueTest2
    assert queue.__len__() == 0

    with pytest.raises(IndexError):
        assert queue.search(100) is None
        assert queue.search(-1) is None

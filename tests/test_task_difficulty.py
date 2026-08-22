"""Уровень сложности есть у каждой задачи и совпадает с базовой для «исправь»."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.fix_tasks_defs import FIX_TASK_DEFS
from data.registry import TASKS_BY_TOPIC
from data.tasks.common import VALID_DIFFICULTIES, infer_difficulty


def test_infer_difficulty_by_content():
    assert infer_difficulty("io-01") == "easy"
    assert infer_difficulty("io-11") == "easy"
    assert infer_difficulty("io-35") == "medium"
    assert infer_difficulty("numbers-22") == "medium"
    assert infer_difficulty("numbers-35") == "easy"
    assert infer_difficulty("cond-23") == "medium"
    assert infer_difficulty("cond-26") == "hard"
    assert infer_difficulty("str-33") == "easy"
    assert infer_difficulty("str-34") == "easy"
    assert infer_difficulty("list-35") == "medium"
    assert infer_difficulty("while-31") == "hard"
    assert infer_difficulty("io-41") == "hard"
    assert infer_difficulty("list-50") == "hard"


def test_infer_difficulty_uses_based_on():
    assert infer_difficulty("io-fix-10", based_on="io-35") == "medium"
    assert infer_difficulty("io-fix-01", based_on="io-01") == "easy"
    assert infer_difficulty("cond-fix-05", based_on="cond-26") == "hard"


def test_every_task_has_difficulty():
    for topic_id, tasks in TASKS_BY_TOPIC.items():
        assert tasks, topic_id
        for task in tasks:
            assert task.get("difficulty") in VALID_DIFFICULTIES, task["id"]


def test_fix_tasks_inherit_base_difficulty():
    for topic_id, defs in FIX_TASK_DEFS.items():
        by_id = {task["id"]: task for task in TASKS_BY_TOPIC[topic_id]}
        for fix in defs:
            base = by_id[fix["based_on"]]
            merged = by_id[fix["id"]]
            assert merged["difficulty"] == base["difficulty"], fix["id"]


def test_fix_task_comes_before_similar_task():
    for topic_id, defs in FIX_TASK_DEFS.items():
        ids = [task["id"] for task in TASKS_BY_TOPIC[topic_id]]
        for fix in defs:
            assert ids.index(fix["id"]) == ids.index(fix["based_on"]) - 1, fix["id"]


def test_tasks_ordered_by_difficulty():
    order = {"easy": 0, "medium": 1, "hard": 2}
    for topic_id, tasks in TASKS_BY_TOPIC.items():
        ranks = [order[task["difficulty"]] for task in tasks]
        assert ranks == sorted(ranks), topic_id


if __name__ == "__main__":
    test_infer_difficulty_by_content()
    test_infer_difficulty_uses_based_on()
    test_every_task_has_difficulty()
    test_fix_tasks_inherit_base_difficulty()
    test_fix_task_comes_before_similar_task()
    test_tasks_ordered_by_difficulty()
    print("OK")

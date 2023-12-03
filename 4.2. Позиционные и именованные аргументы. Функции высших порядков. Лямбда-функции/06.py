"""
Кофейня
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_05/0a1SSW7uQ4
Status: not Solved.
"""


from typing import Dict, List, Union

in_stock = {"coffee": 1, "milk": 2, "cream": 3}


def order(*args, **kwargs: Union[Dict[str, int], List[str]]) -> str:
    OUT_OF_STOCK_MESSAGE = "К сожалению, не можем предложить Вам напиток"
    RECIPES = {
        "Эспрессо": {
            "coffee": 1,
            "milk": 0,
            "cream": 0,
        },
        "Капучино": {
            "coffee": 1,
            "milk": 3,
            "cream": 0,
        },
        "Макиато": {
            "coffee": 2,
            "milk": 1,
            "cream": 0,
        },
        "Кофе по-венски": {
            "coffee": 1,
            "milk": 0,
            "cream": 2,
        },
        "Латте Макиато": {
            "coffee": 1,
            "milk": 2,
            "cream": 1,
        },
        "Кон Панна": {
            "coffee": 1,
            "milk": 0,
            "cream": 1,
        },
    }
    t: Dict[str, int] = in_stock
    answer = []
    orders: List[str] = kwargs.get("order") or args.get("order")
    for order in orders:
        current_recipe = RECIPES[order]
        diff_dict = {
            key: t[key] - current_recipe.get(key, 0) for key in t.keys()
        }
        if all([value >= 0 for value in diff_dict.values()]):
            t = diff_dict
            answer.append(order)
        else:
            return "\n".join(i for i in answer) + '\n' + OUT_OF_STOCK_MESSAGE
    return "\n".join(i for i in answer)


if __name__ == "__main__":
    assert (
        order(
            # in_stock={"coffee": 1, "milk": 2, "cream": 3},
            order=(
                "Эспрессо",
                "Капучино",
                "Макиато",
                # "Кофе по-венски",
                # "Латте Макиато",
                # "Кон Панна",
            ),
        )
        == "Эспрессо\nК сожалению, не можем предложить Вам напиток"
    )

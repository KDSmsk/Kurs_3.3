from func import filter_date
from func import filter_date_2
from func import filter_score
from func import sort_obj_from_date
import transction_obj as tr_obj

def test_filter_date():
    assert filter_date("2019-07-03T18:35:29.512364") == "03.07.2019"

def test_filter_date2():
    assert filter_date_2("2019-07-03T18:35:29.512364") == ['2019', '07', '03']

def test_filter_score():
    assert filter_score("Счет 33407225454123927865") == 'Счет 3340 7225 4541 ХХХХ 7865 '
    assert filter_score("Visa Platinum 5355133159258236") == 'Visa Platinum 5355 1331 ХХХХ 8236 '

def test_filter_sort_obj_from_date():
    transaction_obj = tr_obj.transaction()
    JSON = {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {
              "amount": "96900.90",
              "currency": {
                "name": "руб.",
                "code": "RUB"
                          }
                                },
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215"
            }
    transaction_obj.set_param_from_json(JSON)
    assert transaction_obj.get_id() == 634356296
    assert transaction_obj.get_date() == "2018-01-21T01:10:28.317704"
    assert transaction_obj.get_state() == "EXECUTED"
    assert transaction_obj.get_many_id() == "RUB"
    assert transaction_obj.get_many_cont() == "96900.90"
    assert transaction_obj.get_description() == "Перевод со счета на счет"
    assert transaction_obj.get_from() == "Счет 33407225454123927865"
    assert transaction_obj.get_to() == "Счет 79619011266276091215"

def test_sort_obj_from_date():
    transaction_obj = tr_obj.transaction()
    JSON = {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {
              "amount": "96900.90",
              "currency": {
                "name": "руб.",
                "code": "RUB"
                          }
                                },
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215"
            }
    transaction_obj.set_param_from_json(JSON)
    assert sort_obj_from_date(transaction_obj) == '20180121'

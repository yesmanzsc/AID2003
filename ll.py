
def calculate_cost_of_travel (person_number,money) :
    """
    计算旅游费用
    :param person_number: 旅游人数
    :param money: 旅游费用
    :return: 总费用
    """
    if person_number > 5:
        return person_number*260
    else:
        return person_number*300


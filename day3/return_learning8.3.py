def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# 编写一个名为 city_country()的函数，它接受城市的名称及其所属的
# 国家。这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对调用这个函数，并打印它返回的值
def city_country(city, country):
    """返回一个格式类似于下面这样的字符串："Santiago, Chile" """
    return city.title() + ', ' + country.title()
if __name__ == '__main__':
    musician = get_formatted_name('john', 'hooker')
    print(musician)
    musician = build_person('jimi', 'hendrix', age=27)

    print(musician)
    city_country= city_country('santiago', 'chile')
    print(city_country)
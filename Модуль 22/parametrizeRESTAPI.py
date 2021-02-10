# Дополнение в модуль 20
import pytest, json, requests


def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
   """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
   запроса и результат в формате JSON с данными добавленного питомца"""

   data = MultipartEncoder(
       fields={
           'name': name,
           'animal_type': animal_type,
           'age': age
       })
   headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

   res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
   status = res.status_code
   result = ""
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   print(result)
   return status, result





def is_age_valid(age):
   # Проверяем, что возраст - это число от 1 до 49 и целое
   return age.isdigit() \
          and 0 < int(age) < 50 \
          and float(age) == int(age)


@pytest.mark.parametrize("name"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type"
   , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
   , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("age"
   , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
   , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
def test_add_new_pet_simple(name, animal_type, age):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '' or animal_type == '' or is_age_valid():
       assert pytest.status == 400
   else:
       assert pytest.status == 200
       assert result['name'] == name
       assert result['age'] == age
       assert result['animal_type'] == animal_type
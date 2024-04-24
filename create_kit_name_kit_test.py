import sender_stand_request
import data
from data import user_body


def positive_assert(param):
    pass


def test_create_user_1_letter_in_first_name_get_success_response():
    # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    kit_body = {"name": "a"}

    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""


def test_create_user_511_letter_in_first_name_get_success_response():
    positive_assert(data.letter_511)


def test_create_user_0_letter_in_first_name_get_error_response():
    negative_assert_no_firstname(data.blank_space)


def test_create_user_512_letter_in_first_name_get_error_response():
    negative_assert_no_firstname(data.letter_512)


def test_create_user_special_letter_in_first_name_get_error_response():
    positive_assert(data.special_letter)


def test_create_user_space_in_first_name_get_error_response():
    positive_assert(data.space_first_name)


def test_create_user_numbers_in_first_name_get_error_response():
    positive_assert(data.numbers_string)


def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = data.blank_space
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


def test_create_user_numeros_in_first_name_get_error_response():
    user_body = data.numbers
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

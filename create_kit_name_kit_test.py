import sender_stand_request
import data


def positive_assert(kit_body):

    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.create_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201

    assert user_response.json()["name"] == kit_body["name"]


def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert(data.name)


def test_create_kit_511_in_kit_body_letter_get_success_response():
    positive_assert(data.letter_511)


def test_create_kit_0_letter_in_kit_body_get_error_response():
    negative_assert_no_kit_body(data.blank_space)


def test_create_kit_512_letter_in_kit_body_name_get_error_response():
    negative_assert_no_kit_body(data.letter_512)


def test_create_kit_special_letter_in_kit_body__get_error_response():
    positive_assert(data.special_letter)


def test_create_kit_space_in_kit_body_get_error_response():
    positive_assert(data.space_first_name)


def test_create_kit_numbers_string_in_kit_body_get_error_response():
    positive_assert(data.numbers_string)


def negative_assert_no_kit_body(kit_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.create_client_kit(kit_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400


def test_create_kit_empty_in_kit_body_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = data.blank_space
    # Comprueba la respuesta
    negative_assert_no_kit_body(kit_body)


def test_create_kit_numbers_in_kit_body_get_error_response():
    kit_body = data.numbers
    # Comprueba la respuesta
    negative_assert_no_kit_body(kit_body)

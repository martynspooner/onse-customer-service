from behave import when, given

from customer_service.model.customer import Customer


@given('customer "{name}" with ID "{customer_id:d}" exists')
def create_customer(context, name, customer_id):
    (first_name, surname) = name.split(' ', 2)

    customer = Customer(customer_id=customer_id,
                        first_name=first_name,
                        surname=surname)

    context.customer_repository.store(customer)


@when('customer id "{customer_id}" changes name to "{new_name}"')
def update_customer(context, customer_id, new_name):
    (first_name, surname) = new_name.split(' ', 2)
    response = context.web_client.post(
        '/customers/update/' + customer_id + '/',
        json={'firstName': first_name, 'surname': surname})

    body = response.get_json()
    assert f"{body['firstName']} {body['surname']}" == new_name

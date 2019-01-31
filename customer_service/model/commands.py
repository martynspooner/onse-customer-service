from customer_service.model.customer import Customer


def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)


def update_customer(customer_id, customer_repository,
                    new_fist_name, new_surname):
    customer = get_customer(customer_id, customer_repository)
    customer.first_name = new_fist_name
    customer.surname = new_surname
    return customer

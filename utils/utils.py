def validate_fields(fields, Model):
    """
    Given a list of fields and Model, raise exception
    if a given field is not present into the list
    :param fields:
    :param model:
    :return:
    """

    valid_fields = Model.get_allowed_group_fields()
    for field in fields:
        if field not in valid_fields:
            raise Exception('Invalid field!')

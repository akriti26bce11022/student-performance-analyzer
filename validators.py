def is_valid_marks(marks):
    return 0 <= marks <= 100


def is_valid_classes(total_classes, attended_classes):
    if total_classes <= 0:
        return False

    if attended_classes < 0:
        return False

    if attended_classes > total_classes:
        return False

    return True
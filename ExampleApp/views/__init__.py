from ExampleApp.orms import get_orm_impl


class CommonCRUD(get_orm_impl()):
    """
    公共的CRUD类
    """
    model = None



if __name__ == '__main__':
    CommonCRUD.test_print()
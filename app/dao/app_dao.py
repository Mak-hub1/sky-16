from app.dao import database
from sqlalchemy import or_  # , desc, func


class AppDAO:

    def get_all_users(self):
        data = database.db.session().query(database.User).all()
        result = list(map(lambda x: x.to_dict(), data))
        return result

    def get_user_by_id(self, id: int) -> dict[str: any]:
        data = database.db.session().query(database.User).filter(database.User.id == id).first()
        if data is None:
            return {}
        return data.to_dict()

    def get_all_orders(self):
        data = database.db.session().query(database.Order).all()
        result = list(map(lambda x: x.to_dict(), data))
        return result

    def get_orders_by_id(self, id: int) -> dict[str: any]:
        data = database.db.session().query(database.Order).filter(database.Order.id == id).first()
        if data is None:
            return {}
        return data.to_dict()

    def get_all_offers(self):
        data = database.db.session().query(database.Offer).all()
        result = list(map(lambda x: x.to_dict(), data))
        return result

    def get_offer_by_id(self, id: int) -> dict[str: any]:
        data = database.db.session().query(database.Offer).filter(database.Offer.id == id).first()
        if data is None:
            return {}
        return data.to_dict()

    def add_user(self, json: dict[str, str]) -> str:
        try:
            user = database.User(**json)
            with database.db.session.begin():
                database.db.session.add_all([user])
            return f'Пользователь {user.last_name} добавлен'
        except Exception:
            return 'Не удалось добавить пользователя'

    def update_user(self, id: int, json: dict[str, str]) -> str:
        user = database.User.query.get(id)
        try:
            user.update_user(json)
            database.db.session.add(user)
            database.db.session.commit()
            return 'Пользователь обновлен'
        except Exception:
            return 'Не удалось обновить пользователя'

    def delete_user(self, id: int) -> str:
        user = database.User.query.get(id)
        try:
            database.db.session.delete(user)
            database.db.session.commit()
            return f'Пользователь удален! '
        except Exception:
            return 'Не удалось удалить пользователя'

    def add_order(self, json: dict[str, str]) -> str:
        try:
            model = database.Order(**json)
            with database.db.session.begin():
                database.db.session.add_all([model])
            return f'Заказ добавлен'
        except Exception:
            return 'Не удалось добавить заказ'

    def update_order(self, id: int, json: dict[str, str]) -> str:
        model = database.Order.query.get(id)
        try:
            model.update(json)
            database.db.session.add(model)
            database.db.session.commit()
            return 'Заказ обновлен'
        except Exception:
            return 'Не удалось обновить заказ'

    def delete_order(self, id: int) -> str:
        model = database.Order.query.get(id)
        try:
            database.db.session.delete(model)
            database.db.session.commit()
            return f'Заказ удаден! '
        except Exception:
            return 'Не удалось удалить заказ'

    def add_offer(self, json: dict[str, str]) -> str:
        try:
            model = database.Offer(**json)
            with database.db.session.begin():
                database.db.session.add_all([model])
            return f'Предложение добавлено'
        except Exception:
            return 'Не удалось добавить предложение'

    def update_offer(self, id: int, json: dict[str, str]) -> str:
        model = database.Offer.query.get(id)
        try:
            model.update(json)
            database.db.session.add(model)
            database.db.session.commit()
            return 'Предложение обновлено'
        except Exception:
            return 'Не удалось обновить предложение'

    def delete_offer(self, id: int) -> str:
        model = database.Offer.query.get(id)
        try:
            database.db.session.delete(model)
            database.db.session.commit()
            return f'Предложение удалено! '
        except Exception:
            return 'Не удалось удалить предложение'

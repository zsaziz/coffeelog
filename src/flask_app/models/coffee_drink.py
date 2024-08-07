# 3p lib
from sqlalchemy import desc

# local lib
from data.create_coffee_drink import CreateCoffeeDrink
from data.update_coffee_drink import UpdateCoffeeDrink
from flask_app import db
from flask_app.models.coffee_beans_json_encoder import CoffeeBeansJsonEncoder
from flask_app.models.additives_json_encoder import AdditivesJsonEncoder
from flask_app.models.user import User
from utils.common_utils import get_current_local_datetime
from utils.logging_utils import get_logger

# python lib
from collections import OrderedDict

log = get_logger(__name__)


class CoffeeDrink(db.Model):
    """Flask DB class object for CoffeeDrink metadata
    """

    COFFEE_DRINK_NAME = 'coffee_drink'
    COFFEE_DRINK_TABLE_NAME = 'coffeelog-coffeedrink-metadata'

    BREW_ID = 'brew_id'
    USER_ID = 'user_id'
    DRINK_NAME = 'drink_name'
    QUANTITY_IN_FL_OZ = 'quantity_in_fl_oz'
    MILK_OPTIONS = 'milk_options'
    ADDITIVES = 'additives'
    COFFEE_BEANS = 'coffee_beans'
    CAFE = 'cafe'
    DRINK_TIME = 'drink_time'
    CREATED_TIME = 'created_time'
    # sql internal attribute
    SQL_INSTANCE_STATE = '_sa_instance_state'

    # Custom attribute order map for CoffeeDrink with rankings
    _PUBLIC_ATTRIBUTE_ORDER = {attribute: ranking for ranking, attribute in enumerate([
        DRINK_NAME,
        QUANTITY_IN_FL_OZ,
        MILK_OPTIONS,
        ADDITIVES,
        DRINK_TIME,
        COFFEE_BEANS,
        CAFE,
    ])}

    _REMOVED_ATTRIBUTES = [
        BREW_ID,
        USER_ID,
        CREATED_TIME,
        SQL_INSTANCE_STATE
    ]


    __tablename__ = COFFEE_DRINK_TABLE_NAME

    # Primary key - consists of user_id and created_time
    brew_id = db.Column(db.String, nullable=False, unique=True, primary_key=True, autoincrement=False)

    # Required attributes
    user_id = db.Column(db.String, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    drink_name = db.Column(db.String, nullable=False)
    quantity_in_fl_oz = db.Column(db.Integer, nullable=False)
    drink_time = db.Column(db.DateTime, nullable=False)

    # Optional attributes
    milk_options = db.Column(db.String)
    additives = db.Column(AdditivesJsonEncoder)
    coffee_beans = db.Column(CoffeeBeansJsonEncoder)
    cafe = db.Column(db.String)

    def __init__(self, create_coffee_drink: CreateCoffeeDrink, user_id: str):
        self.user_id = user_id
        self.created_time = get_current_local_datetime()

        self.brew_id = _generate_brew_id(self)

        for attr_name, attr_val in create_coffee_drink.__dict__.items():
            if attr_name == CreateCoffeeDrink.DRINK_TIME:
                if attr_val:
                    setattr(self, attr_name, attr_val)
                else:
                    # Default drink_time to created_time
                    setattr(self, attr_name, self.created_time)
            else:
                setattr(self, attr_name, attr_val)

    def get_id(self):
        return self.brew_id
    
    def public_dict(self):
        public_dict = self.__dict__.copy()
        for attr in self._REMOVED_ATTRIBUTES:
            public_dict.pop(attr, None)
        
        order_dict = OrderedDict(sorted(public_dict.items(), key=lambda i: self._PUBLIC_ATTRIBUTE_ORDER.get(i[0])))
        return order_dict

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'{self.__class__.__name__}/\n{self.__repr__()}'
    
    def create_coffee_drink(self):
        db.session.add(self)
        db.session.commit()
        log.info('Created %s with %s %s', self.COFFEE_DRINK_NAME, self.BREW_ID, self.brew_id)

    def delete_coffee_drink(self):
        db.session.delete(self)
        db.session.commit()
        log.info('Deleted %s with %s %s', self.COFFEE_DRINK_NAME, self.BREW_ID, self.brew_id)

    def update_coffee_drink(self, update_coffee_drink: UpdateCoffeeDrink):
        for attr_name, attr_val in update_coffee_drink.__dict__.items():
            if attr_val:
                setattr(self, attr_name, attr_val)
        
        db.session.commit()
        log.info('Updated %s with %s %s', self.COFFEE_DRINK_NAME, self.BREW_ID, self.brew_id)

    @staticmethod
    def get_coffee_drink(brew_id: str):
        print('get_coffee_drink')
        return CoffeeDrink.query.get(brew_id)
    
    @staticmethod
    def get_coffee_drinks_for_user(user: User, sort=None):
        order_by = CoffeeDrink.DRINK_TIME
        if sort:
            order_by = sort
            
        return CoffeeDrink.query.filter_by(user_id=user.email).order_by(desc(order_by)).all()
    
    @staticmethod
    def _delete_all():
        CoffeeDrink.query.delete()
        db.session.commit()
        log.info('Deleted all %s', CoffeeDrink.COFFEE_DRINK_NAME)
        
def _generate_brew_id(coffee_drink: CoffeeDrink):
    # Convert timestamp from secs to millisecs
    return f'{coffee_drink.user_id.split("@")[0]}-{int(coffee_drink.created_time.timestamp() * 1000)}'

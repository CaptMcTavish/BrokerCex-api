# coding: utf-8

"""
    Broker API.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: support@cexbro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body7(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'expire_date': 'str',
        'instrument': 'str',
        'limit_price': 'float',
        'order_code': 'str',
        'position_code': 'str',
        'position_effect': 'str',
        'price_link': 'str',
        'price_offset': 'float',
        'quantity': 'int',
        'side': 'str',
        'stop_price': 'float',
        'tif': 'str',
        'type': 'str'
    }

    attribute_map = {
        'expire_date': 'expireDate',
        'instrument': 'instrument',
        'limit_price': 'limitPrice',
        'order_code': 'orderCode',
        'position_code': 'positionCode',
        'position_effect': 'positionEffect',
        'price_link': 'priceLink',
        'price_offset': 'priceOffset',
        'quantity': 'quantity',
        'side': 'side',
        'stop_price': 'stopPrice',
        'tif': 'tif',
        'type': 'type'
    }

    def __init__(self, expire_date=None, instrument=None, limit_price=None, order_code=None, position_code=None, position_effect=None, price_link=None, price_offset=None, quantity=None, side=None, stop_price=None, tif=None, type=None):  # noqa: E501
        """Body7 - a model defined in Swagger"""  # noqa: E501

        self._expire_date = None
        self._instrument = None
        self._limit_price = None
        self._order_code = None
        self._position_code = None
        self._position_effect = None
        self._price_link = None
        self._price_offset = None
        self._quantity = None
        self._side = None
        self._stop_price = None
        self._tif = None
        self._type = None
        self.discriminator = None

        if expire_date is not None:
            self.expire_date = expire_date
        if instrument is not None:
            self.instrument = instrument
        if limit_price is not None:
            self.limit_price = limit_price
        self.order_code = order_code
        if position_code is not None:
            self.position_code = position_code
        if position_effect is not None:
            self.position_effect = position_effect
        if price_link is not None:
            self.price_link = price_link
        if price_offset is not None:
            self.price_offset = price_offset
        if quantity is not None:
            self.quantity = quantity
        if side is not None:
            self.side = side
        if stop_price is not None:
            self.stop_price = stop_price
        if tif is not None:
            self.tif = tif
        self.type = type

    @property
    def expire_date(self):
        """Gets the expire_date of this Body7.  # noqa: E501


        :return: The expire_date of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this Body7.


        :param expire_date: The expire_date of this Body7.  # noqa: E501
        :type: str
        """

        self._expire_date = expire_date

    @property
    def instrument(self):
        """Gets the instrument of this Body7.  # noqa: E501


        :return: The instrument of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this Body7.


        :param instrument: The instrument of this Body7.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def limit_price(self):
        """Gets the limit_price of this Body7.  # noqa: E501


        :return: The limit_price of this Body7.  # noqa: E501
        :rtype: float
        """
        return self._limit_price

    @limit_price.setter
    def limit_price(self, limit_price):
        """Sets the limit_price of this Body7.


        :param limit_price: The limit_price of this Body7.  # noqa: E501
        :type: float
        """

        self._limit_price = limit_price

    @property
    def order_code(self):
        """Gets the order_code of this Body7.  # noqa: E501

        order code must be unique  # noqa: E501

        :return: The order_code of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this Body7.

        order code must be unique  # noqa: E501

        :param order_code: The order_code of this Body7.  # noqa: E501
        :type: str
        """
        if order_code is None:
            raise ValueError("Invalid value for `order_code`, must not be `None`")  # noqa: E501

        self._order_code = order_code

    @property
    def position_code(self):
        """Gets the position_code of this Body7.  # noqa: E501


        :return: The position_code of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._position_code

    @position_code.setter
    def position_code(self, position_code):
        """Sets the position_code of this Body7.


        :param position_code: The position_code of this Body7.  # noqa: E501
        :type: str
        """

        self._position_code = position_code

    @property
    def position_effect(self):
        """Gets the position_effect of this Body7.  # noqa: E501


        :return: The position_effect of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._position_effect

    @position_effect.setter
    def position_effect(self, position_effect):
        """Sets the position_effect of this Body7.


        :param position_effect: The position_effect of this Body7.  # noqa: E501
        :type: str
        """

        self._position_effect = position_effect

    @property
    def price_link(self):
        """Gets the price_link of this Body7.  # noqa: E501


        :return: The price_link of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._price_link

    @price_link.setter
    def price_link(self, price_link):
        """Sets the price_link of this Body7.


        :param price_link: The price_link of this Body7.  # noqa: E501
        :type: str
        """

        self._price_link = price_link

    @property
    def price_offset(self):
        """Gets the price_offset of this Body7.  # noqa: E501


        :return: The price_offset of this Body7.  # noqa: E501
        :rtype: float
        """
        return self._price_offset

    @price_offset.setter
    def price_offset(self, price_offset):
        """Sets the price_offset of this Body7.


        :param price_offset: The price_offset of this Body7.  # noqa: E501
        :type: float
        """

        self._price_offset = price_offset

    @property
    def quantity(self):
        """Gets the quantity of this Body7.  # noqa: E501


        :return: The quantity of this Body7.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Body7.


        :param quantity: The quantity of this Body7.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def side(self):
        """Gets the side of this Body7.  # noqa: E501


        :return: The side of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Body7.


        :param side: The side of this Body7.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def stop_price(self):
        """Gets the stop_price of this Body7.  # noqa: E501


        :return: The stop_price of this Body7.  # noqa: E501
        :rtype: float
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this Body7.


        :param stop_price: The stop_price of this Body7.  # noqa: E501
        :type: float
        """

        self._stop_price = stop_price

    @property
    def tif(self):
        """Gets the tif of this Body7.  # noqa: E501


        :return: The tif of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._tif

    @tif.setter
    def tif(self, tif):
        """Sets the tif of this Body7.


        :param tif: The tif of this Body7.  # noqa: E501
        :type: str
        """

        self._tif = tif

    @property
    def type(self):
        """Gets the type of this Body7.  # noqa: E501

        type of order  # noqa: E501

        :return: The type of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body7.

        type of order  # noqa: E501

        :param type: The type of this Body7.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body7, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
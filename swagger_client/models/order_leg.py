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


class OrderLeg(object):
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
        'filled_quantity': 'float',
        'instrument': 'str',
        'leg_ratio': 'float',
        'position_code': 'str',
        'position_effect': 'str',
        'price': 'float',
        'quantity': 'float',
        'remaining_quantity': 'float',
        'side': 'str'
    }

    attribute_map = {
        'filled_quantity': 'filledQuantity',
        'instrument': 'instrument',
        'leg_ratio': 'legRatio',
        'position_code': 'positionCode',
        'position_effect': 'positionEffect',
        'price': 'price',
        'quantity': 'quantity',
        'remaining_quantity': 'remainingQuantity',
        'side': 'side'
    }

    def __init__(self, filled_quantity=None, instrument=None, leg_ratio=None, position_code=None, position_effect=None, price=None, quantity=None, remaining_quantity=None, side=None):  # noqa: E501
        """OrderLeg - a model defined in Swagger"""  # noqa: E501

        self._filled_quantity = None
        self._instrument = None
        self._leg_ratio = None
        self._position_code = None
        self._position_effect = None
        self._price = None
        self._quantity = None
        self._remaining_quantity = None
        self._side = None
        self.discriminator = None

        if filled_quantity is not None:
            self.filled_quantity = filled_quantity
        if instrument is not None:
            self.instrument = instrument
        if leg_ratio is not None:
            self.leg_ratio = leg_ratio
        if position_code is not None:
            self.position_code = position_code
        if position_effect is not None:
            self.position_effect = position_effect
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if remaining_quantity is not None:
            self.remaining_quantity = remaining_quantity
        if side is not None:
            self.side = side

    @property
    def filled_quantity(self):
        """Gets the filled_quantity of this OrderLeg.  # noqa: E501


        :return: The filled_quantity of this OrderLeg.  # noqa: E501
        :rtype: float
        """
        return self._filled_quantity

    @filled_quantity.setter
    def filled_quantity(self, filled_quantity):
        """Sets the filled_quantity of this OrderLeg.


        :param filled_quantity: The filled_quantity of this OrderLeg.  # noqa: E501
        :type: float
        """

        self._filled_quantity = filled_quantity

    @property
    def instrument(self):
        """Gets the instrument of this OrderLeg.  # noqa: E501


        :return: The instrument of this OrderLeg.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this OrderLeg.


        :param instrument: The instrument of this OrderLeg.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def leg_ratio(self):
        """Gets the leg_ratio of this OrderLeg.  # noqa: E501


        :return: The leg_ratio of this OrderLeg.  # noqa: E501
        :rtype: float
        """
        return self._leg_ratio

    @leg_ratio.setter
    def leg_ratio(self, leg_ratio):
        """Sets the leg_ratio of this OrderLeg.


        :param leg_ratio: The leg_ratio of this OrderLeg.  # noqa: E501
        :type: float
        """

        self._leg_ratio = leg_ratio

    @property
    def position_code(self):
        """Gets the position_code of this OrderLeg.  # noqa: E501


        :return: The position_code of this OrderLeg.  # noqa: E501
        :rtype: str
        """
        return self._position_code

    @position_code.setter
    def position_code(self, position_code):
        """Sets the position_code of this OrderLeg.


        :param position_code: The position_code of this OrderLeg.  # noqa: E501
        :type: str
        """

        self._position_code = position_code

    @property
    def position_effect(self):
        """Gets the position_effect of this OrderLeg.  # noqa: E501


        :return: The position_effect of this OrderLeg.  # noqa: E501
        :rtype: str
        """
        return self._position_effect

    @position_effect.setter
    def position_effect(self, position_effect):
        """Sets the position_effect of this OrderLeg.


        :param position_effect: The position_effect of this OrderLeg.  # noqa: E501
        :type: str
        """

        self._position_effect = position_effect

    @property
    def price(self):
        """Gets the price of this OrderLeg.  # noqa: E501


        :return: The price of this OrderLeg.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderLeg.


        :param price: The price of this OrderLeg.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OrderLeg.  # noqa: E501


        :return: The quantity of this OrderLeg.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderLeg.


        :param quantity: The quantity of this OrderLeg.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def remaining_quantity(self):
        """Gets the remaining_quantity of this OrderLeg.  # noqa: E501


        :return: The remaining_quantity of this OrderLeg.  # noqa: E501
        :rtype: float
        """
        return self._remaining_quantity

    @remaining_quantity.setter
    def remaining_quantity(self, remaining_quantity):
        """Sets the remaining_quantity of this OrderLeg.


        :param remaining_quantity: The remaining_quantity of this OrderLeg.  # noqa: E501
        :type: float
        """

        self._remaining_quantity = remaining_quantity

    @property
    def side(self):
        """Gets the side of this OrderLeg.  # noqa: E501


        :return: The side of this OrderLeg.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderLeg.


        :param side: The side of this OrderLeg.  # noqa: E501
        :type: str
        """

        self._side = side

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
        if issubclass(OrderLeg, dict):
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
        if not isinstance(other, OrderLeg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
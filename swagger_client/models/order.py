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


class Order(object):
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
        'account': 'str',
        'action_code': 'str',
        'cash_transactions': 'list[OrderCashTransactions]',
        'client_order_id': 'str',
        'executions': 'list[OrderExecution]',
        'final_status': 'bool',
        'instrument': 'str',
        'issue_time': 'datetime',
        'leg_count': 'int',
        'legs': 'list[OrderLeg]',
        'links': 'list[OrderLinks]',
        'order_code': 'str',
        'order_id': 'int',
        'price_link': 'str',
        'price_offset': 'int',
        'side': 'str',
        'status': 'str',
        'tif': 'str',
        'transaction_time': 'datetime',
        'type': 'str',
        'version': 'int'
    }

    attribute_map = {
        'account': 'account',
        'action_code': 'actionCode',
        'cash_transactions': 'cashTransactions',
        'client_order_id': 'clientOrderId',
        'executions': 'executions',
        'final_status': 'finalStatus',
        'instrument': 'instrument',
        'issue_time': 'issueTime',
        'leg_count': 'legCount',
        'legs': 'legs',
        'links': 'links',
        'order_code': 'orderCode',
        'order_id': 'orderId',
        'price_link': 'priceLink',
        'price_offset': 'priceOffset',
        'side': 'side',
        'status': 'status',
        'tif': 'tif',
        'transaction_time': 'transactionTime',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, account=None, action_code=None, cash_transactions=None, client_order_id=None, executions=None, final_status=None, instrument=None, issue_time=None, leg_count=None, legs=None, links=None, order_code=None, order_id=None, price_link=None, price_offset=None, side=None, status=None, tif=None, transaction_time=None, type=None, version=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._action_code = None
        self._cash_transactions = None
        self._client_order_id = None
        self._executions = None
        self._final_status = None
        self._instrument = None
        self._issue_time = None
        self._leg_count = None
        self._legs = None
        self._links = None
        self._order_code = None
        self._order_id = None
        self._price_link = None
        self._price_offset = None
        self._side = None
        self._status = None
        self._tif = None
        self._transaction_time = None
        self._type = None
        self._version = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if action_code is not None:
            self.action_code = action_code
        if cash_transactions is not None:
            self.cash_transactions = cash_transactions
        if client_order_id is not None:
            self.client_order_id = client_order_id
        if executions is not None:
            self.executions = executions
        if final_status is not None:
            self.final_status = final_status
        if instrument is not None:
            self.instrument = instrument
        if issue_time is not None:
            self.issue_time = issue_time
        if leg_count is not None:
            self.leg_count = leg_count
        if legs is not None:
            self.legs = legs
        if links is not None:
            self.links = links
        if order_code is not None:
            self.order_code = order_code
        if order_id is not None:
            self.order_id = order_id
        if price_link is not None:
            self.price_link = price_link
        if price_offset is not None:
            self.price_offset = price_offset
        if side is not None:
            self.side = side
        if status is not None:
            self.status = status
        if tif is not None:
            self.tif = tif
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def account(self):
        """Gets the account of this Order.  # noqa: E501


        :return: The account of this Order.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Order.


        :param account: The account of this Order.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def action_code(self):
        """Gets the action_code of this Order.  # noqa: E501


        :return: The action_code of this Order.  # noqa: E501
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        """Sets the action_code of this Order.


        :param action_code: The action_code of this Order.  # noqa: E501
        :type: str
        """

        self._action_code = action_code

    @property
    def cash_transactions(self):
        """Gets the cash_transactions of this Order.  # noqa: E501


        :return: The cash_transactions of this Order.  # noqa: E501
        :rtype: list[OrderCashTransactions]
        """
        return self._cash_transactions

    @cash_transactions.setter
    def cash_transactions(self, cash_transactions):
        """Sets the cash_transactions of this Order.


        :param cash_transactions: The cash_transactions of this Order.  # noqa: E501
        :type: list[OrderCashTransactions]
        """

        self._cash_transactions = cash_transactions

    @property
    def client_order_id(self):
        """Gets the client_order_id of this Order.  # noqa: E501


        :return: The client_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this Order.


        :param client_order_id: The client_order_id of this Order.  # noqa: E501
        :type: str
        """

        self._client_order_id = client_order_id

    @property
    def executions(self):
        """Gets the executions of this Order.  # noqa: E501


        :return: The executions of this Order.  # noqa: E501
        :rtype: list[OrderExecution]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """Sets the executions of this Order.


        :param executions: The executions of this Order.  # noqa: E501
        :type: list[OrderExecution]
        """

        self._executions = executions

    @property
    def final_status(self):
        """Gets the final_status of this Order.  # noqa: E501


        :return: The final_status of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._final_status

    @final_status.setter
    def final_status(self, final_status):
        """Sets the final_status of this Order.


        :param final_status: The final_status of this Order.  # noqa: E501
        :type: bool
        """

        self._final_status = final_status

    @property
    def instrument(self):
        """Gets the instrument of this Order.  # noqa: E501


        :return: The instrument of this Order.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this Order.


        :param instrument: The instrument of this Order.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def issue_time(self):
        """Gets the issue_time of this Order.  # noqa: E501


        :return: The issue_time of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._issue_time

    @issue_time.setter
    def issue_time(self, issue_time):
        """Sets the issue_time of this Order.


        :param issue_time: The issue_time of this Order.  # noqa: E501
        :type: datetime
        """

        self._issue_time = issue_time

    @property
    def leg_count(self):
        """Gets the leg_count of this Order.  # noqa: E501


        :return: The leg_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._leg_count

    @leg_count.setter
    def leg_count(self, leg_count):
        """Sets the leg_count of this Order.


        :param leg_count: The leg_count of this Order.  # noqa: E501
        :type: int
        """

        self._leg_count = leg_count

    @property
    def legs(self):
        """Gets the legs of this Order.  # noqa: E501


        :return: The legs of this Order.  # noqa: E501
        :rtype: list[OrderLeg]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this Order.


        :param legs: The legs of this Order.  # noqa: E501
        :type: list[OrderLeg]
        """

        self._legs = legs

    @property
    def links(self):
        """Gets the links of this Order.  # noqa: E501


        :return: The links of this Order.  # noqa: E501
        :rtype: list[OrderLinks]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Order.


        :param links: The links of this Order.  # noqa: E501
        :type: list[OrderLinks]
        """

        self._links = links

    @property
    def order_code(self):
        """Gets the order_code of this Order.  # noqa: E501


        :return: The order_code of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this Order.


        :param order_code: The order_code of this Order.  # noqa: E501
        :type: str
        """

        self._order_code = order_code

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501


        :return: The order_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.


        :param order_id: The order_id of this Order.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def price_link(self):
        """Gets the price_link of this Order.  # noqa: E501


        :return: The price_link of this Order.  # noqa: E501
        :rtype: str
        """
        return self._price_link

    @price_link.setter
    def price_link(self, price_link):
        """Sets the price_link of this Order.


        :param price_link: The price_link of this Order.  # noqa: E501
        :type: str
        """

        self._price_link = price_link

    @property
    def price_offset(self):
        """Gets the price_offset of this Order.  # noqa: E501


        :return: The price_offset of this Order.  # noqa: E501
        :rtype: int
        """
        return self._price_offset

    @price_offset.setter
    def price_offset(self, price_offset):
        """Sets the price_offset of this Order.


        :param price_offset: The price_offset of this Order.  # noqa: E501
        :type: int
        """

        self._price_offset = price_offset

    @property
    def side(self):
        """Gets the side of this Order.  # noqa: E501


        :return: The side of this Order.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Order.


        :param side: The side of this Order.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501


        :return: The status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tif(self):
        """Gets the tif of this Order.  # noqa: E501


        :return: The tif of this Order.  # noqa: E501
        :rtype: str
        """
        return self._tif

    @tif.setter
    def tif(self, tif):
        """Sets the tif of this Order.


        :param tif: The tif of this Order.  # noqa: E501
        :type: str
        """

        self._tif = tif

    @property
    def transaction_time(self):
        """Gets the transaction_time of this Order.  # noqa: E501


        :return: The transaction_time of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this Order.


        :param transaction_time: The transaction_time of this Order.  # noqa: E501
        :type: datetime
        """

        self._transaction_time = transaction_time

    @property
    def type(self):
        """Gets the type of this Order.  # noqa: E501


        :return: The type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.


        :param type: The type of this Order.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this Order.  # noqa: E501


        :return: The version of this Order.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Order.


        :param version: The version of this Order.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

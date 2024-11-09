#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Binance API
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Binance API.
#
# Hive Binance API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Binance API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Binance API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """


class AccountAPI(object):

    def self_account(self):
        url = self.neo_url + "account"
        contents = self.get(url, sign=True)
        return contents

    def withdraw_account(
        self, asset, address, amount, address_tag=None, address_name=None
    ):
        url = self.wapi_url + "withdraw.html"
        contents = self.post(
            url,
            params=dict(
                asset=asset,
                address=address,
                amount=amount,
                addressTag=address_tag,
                name=address_name,
            ),
            data=b"",
            mime="application/x-www-form-urlencoded",
            sign=True,
        )
        return contents

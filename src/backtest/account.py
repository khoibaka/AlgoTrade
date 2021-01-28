class Account:
    def __init__(self, starting_budget: float):
        self.__starting_budget = starting_budget
        self.__budget = starting_budget
        self.__asset = 0

    # Getters and setter ------
    def set_budget(self, budget: float) -> None:
        self.__budget = budget

    def set_asset(self, asset: float) -> None:
        self.__asset = asset

    def get_budget(self) -> float:
        return self.__budget

    def get_asset(self) -> float:
        return self.__asset

    def get_account(self, conversion_rate) -> dict:
        return {
            'budget': self.__budget,
            'asset': self.__asset,
            'value': self.get_account_value(conversion_rate)
        }
    # Add and subtract function -------

    def add_asset(self, asset: float) -> float:
        self.__asset += asset
        return self.__asset

    def subtract_asset(self, asset: float) -> float:
        self.__asset -= asset
        return self.__asset

    def add_budget(self, budget: float) -> None:
        self.__budget += budget
        return self.__budget

    def subtract_budget(self, budget: float) -> None:
        self.__budget -= budget
        return self.__budget

    # Get account value
    def get_account_value(self, conversion_rate: float) -> float:
        try:
            asset_value = self.__asset * conversion_rate
            return self.__budget + asset_value
        except:
            raise ValueError("Please provide conversion rate for all asset")


if __name__ == "__main__":
    account = Account(starting_budget=100)
    print(account.add_asset(asset=200))
    print(account.get_budget())

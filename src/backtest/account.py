class Account:
    def __init__(self, starting_budget: float):
        self.__starting_budget = starting_budget
        self.__budget = starting_budget
        self.__assets = {}

    # Getters and setter ------
    def set_budget(self, budget: float) -> None:
        self.__budget = budget

    def set_asset(self, asset_name: str, asset: float) -> None:
        self.__asset[asset_name] = asset

    def get_budget(self) -> float:
        return self.__budget

    def get_asset(self, asset_name: str) -> float:
        return self.__assets[asset_name]

    # Add and subtract function -------
    def add_asset(self, asset_name: str, asset: float) -> float:
        self.__assets[asset_name] = self.__assets.get(asset_name, 0) + asset
        return self.__assets[asset_name]

    def subtract_asset(self, asset_name: str, asset: float) -> float:
        self.__assets[asset_name] = self.__assets.get(asset_name, 0) - asset
        return self.__assets[asset_name]

    def add_budget(self, budget: float) -> None:
        self.__budget += budget
        return self.__budget

    def subtract_budget(self, budget: float) -> None:
        self.__budget -= budget
        return self.__budget

    # Get account value
    def get_account_value(self, conversion_rates: dict) -> float:
        try:
            asset_values = [v * conversion_rates[k] for k, v in self.__assets]
            return self.__budget + sum(asset_values)
        except:
            raise ValueError("Please provide conversion rate for all asset")


if __name__ == "__main__":
    account = Account(starting_budget=100)
    print(account.add_asset(asset_name="BCN", asset=200))
    print(account.get_budget())
    print(account.get_asset("BCN"))

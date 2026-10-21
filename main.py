import math

class SneakerModel:
    def __init__(self, name, retail_price, initial_supply, base_demand, initial_hype_factor):
        self.name = name
        self.retail_price = retail_price
        self.initial_supply = initial_supply
        self.base_demand = base_demand # Represents inherent desirability/potential buyers
        self.hype_factor = initial_hype_factor # Multiplier for current hype (e.g., 0.5 for low, 2.5 for high)
        self.market_saturation = 0.0 # Factor representing market fatigue or oversupply

    def calculate_resale_price(self):
        """
        Calculates the theoretical resale price based on supply, demand, hype,
        and market saturation. The model aims to show how these factors can lead
        to prices above or below retail.
        """
        # Calculate a base premium factor based on demand relative to supply.
        # If demand > supply, this factor is > 1. If demand < supply, it's < 1.
        demand_supply_ratio = self.base_demand / self.initial_supply

        # The 'premium' is influenced by this ratio and the current hype factor.
        # A scaling constant (0.1) is used to make the premium percentage realistic.
        # This ensures that a ratio of 2 with high hype doesn't mean 200% premium directly.
        premium_potential = demand_supply_ratio * self.hype_factor * 0.1

        # Market saturation directly reduces the potential premium or increases the discount.
        # This is a key factor in prices falling below retail.
        final_price_multiplier = 1 + premium_potential - self.market_saturation

        calculated_price = self.retail_price * final_price_multiplier

        # Ensure price has a realistic floor (e.g., 50% of retail) to prevent absurdly low values.
        # The article specifically mentions falling *below retail*, so we allow that.
        return max(self.retail_price * 0.5, calculated_price)

    def update_market_conditions(self, new_hype_factor=None, new_saturation=None):
        if new_hype_factor is not None:
            self.hype_factor = new_hype_factor
        if new_saturation is not None:
            self.market_saturation = new_saturation

def main():
    print("Nike Dunk Low Resale Market Simulation\n")

    # Scenario 1: Early Hype (e.g., 2020-2022) - Limited supply, high hype
    # Prices are significantly above retail due to high demand and scarcity.
    print("--- Scenario 1: Early Hype (e.g., 2020-2022) ---")
    dunk_panda_early = SneakerModel(
        name="Dunk Low 'Panda' (Early Drop)",
        retail_price=110,
        initial_supply=50000,  # Relatively limited for a popular model
        base_demand=100000,    # High inherent demand
        initial_hype_factor=2.5 # Very high hype multiplier
    )
    resale_price_early = dunk_panda_early.calculate_resale_price()
    print(f"{dunk_panda_early.name}:")
    print(f"  Retail Price: ${dunk_panda_early.retail_price:.2f}")
    print(f"  Initial Supply: {dunk_panda_early.initial_supply}")
    print(f"  Hype Factor: {dunk_panda_early.hype_factor}")
    print(f"  Calculated Resale Price: ${resale_price_early:.2f}")
    # Illustrates prices well above retail due to high hype and limited supply.
    print(f"  Status: {'ABOVE RETAIL' if resale_price_early > dunk_panda_early.retail_price else 'BELOW RETAIL' if resale_price_early < dunk_panda_early.retail_price else 'AT RETAIL'}\n")

    # Scenario 2: Peak Popularity, Increased Supply (e.g., 2023) - Still high, but premium shrinks
    # As supply increases to meet demand, the premium over retail starts to decrease.
    print("--- Scenario 2: Peak Popularity, Increased Supply (e.g., 2023) ---")
    dunk_panda_peak = SneakerModel(
        name="Dunk Low 'Panda' (Peak Popularity)",
        retail_price=110,
        initial_supply=200000, # Supply increased significantly due to sustained demand
        base_demand=100000,
        initial_hype_factor=1.8 # Hype still high, but slightly less intense than initial peak
    )
    resale_price_peak = dunk_panda_peak.calculate_resale_price()
    print(f"{dunk_panda_peak.name}:")
    print(f"  Retail Price: ${dunk_panda_peak.retail_price:.2f}")
    print(f"  Initial Supply: {dunk_panda_peak.initial_supply}")
    print(f"  Hype Factor: {dunk_panda_peak.hype_factor}")
    print(f"  Calculated Resale Price: ${resale_price_peak:.2f}")
    print(f"  Status: {'ABOVE RETAIL' if resale_price_peak > dunk_panda_peak.retail_price else 'BELOW RETAIL' if resale_price_peak < dunk_panda_peak.retail_price else 'AT RETAIL'}\n")

    # Scenario 3: Market Saturation & Decreased Hype (e.g., 2026 prediction)
    # This scenario directly addresses the article's core prediction: prices falling below retail.
    # Factors include high supply, significantly reduced hype, and market saturation.
    print("--- Scenario 3: Market Saturation & Decreased Hype (e.g., 2026 Prediction) ---")
    dunk_panda_future = SneakerModel(
        name="Dunk Low 'Panda' (2026 Prediction)",
        retail_price=110,
        initial_supply=300000, # Even higher supply, widely available
        base_demand=100000,
        initial_hype_factor=0.8 # Hype significantly decreased as trend fades
    )
    # Crucially, introduce market saturation, which acts as a direct price depressor.
    dunk_panda_future.update_market_conditions(new_saturation=0.3) # Significant market saturation
    resale_price_future = dunk_panda_future.calculate_resale_price()
    print(f"{dunk_panda_future.name}:")
    print(f"  Retail Price: ${dunk_panda_future.retail_price:.2f}")
    print(f"  Initial Supply: {dunk_panda_future.initial_supply}")
    print(f"  Hype Factor: {dunk_panda_future.hype_factor}")
    print(f"  Market Saturation Factor: {dunk_panda_future.market_saturation}")
    print(f"  Calculated Resale Price: ${resale_price_future:.2f}")
    # This demonstrates how increased supply, decreased hype, and market saturation
    # can lead to prices falling below retail, aligning with the article's prediction for 2026.
    print(f"  Status: {'ABOVE RETAIL' if resale_price_future > dunk_panda_future.retail_price else 'BELOW RETAIL' if resale_price_future < dunk_panda_future.retail_price else 'AT RETAIL'}\n")

if __name__ == "__main__":
    main()

import re
import sys


def calculate_total(items):
    """Calculate the total of a list of numbers."""
    total = 0
    for item in items:
        if isinstance(item, (int, float)):
            total += item
    return total


class DataProcessor:
    """Process and analyze data."""

    def __init__(self, data):
        self.data = data

    def filter_data(self, threshold=10):
        """Filter data above threshold."""
        return [x for x in self.data if x > threshold]

    def compute_stats(self):
        """Compute basic statistics."""
        if not self.data:
            return None
        return {
            'mean': sum(self.data) / len(self.data),
            'max': max(self.data),
            'min': min(self.data)
        }


# Main execution
if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25]
    processor = DataProcessor(numbers)

    print(f"Total: {calculate_total(numbers)}")
    print(f"Filtered (>10): {processor.filter_data()}")
    print(f"Statistics: {processor.compute_stats()}")
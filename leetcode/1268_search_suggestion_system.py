from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        products.sort()
        res = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            idx = binary_search(products, prefix)
            search_results = [
                product
                for product in products[idx : idx + 3]
                if product.startswith(prefix)
            ]
            res.append(search_results)

        return res

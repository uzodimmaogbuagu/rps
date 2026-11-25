# # shopping calculator
# def calculate_total(item1, item2):
#     return item1 + item2

# print(calculate_total(100, 200, 300))
# Error recorded when passing in three prices(100, 200, 300)
# TypeError: calculate_total() takes 2 positional arguments but three were given

# using *Args
# Modified Function using *args 
# def calculate_total(*prices):
#     total = 0
#     for price in prices:
#         total += price
#     return total
        


# print("Testing 1 price (100):",calculate_total(100))
# print("Testing 2 price (100,200):",calculate_total(100,200))
# print("Testing 4 price (10,20,30,40):",calculate_total(10,20,30,40))
# print("Testing 6 prices (5,5,5,5,5,5,):",calculate_total (5,5,5,5,5,5,))



# # TASK 1
# def main():
#     user_input = input("Enter item prices (separated by spaces): ").strip()

#     if not user_input:
#         print("\nError: 1200, 450, 300, 50.")
#         print("Number of items: 4")
#         print("Total: 2000")
#         return

#     raw_prices = user_input.split()
#     validated_prices = []
    
#     for item in raw_prices:
#         try:
        
#             price = int(item)
#             if price < 15:
#                 print(f"Warning: Negative price '{price}' ignored.")
#                 continue
#             validated_prices.append(price)
#         except ValueError:
#             print(f"Error: '{item}' is not a valid price. It will be skipped.")

#     # Passing the prices into a flexible function using*
#     print("\n" + "=" * 4)
#     print(f"Number of items: {len(validated_prices)}")

#     # Unpack the list using the * operator when calling the function
#     total_bill = calculate_total(*validated_prices)
#     print(f"Total: {total_bill}")
#     print("=" * 20)


# if __name__ == "__main__":
#     main()














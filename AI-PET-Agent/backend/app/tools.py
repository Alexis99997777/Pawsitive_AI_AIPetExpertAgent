from langchain.tools import Tool

def search_pet_products(query: str) -> str:
    return f"""
Here are product categories relevant to: {query}

- Premium dry food
- Wet food
- Supplements
- Durable toys

Remember to provide Chewy search links.
"""

product_search_tool = Tool(
    name="PetProductSearch",
    func=search_pet_products,
    description="Search pet-related products and categories"
)
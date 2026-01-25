class chai:
    origin = "India"
    size = "Medium"


cutting = chai()
print(f"Cutting is from {cutting.size}.")

cutting.size = "Large"
del cutting.size
print(
    f"After deletion, Cutting is from {cutting.size}. <- This is called the shodowing effect. The instance variable 'size' was deleted, so it refers back to the class variable."
)
cutting.strength = "Strong"
print(f"Cutting has a {cutting.strength} strength.")

del cutting.strength
# print(f"After deletion: {cutting.strength}")  # This will raise an AttributeError since 'strength' was deleted.
